import advertools as adv

## ********** SEM (Search Engine Marketing)*************

# USING KEYWORD FUNCTIONALITY FROM ADVERTOOLS
"""
products = ['kapunga rice', 'ecommerce', 'inventory']
words = ['kenya', 'discount', 'cheap', 'management', 'system']

# negative exact keywords
print(adv.kw_neg_exact(products))

# key words phrase
print(adv.kw_phrase(products))
# kw_df = adv.kw_generate(products, words)
# print(kw_df)





# CREATE ADS use template

products = ['Rice', 'Dal', 'Wheat','Millet']
# products = []
ads = adv.ad_create(template='Buy kapunga {} in our new store',
            replacements=products,
            max_len=50,
            fallback='items')

print(ads)


desc_text = "Get the latest gadget online. The GX12 model comes with 13 things that do a lot of good stuff for your health. Start shopping now."
len(desc_text)  # 130
adv.ad_from_string(desc_text)  # default values (Google text ads)
adv.ad_from_string(desc_text, [125, 25, 30])  # Facebook feed ads


"""

# adv.ad_from_string()

# ********** SEO(Search Engine Optimization) ****************

url_list = ['https://smartmgr.com/',
            'https://www.soft-titan.com',
            'https://pypil.com/']


insights = adv.crawl(url_list,
          output_file='example_crawl_1.jl',
          follow_links=False)

print(insights)
















