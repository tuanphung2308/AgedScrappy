import scrapy
import json
import pandas as pd
from pandas import DataFrame

class SportSpider(scrapy.Spider):
    name = "sport"
    start_urls = []
    df_cleaned_content = []

    with open('/Users/tuanminh/PycharmProjects/whatshouldicallthis/graphql.json') as f:
        data = json.load(f)

        assets = data['data']['assetsConnection']['assets']
        print(len(assets))
        for asset in assets:
            published_url = 'https://theage.com.au/' + asset['urls']['published']['theage']['path']
            start_urls.append(published_url)

    def parse(self, response):
        a_body = response.xpath('//*[@id="content"]/div/article')
        p_tag_list = a_body.css("section > div p::text").getall()
        for p_text in p_tag_list:
            cleaned_text_list = []
            if p_text == 'Replay':
                continue
            if p_text == ' ':
                continue
            if p_text == 'Sports news, results and expert commentary delivered straight to your inbox. Sign up to the ':
                continue
            if 'weekday newsletter' in p_text:
                continue
            print(p_text)
            cleaned_text_list.append(p_text)
        self.df_cleaned_content.append("\n ".join(p_text))

    def closed(self, reason):
        # will be called when the crawler process ends
        # any code
        # do something with collected data
        df = pd.read_csv('df.csv')
        df['content'] = self.df_cleaned_content
        print(df)