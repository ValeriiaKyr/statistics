import scrapy
from scrapy.http import Response


class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["www.pracuj.pl"]
    start_urls = ["https://www.pracuj.pl/praca/python;kw?utm_source=google&utm_medium=cpc&utm_campaign=dsa_miasta_an&campaignid=20387307111&adgroupid=157252921568&gad_source=1&gclid=CjwKCAiAxKy5BhBbEiwAYiW--xCq-CDIBRyZwDEC0tZeGD6dr2OlbSgwcJd2BAw3hvwtve20L1uBnBoCZzQQAvD_BwE"]

    def parse(self, response: Response, **kwargs) -> dict:
        pass
