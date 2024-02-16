import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.quintoandar.com.br"]
    start_urls = [
        "https://www.quintoandar.com.br/alugar/imovel/florianopolis-sc-brasil"]

    def parse(self, response):
        all_text = response.css('main > section.sc-17znhs8-0.gbFAEp > div')

        valor = all_text.css('h3::text').getall()
        detalhes = all_text.css('h4::text').getall()

        for valor_, detalhes_ in zip(valor, detalhes):
            yield {
                'valor': valor_,
                'detalhes': detalhes_
            }
