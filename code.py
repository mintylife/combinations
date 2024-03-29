cols = [
      'age_cols'
    , 'trs_cols'
    , 'amt_cols'
    , 'clients_cols'
    , 'suppliers_cols'
    , 'div_cols'
    , 'label_cols'
    , 'tov_cols'
    , 'serv_cols'
    , 'in_cols'
    , 'out_cols'
    , 'oborot_cols'
    , 'prop_cols'
    , 'with_cols'
    , 'median_cols'
    , 'divers_cols'
    , 'temp_cols'
    , 'vkl_cols'
]

keywords = [
      'age' 
    , 'trs' 
    , 'amt' 
    , 'clients' 
    , 'suppliers'
    , '/' 
    , 'label' 
    , 'Товары'
    , 'Услуги' 
    , 'IN' 
    , 'OUT' 
    , 'oborot' 
    , 'prop'
    , 'with' 
    , 'median'
    , 'divers' 
    , 'temp' 
    , 'Вклады и аренда' 
]

print('hello world!')

groups = {}
for new_col, keyword in zip(cols, keywords):
    groups[new_col]  = [col for col in train_df.columns if keyword in col]
groups

print('glad to see you here!')