import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.quintoandar.com.br"]
    start_urls = [
        "https://www.quintoandar.com.br/alugar/imovel/florianopolis-sc-brasil"]

    def parse(self, response):
        rows = response.css('.gnxvcs')

        for row in rows:
            yield {
                'detalhes': row.css('h4::text').getall(),
            }
