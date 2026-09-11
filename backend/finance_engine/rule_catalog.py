RULE_CATALOG={
 'L001':{'category':'Borçluluk','metric':'finance_cost_to_operating_profit','threshold':{'critical':0.60,'high':0.40,'medium':0.25},'direction':'lower_is_better','confidence':'high'},
 'L002':{'category':'Borçluluk','metric':'debt_to_equity','threshold':{'critical':5.0,'high':3.0,'medium':2.0},'direction':'lower_is_better','confidence':'high'},
 'Q001':{'category':'Likidite','metric':'current_ratio','threshold':{'critical':1.0,'medium':1.2},'direction':'higher_is_better','confidence':'high'},
 'W001':{'category':'İşletme Sermayesi','metric':'receivables_to_sales','threshold':{'high':0.50},'direction':'lower_is_better','confidence':'medium'},
 'D004':{'category':'Borçluluk','metric':'debt_to_assets','threshold':{'critical':0.70,'high':0.50},'direction':'lower_is_better','confidence':'high'},
 'D006':{'category':'Borçluluk','metric':'interest_coverage','threshold':{'critical':1.5,'high':3.0},'direction':'higher_is_better','confidence':'high'},
}

def get_rule_catalog(): return RULE_CATALOG
