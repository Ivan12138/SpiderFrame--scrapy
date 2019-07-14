# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # 下面为了拼接链接实现翻页做准备
    offset = 1
    baseURL = "https://careers.tencent.com/search.html?index="
    start_urls = [baseURL+str(offset)]

    def parse(self, response):

        contents = response.xpath("//div[@class ='recruit-list']/a")
        for each in contents:
            item = TencentItem()
            positionName=each.xpath("/h4/text()").extract()
            organization = each.xpath("/p/span[1]/text()").extract()
            positionLocation = each.xpath("/p/span[2]/text()").extract()
            positionType = each.xpath("/p/span[3]/text()").extract()
            releaseTime = each.xpath("/p/span[4]/text()").extract()
            positionBrief = each.xpath("/p[2]/text()").extract()

            item['positionName'] = positionName[0]
            item['organization'] = organization[0]
            item['positionLocation'] = positionLocation[0]
            item['positionType'] = positionType[0]
            item['releaseTime'] = releaseTime[0]
            item['positionBrief'] = positionBrief[0]
            yield item
        # # 第一种写法：拼接url。使用场景，页面没有可以点击的链接，只能通过拼接url才能获得响应
        if self.offset<380:
            self.offset += 1
            url = self.baseURL + str(self.offset)
            # 返回请求
            yield scrapy.Request(url,callback=self.parse)

        #第二种方法：直接从response获取需要爬取链接，并发送请求，直至全部取完
        # if len(response.xpath("//li[@class='next disabled']"))==0:
        #     url = response.xpath("//li[@class='next']/@href").extract()[0]
        #     yield scrapy.Request("https://careers.tencent.com"+url,callback=self.parse)
