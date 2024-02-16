import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [
        "https://news.ycombinator.com",
    ]

    def parse(self, response):
        all_body = response.css('tr.athing')

        for info in all_body:
            subtext = info.xpath('following-sibling::tr')[0]
            yield {
                'title': info.css('span.titleline a::text').get(),
                'score': subtext.css('span.score::text').get(),
                'author': subtext.css('span > a.hnuser::text').get(),
                'hour': subtext.css('span > span.age::attr(title)').get(),
            }
