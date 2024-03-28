import scrapy

class Cegef(scrapy.Spider):
    name = 'cegef'
    allowed_domains = ['cegef.com']
    start_urls = ['https://cegef.com/course_cat/cao/', 'https://cegef.com/course_cat/bureau/', 'https://cegef.com/course_cat/pao/', 'https://cegef.com/course_cat/bim/', 'https://cegef.com/course_cat/manage/', 'https://cegef.com/course_cat/rh_gpec/', 'https://cegef.com/course_cat/compta/', 'https://cegef.com/course_cat/com/']

    def parse(self, response):
        formations = self.extract_formations(response)
        yield from formations

        last_page_number = int(response.css('.pagination li:last-child a::text').get())

        for page_number in range(2, last_page_number + 1):
            next_page_url = f'{response.url}page/{page_number}/'
            yield scrapy.Request(next_page_url, callback=self.parse)

    def extract_formations(self, response):
        formations = response.css('.details')
        for formation in formations:
            nom = formation.css('h3 a::text').get()
            description = formation.css('p::text').get()
            yield {
                'nom': nom.strip() if nom else None,
                'description': description.strip() if description else None
            }