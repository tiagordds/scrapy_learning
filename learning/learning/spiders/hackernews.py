import scrapy
# from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [
        "https://news.ycombinator.com/news"
    ]

    def parse(self, response):
        all_body = response.css('tr.athing')
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for info in all_body:
            subtext = info.xpath('following-sibling::tr')[0]
            info_row = info.xpath('following-sibling::tr')[0]
            score = info_row.css('span.score::text').get()
            score_list = []

            if score is not None:
                for number in score:
                    if number in numbers:
                        score_list.append(number)
                        edited_score_map = map(str, score_list)
                        edited_score = ''.join(edited_score_map)
                        edited_score = int(edited_score)
            else:
                edited_score = score

            yield {
                'title': info.css('span.titleline a::text').get(),
                'score': edited_score,
                'author': subtext.css('span > a.hnuser::text').get(),
                'hour': subtext.css('span > span.age::attr(title)').get(),
            }
