import json
from pandas import DataFrame

data_list = []

with open('graphql.json') as f:
    data = json.load(f)

    assets = data['data']['assetsConnection']['assets']
    print(len(assets))
    for asset in assets:
        asset_id, headline, asset_about, modified, published = \
            asset['id'], asset['asset']['headlines']['headline'], \
            asset['asset']['about'], asset['dates']['modified'], \
            asset['dates']['published']
        published_url = 'https://theage.com.au/' + asset['urls']['published']['theage']['path']
        primary_tag = asset['tags']['primary']['displayName']
        secondary_tags = [t['displayName'] for t in asset['tags']['secondary']]
        data = [asset_id, headline, asset_about, published_url, modified, published, primary_tag, secondary_tags]
        data_list.append(data)
    # print(assets)

df = DataFrame(data_list, columns=['id', 'headline', 'about', 'url', 'modified_date',
                                   'published_date', 'primary_tag', 'secondary_tag'])
df.to_csv('df.csv')
print(df.shape)
