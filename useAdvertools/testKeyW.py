import advertools as adv

products = ['kapunga rice', 'ecommerce', 'inventory']
words = ['kenya', 'discount', 'cheap', 'management', 'system']

kw_df = adv.kw_generate(products, words)
print(kw_df)
