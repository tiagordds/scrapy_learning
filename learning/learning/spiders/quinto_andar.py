import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.quintoandar.com.br"]
    start_urls = [
        "https://www.quintoandar.com.br/alugar/imovel/florianopolis-sc-brasil"]

    def parse(self, response):
        rows = response.css('.gnxvcs')

        price = rows.css('h3::text').get()

        for i, row in enumerate(rows):
            price_ = price[i]
            yield {
                'preco': price_,
                'detalhes': row.css('h4::text').get(),
            }
