import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        all_page = response.css('#hnmain')
        x = 0
        while x < 31:

            for post_info in all_page:
                all_title = post_info.css("span.titleline")
                title = all_title.css("a::text")[x].get()
                all_info = post_info.css("span.subline")
                points = all_info.css("span.score::text")[x].get()
                yield {
                    'title': title,
                    'points': points
                }
                x += 1
