import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        all_body = response.xpath(
            "//table[@id='hnmain']")

        title = all_body.css("span.titleline a::text").getall()
        score = all_body.css("span.score::text").getall()
        hour = all_body.css("span.age::attr(title)").getall()
        author = all_body.css("a.hnuser::text").getall()

        for title_, points_, hour_, author_ in zip(title, score, hour, author):

            yield {
                'title': title_,
                'points': points_,
                'hour': hour_,
                'author': author_,
            }
