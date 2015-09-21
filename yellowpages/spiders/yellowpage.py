# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.http import Request
from lxml.html import fromstring
from scrapy.selector import Selector
from yellowpages.items import YellowpagesItem

search_terms = ['real estate companies']
locations = ['Cincinnati, OH']

class YellowpageSpider(scrapy.Spider):
    name = "yellowpage"
    allowed_domains = ["yellowpages.com"]

    # start_urls = (
    #     'http://www.yellowpages.com/',
    # )
    start_urls = ('http://www.yellowpages.com/search?search_terms={}&geo_location_terms={}'.format(search_terms[ctr],locations[ctr]) for ctr,search_term in enumerate(search_terms)
    )
    base_url = 'http://www.yellowpages.com'
    def parse(self, response):

        hxs = Selector(response)
        item = YellowpagesItem()
        item['url'] = response.url
        companies = hxs.xpath('//div[@class="info"]')
        for company in companies:
            company_name = company.xpath('.//a[@itemprop="name"]/text()').extract()
            if company_name:
                company_name = company_name[0]
                item['company_name'] = company_name

            street = company.xpath('.//span[@itemprop="streetAddress"]/text()').extract()
            if street:
                street = street[0]
                item['street'] = street
            locality = company.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
            if locality:
                locality = locality[0]
                item['locality'] = locality
            region = company.xpath('.//span[@itemprop="addressRegion"]/text()').extract()
            if region:
                region = region[0]
                item['region'] = region
            postal_code = company.xpath('.//span[@itemprop="postalCode"]/text()').extract()
            if postal_code:
                postal_code = postal_code[0]
                item['postal_code'] = postal_code
            telephone = company.xpath('.//div[@itemprop="telephone"]/text()').extract()
            if telephone:
                telephone = telephone[0]
                item['telephone'] = telephone
            website = company.xpath('.//a[contains(text(),"Website")]/@href').extract()
            if website:
                website = website[0]
                item['website'] = website

            print item

            yield item


        # self.parse_page(response)
        # hxs = Selector(response)

        # for search_term in search_terms:
        #     search_terms = urllib.quote_plus(search_term)
        #     location = urllib.quote_plus()
        #     url = 'http://www.yellowpages.com/search?search_terms={}&geo_location_terms={}'.format(search_terms,location)
            # yield Request(url,self.parse_page,dont_filter=True)
        #pagination
        next_link = hxs.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_link:
            next_link = next_link[0]
            print next_link
            # yield Request(url,self.parse_page,dont_filter=True)
            yield Request(self.base_url+next_link,self.parse,dont_filter=True)

    def parse_page(self, response):
        hxs = Selector(response)
        item = YellowpagesItem()
        item['url'] = response.url
        companies = hxs.xpath('//div[@class="info"]')
        for company in companies:
            company_name = company.xpath('.//a[@itemprop="name"]/text()').extract()
            if company_name:
                company_name = company_name[0]
                item['company_name'] = company_name

            street = company.xpath('.//span[@itemprop="streetAddress"]/text()').extract()
            if street:
                street = street[0]
                item['street'] = street
            locality = company.xpath('.//span[@itemprop="addressLocality"]/text()').extract()
            if locality:
                locality = locality[0]
                item['locality'] = locality
            region = company.xpath('.//span[@itemprop="addressRegion"]/text()').extract()
            if region:
                region = region[0]
                item['region'] = region
            postal_code = company.xpath('.//span[@itemprop="postalCode"]/text()').extract()
            if postal_code:
                postal_code = postal_code[0]
                item['postal_code'] = postal_code
            telephone = company.xpath('.//div[@itemprop="telephone"]/text()').extract()
            if telephone:
                telephone = telephone[0]
                item['telephone'] = telephone
            website = company.xpath('.//a[contains(text(),"Website")]/@href').extract()
            if website:
                website = website[0]
                item['website'] = website

            print item

            yield item





        # print response.url
        # # html = fromstring(response.body)
        # with open('check.html','wb') as mf:
        #     mf.write(response.body)
