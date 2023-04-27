import advertools as adv
'''

## ********** SEM (Search Engine Marketing)*************

# USING KEYWORD FUNCTIONALITY FROM ADVERTOOLS
products = ['kapunga rice', 'ecommerce', 'inventory']
words = ['kenya', 'discount', 'cheap', 'management', 'system']

# negative exact keywords
print(adv.kw_neg_exact(products))

# key words phrase
print(adv.kw_phrase(products))
kw_df = adv.kw_generate(products, words)
print(kw_df)

'''


"""
# CREATE ADS use template
products = ['Rice', 'Dal', 'Wheat','Millet']
ads = adv.ad_create(template='Buy kapunga {} in our new store',
            replacements=products,
            max_len=50,
            fallback='items')

print(ads)

desc_text = "Get the latest gadget online. The GX12 model comes with 13 things that do a lot of good stuff for your health. Start shopping now."
len(desc_text)  # 130
print(adv.ad_from_string(desc_text))  # default values (Google text ads)
print(adv.ad_from_string(desc_text, [125, 25, 30]))  # Facebook feed ads
# adv.ad_from_string()


"""


# ********** SEO(Search Engine Optimization) ****************


# get_robots = adv.robotstxt_test('https://www.salesforce.com/robots.txt',
#                                 user_agents=['*'],
#                 urls=['/']) 

# print(get_robots)
# get_robots = adv.robotstxt_to_df('https://www.salesforce.com/robots.txt')
# print(get_robots[get_robots['directive'] == 'Sitemap'])

# url_list = ['https://smartmgr.com/',
#             'https://www.soft-titan.com',
#             'https://pypil.com/']


# insights = adv.crawl(url_list,
#           output_file='example_crawl_1.jl',
#           follow_links=False)

# print(insights)

# '''

# '''

# robots_urls = ['https://www.google.com/robots.txt',
#                'https://twitter.com/robots.txt',
#                'https://facebook.com/robots.txt']

# googtwfb = adv.robotstxt_to_df(robots_urls)

# # How many lines does each robots file have?
# print(googtwfb.groupby('robotstxt_url')['directive'].count())

# # Display the first five rows of each of the robots files:
# print(googtwfb.groupby('robotstxt_url').head())


sitemap_urls = [
    "https://www.google.com/sitemap.xml",
]
sitemaps = adv.sitemap_to_df(sitemap_urls[0])
print(sitemaps)

# vegetable_emoji = adv.emoji_search('vegetable')
# vegetable_emoji.head()



# '''
