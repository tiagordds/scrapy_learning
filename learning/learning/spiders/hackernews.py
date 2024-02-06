import scrapy


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        all_title = response.css('span.titleline')
        sub_line = response.css('span.subline')

        for title_line in all_title:
            title = title_line.css('a::text').extract()

            yield {
                'title': title
            }

        for post_information in sub_line:
            points = post_information.css('span.score::text').extract()
            author = post_information.css('a.hnuser::text').extract()
            time = post_information.css('span.age::attr(title)').extract()
            yield {
                'points': points,
                'author': author,
                'time': time,
            }
