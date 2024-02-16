import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.quintoandar.com.br"]
    start_urls = [
        "https://www.quintoandar.com.br/alugar/imovel/florianopolis-sc-brasil"]

    def parse(self, response):
        body = response.css('main > section.sc-17znhs8-0.gbFAEp > div')

        for info in body:
            yield {
                'detalhes': info.css('h4::text').getall()
            }
