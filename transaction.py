import pandas as pd
fact_payment = pd.read_csv('fact_primary.csv')
product = pd.read_csv('product.csv')
product = product.rename(columns={'id': 'dim_productid'})
new_merge = fact_payment.merge(product, on='dim_productid', how='left')
new_group = new_merge.groupby(by='product_name', dropna=False)['tx_id'].count()
transaction_count = pd.DataFrame(new_group)
transaction_sort = transaction_count['tx_id'].sort_values(ascending=False)
final = pd.DataFrame(transaction_sort)