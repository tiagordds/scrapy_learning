import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        all_body = response.xpath(
            "//table[@id='hnmain']")

        body = (all_body.css("span.titleline a::text").getall(),
                all_body.css("span.score::text").getall(),
                all_body.css("span.age::attr(title)").getall(),
                all_body.css("a.hnuser::text").getall())

        print('*' * 100)
        title = (body[0])
        score = (body[1])
        hour = (body[2])
        author = (body[3])

        for title_, points_, hour_, author_ in zip(title, score, hour, author):
            post_info = []
            post_info.append(title_)
            post_info.append(author_)
            post_info.append(points_)
            post_info.append(hour_)
            yield {
                'Post Info': post_info
            }
