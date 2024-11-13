import time

import scrapy
from scrapy import Selector
from scrapy.http import Response
from selenium import webdriver

class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["www.pracuj.pl"]
    start_urls = ["https://www.pracuj.pl/praca/python;kw?utm_source=google&utm_medium=cpc&utm_campaign=dsa_miasta_an&campaignid=20387307111&adgroupid=157252921568&gad_source=1&gclid=CjwKCAiAxKy5BhBbEiwAYiW--xCq-CDIBRyZwDEC0tZeGD6dr2OlbSgwcJd2BAw3hvwtve20L1uBnBoCZzQQAvD_BwE"]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()

    def close(self, reason: str) -> None:
        self.driver.close()

    def parse(self, response: Response, **kwargs) -> dict:
        all_links = response.css("div.listing_ohw4t83 div.type--positioned div.tiles_cobg3mp a.tiles_cnb3rfy::attr(href)").getall()

        for job in all_links:
            detail_url = response.urljoin(job)
            info = self._parse_additional_info(detail_url)
            yield {
                "title": info["title"],
                "company": info["company"],
                "expected": info["expected"],
                "link": info["link"],
                "project": info["project"],
                "level": info["level"],
                "work mode": info["work_mode"],
                "salary": info["salary"],
                "salary_for": info["salary_for"],
                "city": info["city"],
                "ukrainian_people": info["ukrainian_people"],
            }


    def _parse_additional_info(
            self,
            detail_url,
    ) -> dict:
        self.driver.get(detail_url)
        time.sleep(3)
        detail_page = self.driver.page_source
        detail_response = Selector(text=detail_page)
        salary = detail_response.css(
                "div[data-test='section-salary'] div.s1u58mkm div.s1wj9oyw div.s1n75vtn::text"
            ).get()
        ukrainian_people = detail_response.css(
            "li[data-scroll-id='attribute-primary-ukrainian-friendly'] div.tchzayo div.t1g3wgsd::text"
        ).get()

        salary_for = detail_response.css(
            "div.c1prh5n1 div[data-test='section-salary'] div.sxxv7b6::text"
        ).get()
        city = detail_response.css(
                "li[data-test='sections-benefit-workplaces'] div.tchzayo a.wv9o0p1::text"
            ).get()
        if city:
            city = city.split(", ")[-1]
        if salary:
            salary = salary.replace('\xa0', '')

        if ukrainian_people:
            ukrainian_people = True
        else:
            ukrainian_people = False

        info = {
            "title": detail_response.css(
                "h1.ow09k7q::text"
            ).get(),
            "company": detail_response.css(
                "h2.cp9trhu::text"
            ).get(),
            "expected": [li.css("::text").get() for li in detail_response.css("div[data-test='section-technologies-expected'] ul.cku9rky li.catru5k")],
            "optional knowledge": [li.css("::text").get() for li in detail_response.css("ul.cku9rky li.catru5k")],
            "link": detail_url,
            "project": detail_response.css("div.cu3huna ul.c1qnwb5g li.t6laip8::text").getall(),
            "level": detail_response.css(
                "li[data-test='sections-benefit-employment-type-name'] div.tchzayo div.t1g3wgsd::text"
            ).get(),
            "work_mode": detail_response.css(
                "li[data-scroll-id='work-modes'] div.tchzayo div.t1g3wgsd::text"
            ).get(),
            # "salary": detail_response.css(
            #     "div[data-test='section-salary'] div.s1u58mkm div.s1wj9oyw div.s1n75vtn::text"
            # ).get().replace('\xa0', ''),
            "salary": salary,
            "salary_for": salary_for,
            # "city": detail_response.css(
            #     "li[data-test='sections-benefit-workplaces'] div.tchzayo a.wv9o0p1::text"
            # ).get().split(", ")[-1],
            "city": city,
            # "ukrainian_people": detail_response.css(
            #     "li[data-scroll-id='attribute-primary-ukrainian-friendly'] div.tchzayo div.t1g3wgsd::text"
            # ).get(),
            "ukrainian_people": ukrainian_people,

        }
        return info

