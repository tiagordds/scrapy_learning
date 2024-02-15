import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.quintoandar.com.br"]
    start_urls = [
        "https://www.quintoandar.com.br/alugar/imovel/florianopolis-sc-brasil"]

    def parse(self, response):
        all_text = response.css('main > section.sc-17znhs8-0.gbFAEp > div')

        for info in all_text:
            yield {
                # 'valor': info.css('h3::text').get(),
                'detalhes': info.css('h4::text').getall(),
            }

# __next > div > main > section.sc-17znhs8-0.gbFAEp > div
