from __future__ import annotations

from typing import Any

from .opportunity_engine import build_opportunities
from .root_cause_engine import build_root_cause_analysis
from .business_impact_engine import build_business_impact
from .risk_ranking_engine import build_risk_ranking
from .cash_conversion_engine import build_cash_conversion_cycle
from .trend_engine import build_trend_analysis
from .benchmarking_engine import build_benchmark_analysis
from .executive_summary_engine import build_executive_summary
from .cash_bridge_engine import build_cash_bridge
from .profit_quality_engine import build_profit_quality
from .action_engine import build_management_actions
from .validation_engine import build_calculation_audit
from .scenario_engine import build_scenarios
from .gap_detection_engine import build_gap_detection, build_extended_root_cause
from .operational_finance_engine import build_operational_finance
from .finding_registry import build_finding_registry
from .strategy_playbook import build_strategy_playbook
from .narrative_engine import build_narrative_engine
from .dupont_engine import build_dupont_analysis


def _safe_div(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return float(a) / float(b)


def _clamp(v: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, v))


def _score_band(value: float | None, bands: list[tuple[float, float]], default: float = 0.0) -> float:
    if value is None:
        return default
    for threshold, score in bands:
        if value >= threshold:
            return score
    return default


def _severity_rank(severity: str) -> int:
    return {"critical": 4, "high": 3, "medium": 2, "low": 1, "positive": 0}.get(severity, 0)


def build_finance_business_partner_analysis(
    statements: dict[str, Any],
    quality: dict[str, Any],
    sector: str | None = None,
    previous_periods: list[dict[str, Any]] | None = None,
    data_hub: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Deterministic first-generation Finance Business Partner decision engine.

    This engine does not ask an LLM to invent financial facts. It derives evidence,
    risks, opportunities and impact estimates from the canonical financial model.
    Thresholds are general-purpose financial guardrails, not industry benchmarks.
    """
    pl = statements["profit_and_loss"]
    bs = statements["balance_sheet"]
    k = statements["kpis"]

    net_sales = float(pl.get("Net sales") or 0.0)
    gross_profit = float(pl.get("Gross profit") or 0.0)
    operating_profit = float(pl.get("Operating profit") or 0.0)
    net_profit = float(pl.get("Net profit") or 0.0)
    finance_costs = float(pl.get("Finance costs") or 0.0)
    other_operating_income = float(pl.get("Other operating income") or 0.0)
    other_non_operating_income = float(pl.get("Other non-operating income") or 0.0)
    total_assets = float(bs.get("Total assets") or 0.0)
    current_assets = float(bs.get("Current assets") or 0.0)
    current_liabilities = float(bs.get("Current liabilities") or 0.0)
    total_equity = float(bs.get("Total equity incl. current result") or 0.0)

    financial_debt = float(k.get("financial_debt") or 0.0)
    net_debt = float(k.get("net_debt") or 0.0)
    cash = float(k.get("cash") or 0.0)
    receivables = float(k.get("receivables") or 0.0)
    inventory = float(k.get("inventory") or 0.0)

    gross_margin = k.get("gross_margin_pct")
    operating_margin = k.get("operating_margin_pct")
    net_margin = k.get("net_margin_pct")
    current_ratio = k.get("current_ratio")
    quick_ratio = k.get("quick_ratio")
    cash_ratio = k.get("cash_ratio")
    debt_to_equity = k.get("debt_to_equity")
    roa = k.get("return_on_assets_pct")
    roe = k.get("return_on_equity_pct")
    asset_turnover = k.get("asset_turnover")

    finance_cost_to_op = _safe_div(finance_costs, operating_profit)
    interest_coverage_proxy = _safe_div(operating_profit, finance_costs)
    debt_to_assets = _safe_div(financial_debt, total_assets)
    equity_ratio = _safe_div(total_equity, total_assets)
    cash_to_debt = _safe_div(cash, financial_debt)
    receivables_to_sales = _safe_div(receivables, net_sales)
    non_core_income = other_operating_income + other_non_operating_income
    non_core_income_to_pbt = _safe_div(non_core_income, float(pl.get("Pre-tax profit") or 0.0))

    # ----- Health score -----
    data_score = float(quality.get("score") or 0.0)
    data_component = _clamp(data_score) * 0.15

    liquidity_points = 0.0
    if current_ratio is not None:
        liquidity_points += _score_band(current_ratio, [(1.50, 10), (1.20, 8), (1.00, 6), (0.80, 3)], 0)
    if cash_ratio is not None:
        liquidity_points += _score_band(cash_ratio, [(0.50, 10), (0.30, 8), (0.15, 5), (0.05, 2)], 0)

    leverage_points = 0.0
    if debt_to_equity is not None:
        if debt_to_equity <= 1.0: leverage_points += 12
        elif debt_to_equity <= 2.0: leverage_points += 9
        elif debt_to_equity <= 3.0: leverage_points += 6
        elif debt_to_equity <= 5.0: leverage_points += 3
    if finance_cost_to_op is not None:
        if finance_cost_to_op <= 0.20: leverage_points += 13
        elif finance_cost_to_op <= 0.35: leverage_points += 10
        elif finance_cost_to_op <= 0.50: leverage_points += 6
        elif finance_cost_to_op <= 0.75: leverage_points += 3

    profitability_points = 0.0
    if operating_margin is not None:
        profitability_points += _score_band(operating_margin, [(15, 13), (10, 10), (5, 6), (0, 3)], 0)
    if net_margin is not None:
        profitability_points += _score_band(net_margin, [(10, 12), (5, 9), (2, 5), (0, 2)], 0)

    efficiency_points = 0.0
    if asset_turnover is not None:
        efficiency_points += _score_band(asset_turnover, [(1.5, 8), (1.0, 6), (0.7, 4), (0.4, 2)], 0)
    if equity_ratio is not None:
        efficiency_points += _score_band(equity_ratio, [(0.40, 7), (0.30, 5), (0.20, 3), (0.10, 1)], 0)

    health_score = round(_clamp(data_component + liquidity_points + leverage_points + profitability_points + efficiency_points), 1)
    health_label = "Güçlü" if health_score >= 80 else "Dengeli" if health_score >= 65 else "Dikkat Gerektiriyor" if health_score >= 50 else "Yüksek Risk"

    findings: list[dict[str, Any]] = []

    def add_finding(code: str, category: str, severity: str, title: str, evidence: list[str], interpretation: str, recommendation: str, confidence: str = "high"):
        findings.append({
            "code": code,
            "category": category,
            "severity": severity,
            "title": title,
            "evidence": evidence,
            "interpretation": interpretation,
            "recommendation": recommendation,
            "confidence": confidence,
        })

    # Profitability
    if operating_margin is not None:
        if operating_margin >= 12:
            add_finding("P001", "Kârlılık", "positive", "Faaliyet kârlılığı güçlü", [f"Operating margin %{operating_margin:.1f}", f"Operating profit {operating_profit:,.0f} TL"], "Ana faaliyetler anlamlı bir kâr marjı üretiyor.", "Faaliyet marjını korurken finansman ve işletme sermayesi baskısını azaltmaya odaklan.")
        elif operating_margin < 5:
            add_finding("P002", "Kârlılık", "high", "Faaliyet marjı zayıf", [f"Operating margin %{operating_margin:.1f}"], "Satışlar faaliyet seviyesinde sınırlı kâra dönüşüyor.", "Brüt marj, fiyatlama, ürün/müşteri karması ve faaliyet giderlerini ayrıştırarak marj kök neden analizi yap.")

    if gross_margin is not None and gross_margin < 15:
        add_finding("P003", "Kârlılık", "medium", "Brüt marj sınırlı", [f"Gross margin %{gross_margin:.1f}"], "Maliyet veya fiyatlama baskısı faaliyet kârlılığı için düşük tampon bırakıyor.", "Fiyatlama, indirimler ve satış maliyetini müşteri/ürün bazında analiz et.")

    # Financing pressure
    if finance_cost_to_op is not None:
        pct = finance_cost_to_op * 100
        if finance_cost_to_op > 0.60:
            sev = "critical"
        elif finance_cost_to_op > 0.40:
            sev = "high"
        elif finance_cost_to_op > 0.25:
            sev = "medium"
        else:
            sev = "positive"
        add_finding(
            "L001", "Borçluluk", sev,
            "Finansman gider baskısı" if sev != "positive" else "Finansman gider yükü kontrollü",
            [f"Finance costs / Operating profit %{pct:.1f}", f"Finance costs {finance_costs:,.0f} TL", f"Operating profit {operating_profit:,.0f} TL"],
            "Finansman giderleri faaliyet kârının önemli bölümünü tüketiyor." if sev != "positive" else "Faaliyet kârının büyük kısmı finansman giderlerinden sonra korunuyor.",
            "Borç kompozisyonu, faiz oranları, vade yapısı ve işletme sermayesi finansman ihtiyacını gözden geçir." if sev != "positive" else "Mevcut finansman disiplinini koru.",
        )

    if debt_to_equity is not None:
        if debt_to_equity > 5:
            sev = "critical"
        elif debt_to_equity > 3:
            sev = "high"
        elif debt_to_equity > 2:
            sev = "medium"
        else:
            sev = "positive"
        add_finding(
            "L002", "Borçluluk", sev,
            "Finansal kaldıraç yüksek" if sev != "positive" else "Finansal kaldıraç makul",
            [f"Financial debt / Equity {debt_to_equity:.2f}x", f"Financial debt {financial_debt:,.0f} TL", f"Equity {total_equity:,.0f} TL"],
            "Borç seviyesi özkaynak tabanına göre yüksek; refinansman ve faiz hassasiyeti artıyor." if sev != "positive" else "Borç/özkaynak dengesi genel eşiklerde yönetilebilir seviyede.",
            "Kısa vadeli borç azaltımı, özkaynak güçlendirme ve borç vadesini uzatma seçeneklerini karşılaştır." if sev != "positive" else "Borçluluk seviyesini yeni yatırımlarda disiplinli izle.",
        )

    # Liquidity
    if current_ratio is not None:
        if current_ratio < 1.0:
            add_finding("Q001", "Likidite", "critical", "Kısa vadeli likidite açığı", [f"Current ratio {current_ratio:.2f}x"], "Dönen varlıklar kısa vadeli yükümlülükleri tam karşılamıyor.", "13 haftalık nakit planı, tahsilat hızlandırma ve kısa vadeli borç yeniden yapılandırması önceliklendirilmeli.")
        elif current_ratio < 1.2:
            add_finding("Q002", "Likidite", "medium", "Likidite tamponu sınırlı", [f"Current ratio {current_ratio:.2f}x", f"Cash ratio {cash_ratio:.2f}x" if cash_ratio is not None else ""], "Kısa vadeli yükümlülükler karşılanabiliyor ancak hata payı düşük.", "Nakit tamponu ve tahsilat planını stres senaryolarıyla izle.")

    # Cash vs debt
    if cash_to_debt is not None and cash_to_debt < 0.5:
        add_finding("Q003", "Likidite", "high", "Nakit finansal borcu sınırlı karşılıyor", [f"Cash / Financial debt %{cash_to_debt*100:.1f}", f"Net debt {net_debt:,.0f} TL"], "Mevcut nakit finansal borcun yarısından azını karşılıyor.", "Serbest nakit yaratımı ve borç azaltımını birlikte planla.")

    # Receivables concentration at statement level
    if receivables_to_sales is not None and receivables_to_sales > 0.50:
        add_finding("W001", "İşletme Sermayesi", "high", "Alacak bakiyesi satışlara göre yüksek", [f"Receivables / Net sales %{receivables_to_sales*100:.1f}", f"Receivables {receivables:,.0f} TL"], "Satışların önemli bölümü bilanço tarihinde henüz nakde dönüşmemiş görünüyor. Dönem bilgisi ve aging olmadan DSO kesin hesaplanamaz.", "AR aging yükleyerek gecikme, müşteri yoğunlaşması ve DSO analizini derinleştir.", confidence="medium")

    # Earnings quality
    if non_core_income_to_pbt is not None and non_core_income_to_pbt > 0.30:
        add_finding("E001", "Kazanç Kalitesi", "medium", "Faaliyet dışı/ikincil gelirlerin kâra katkısı yüksek", [f"Other income / PBT %{non_core_income_to_pbt*100:.1f}", f"Other income {non_core_income:,.0f} TL"], "Vergi öncesi kârın anlamlı bir bölümü ana faaliyet dışındaki gelirlerden destekleniyor olabilir.", "Sürdürülebilir faaliyet kârlılığını diğer gelirlerden ayrı takip et.")

    # Efficiency
    if asset_turnover is not None and asset_turnover < 0.6:
        add_finding("A001", "Verimlilik", "medium", "Varlık devir hızı düşük", [f"Asset turnover {asset_turnover:.2f}x"], "Varlık tabanı satış üretimine göre ağır olabilir.", "Atıl varlıklar ve sermaye bağlayan kalemleri incele.")


    # Advanced Risk Rules V1.3

    if debt_to_assets is not None:
        if debt_to_assets > 0.70:
            add_finding("D004","Borçluluk","critical","Borç yükü kritik seviyede",
                        [f"Debt / Assets %{debt_to_assets*100:.1f}"],
                        "Varlıkların önemli bölümü borç ile finanse edilmektedir.",
                        "Borç azaltımı ve sermaye güçlendirme seçenekleri değerlendirilmelidir.")
        elif debt_to_assets > 0.50:
            add_finding("D005","Borçluluk","high","Borç yoğunluğu yüksek",
                        [f"Debt / Assets %{debt_to_assets*100:.1f}"],
                        "Borç seviyesi finansal esnekliği azaltabilir.",
                        "Borç yapısı yakından izlenmelidir.")

    if interest_coverage_proxy is not None:
        if interest_coverage_proxy < 1.5:
            add_finding("D006","Borçluluk","critical","Faiz karşılama seviyesi kritik",
                        [f"Interest Coverage {interest_coverage_proxy:.2f}x"],
                        "Faaliyet karı faiz yükünü taşımakta zorlanıyor.",
                        "Borç maliyetleri ve finansman yapısı gözden geçirilmelidir.")
        elif interest_coverage_proxy < 3:
            add_finding("D007","Borçluluk","high","Faiz karşılama seviyesi zayıf",
                        [f"Interest Coverage {interest_coverage_proxy:.2f}x"],
                        "Faiz giderleri karlılığı baskılıyor.",
                        "Faiz maliyetlerini azaltacak aksiyonlar değerlendirilmelidir.")

    if total_equity < 0:
        add_finding("D008","Borçluluk","critical","Negatif özkaynak",
                    [f"Equity {total_equity:,.0f} TL"],
                    "Şirket sermaye erozyonu yaşamaktadır.",
                    "Özkaynak yapısı acilen güçlendirilmelidir.")

    if receivables_to_sales is not None and debt_to_equity is not None:
        if receivables_to_sales > 0.40 and debt_to_equity > 2:
            add_finding("WC004","İşletme Sermayesi","high",
                        "İşletme sermayesi finansman baskısı",
                        [f"Receivables/Sales %{receivables_to_sales*100:.1f}",
                         f"Debt/Equity {debt_to_equity:.2f}x"],
                        "Yüksek alacak seviyesi kredi ihtiyacını artırıyor olabilir.",
                        "Tahsilat performansı ve müşteri vadeleri analiz edilmelidir.")

    # Priority = severity/financial impact/actionability proxy.
    findings_sorted = sorted(findings, key=lambda x: (_severity_rank(x["severity"]), len(x["evidence"])), reverse=True)

    # ----- 5. Opportunity Engine -----
    opportunities_sorted = build_opportunities(statements)

    # ----- 1. Root Cause Engine -----
    # Master Decision Hub (Faz 1): Root Cause now consumes the Findings list
    # itself instead of independently re-deriving its own threshold checks -
    # see root_cause_engine.build_root_cause_analysis docstring for why that
    # matters (threshold drift risk between two copies of "the same" rule).
    root_cause = build_root_cause_analysis(statements, findings=findings_sorted)
    gap_detection = build_gap_detection(statements, quality, data_hub) if data_hub is not None else build_gap_detection(statements, quality, None)
    root_cause = build_extended_root_cause(statements, root_cause, data_hub or {}, gap_detection)
    operational_finance = build_operational_finance(data_hub, statements)
    chain_by_finding_code: dict[str, str] = {}
    for chain in root_cause["causal_chains"]:
        for code in chain.get("related_findings", []):
            chain_by_finding_code[code] = " → ".join(chain["chain"])
    for f in findings_sorted:
        if f["code"] in chain_by_finding_code:
            f["root_cause"] = chain_by_finding_code[f["code"]]

    # ----- 2. Business Impact Engine -----
    business_impact = build_business_impact(statements, findings_sorted, opportunities_sorted)

    # ----- 4. Risk Ranking Engine -----
    risk_ranking = build_risk_ranking(findings_sorted, business_impact, statements)

    # ----- Priority Score (Master Decision Hub, Faz 1) -----
    # Risk Ranking's composite risk_score (severity x confidence x financial
    # exposure, see risk_ranking_engine.py) IS the Priority Score in the
    # Finding -> Root Cause -> Business Impact -> Priority Score -> Action
    # pipeline. Before this, Management Actions ordered its own groups by a
    # bare severity_rank computed independently of Risk Ranking, so two
    # findings tied on severity could be prioritized differently by the
    # Risk list and the Action list. This map is the one thing that carries
    # the Priority Score forward into Action Engine's own ordering.
    priority_by_code: dict[str, float] = {
        code: r["risk_score"]
        for r in risk_ranking.get("ranked_risks", [])
        for code in r.get("contributing_codes", [r.get("code")])
    }

    # ----- 6. Cash Conversion Cycle Engine -----
    period_days = None
    if isinstance(statements.get("period_metadata"), dict):
        period_days = statements["period_metadata"].get("period_days")
    ccc = build_cash_conversion_cycle(statements, period_days=period_days)

    # ----- 7. Trend Analysis Engine -----
    trend = build_trend_analysis(statements, previous_periods)

    # ----- 8. Benchmarking Engine -----
    benchmark = build_benchmark_analysis(statements, sector)

    actions = []
    for f in findings_sorted:
        if f["severity"] in {"critical", "high", "medium"}:
            actions.append({
                "priority": len(actions) + 1,
                "title": f["recommendation"],
                "reason": f["title"],
                "severity": f["severity"],
                "area": f["category"],
            })
        if len(actions) >= 5:
            break

    previous_statement = previous_periods[-1].get("statements") if previous_periods else None
    cash_bridge = build_cash_bridge(statements, previous_statement)
    profit_quality = build_profit_quality(statements, findings=findings_sorted)
    management_actions = build_management_actions(
        findings_sorted, opportunities_sorted, statements,
        causal_chains=root_cause.get('causal_chains'), gap_detection=gap_detection,
        priority_by_code=priority_by_code,
    )
    calculation_audit = build_calculation_audit(statements)

    # ----- 3. Executive Summary Engine -----
    # Built after management_actions/cash_bridge so the narrative can close
    # with a concrete "what should the manager do" decision paragraph and a
    # net-profit-to-cash sentence, instead of stopping at diagnosis.
    executive_summary = build_executive_summary(
        health_score, health_label, findings_sorted, opportunities_sorted,
        root_cause, business_impact, ccc, trend, benchmark,
        management_actions=management_actions, cash_bridge=cash_bridge,
        risk_ranking=risk_ranking, statements=statements,
    )
    scenarios = build_scenarios(statements)

    finding_registry = build_finding_registry(
        findings_sorted, gap_detection, root_cause, risk_ranking, business_impact,
        opportunities=opportunities_sorted, management_actions=management_actions,
    )
    gap_detection_for_report = finding_registry["gap_detection_deduplicated"]
    strategy_playbook = build_strategy_playbook(opportunities_sorted, scenarios)

    # ----- Narrative Engine (multi-scenario Ne oldu/Neden/Maliyet/Ne yapmalı) -----
    # Runs AFTER every input engine it reads from is available. Deliberately
    # separate from executive_summary_engine's top-1 narrative_story: this
    # produces one card PER independently-triggered scenario (margin
    # erosion, DSO risk, inventory bloat, cash runway...), not just the
    # single most severe finding.
    narrative_engine = build_narrative_engine(
        statements, trend, root_cause, business_impact, ccc, cash_bridge=cash_bridge,
        benchmark=benchmark, profit_quality=profit_quality,
        sales_intelligence=(data_hub or {}).get("analysis_sales"),
    )

    # New: DuPont 3 and 5-stage value driver tree decomposition
    dupont = build_dupont_analysis(statements)

    return {
        "engine_version": "2.0",
        "health_score": health_score,
        "health_label": health_label,
        "score_components": {
            "data_trust": round(data_component, 1),
            "liquidity": round(liquidity_points, 1),
            "leverage": round(leverage_points, 1),
            "profitability": round(profitability_points, 1),
            "efficiency_capital": round(efficiency_points, 1),
        },
        "derived_metrics": {
            "finance_cost_to_operating_profit_pct": None if finance_cost_to_op is None else finance_cost_to_op * 100,
            "interest_coverage_proxy": interest_coverage_proxy,
            "debt_to_assets_pct": None if debt_to_assets is None else debt_to_assets * 100,
            "equity_ratio_pct": None if equity_ratio is None else equity_ratio * 100,
            "cash_to_financial_debt_pct": None if cash_to_debt is None else cash_to_debt * 100,
            "receivables_to_sales_pct": None if receivables_to_sales is None else receivables_to_sales * 100,
            "other_income_to_pbt_pct": None if non_core_income_to_pbt is None else non_core_income_to_pbt * 100,
        },
        # Legacy / backward-compatible fields (existing frontend + tests rely on these).
        "findings": findings_sorted,
        "opportunities": opportunities_sorted,
        "actions": actions,
        "executive_summary": executive_summary["text"],
        "methodology_note": "Skor ve kurallar genel finansal eşiklere dayanır; resmi sektör benchmarkı değildir. Trend analizi çok dönemli veri, gerçek DSO/DPO/DIO ise açılış bakiyesi/subledger verisi gerektirir; bu motorlar mevcut verinin izin verdiği ölçüde çalışır ve sınırlarını açıkça belirtir.",
        # New: the 8 requested capabilities, each as its own explicit section.
        "root_cause_engine": root_cause,
        "business_impact_engine": business_impact,
        "executive_summary_engine": executive_summary,
        "risk_ranking_engine": risk_ranking,
        "opportunity_engine": {"opportunities": opportunities_sorted},
        "cash_conversion_cycle": ccc,
        "trend_analysis": trend,
        "benchmarking": benchmark,
        "cash_bridge_engine": cash_bridge,
        "profit_quality_engine": profit_quality,
        "management_actions": management_actions,
        "calculation_audit": calculation_audit,
        "scenario_engine": {"scenarios": scenarios},
        # Report-facing gap list: exact statement-level duplicates of an
        # existing Findings entry are folded out here (see finding_registry
        # for the fold-in record). Callers who need the raw, un-consolidated
        # output of build_gap_detection() (e.g. tests) call it directly.
        "gap_detection_engine": gap_detection_for_report,
        "operational_finance_engine": operational_finance,
        # New: single, de-duplicated, cross-engine finding list. This is the
        # canonical CFO-facing view; every other *_engine section above is
        # still returned for traceability/backward compatibility, but the
        # report layer should render from finding_registry.master_findings
        # instead of re-listing findings/gaps/risks separately.
        "finding_registry": finding_registry,
        # New: single, ranked, de-duplicated view of Opportunity Engine +
        # Scenario Lab (see strategy_playbook.py docstring for why these two
        # were showing the same six commercial levers twice). Report layer
        # should render from here instead of the separate "opportunities"
        # list and "scenario_engine.scenarios" list.
        "strategy_playbook": strategy_playbook,
        # New: multi-scenario Financial Storytelling Engine — see
        # narrative_engine.py module docstring for scope/limits.
        "narrative_engine": narrative_engine,
        # New: DuPont 3 and 5-stage value driver tree decomposition
        "dupont_analysis": dupont,
    }
