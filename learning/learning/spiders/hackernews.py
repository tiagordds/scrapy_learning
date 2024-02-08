import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        body = response.xpath("//td")

        for tr in body.xpath(".//*[contains(concat(' ', normalize-space(@class), ' '), ' titleline ')]//text()"):
            title = tr.getall()
            yield {
                "title": title
            }
