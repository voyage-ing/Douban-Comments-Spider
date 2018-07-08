import re
import os
import urllib
import random
import urllib.parse
import urllib.request
from lxml import etree

subFilmURL = 'https://www.douban.com/search?cat=1002&q='
subBookURL = 'https://www.douban.com/search?cat=1001&q='
subMusicURL = 'https://www.douban.com/search?cat=1003&q='

class Douban_id():
    '''
    get a Douban id according to the film name,music name,or book name that you provid
    '''
    def __init__(self,name,sort='movie'):
        '''
        :param name: film name,music name,or book name
        :param sort: sort attr is optional just from ['movie','book','music']
        '''
        self.name = name
        self.sort = sort
        self.url_1 = subFilmURL
        self.url_2 = subBookURL
        self.url_3 = subMusicURL

    def getID(self):

        if self.sort == 'book':
            url = self.url_2 + urllib.parse.quote(self.name)
        elif self.sort == 'movie':
            url = self.url_1 + urllib.parse.quote(self.name)
        elif self.sort == 'music':
            url = self.url_3 + urllib.parse.quote(self.name)
        else:
            print("error: wrong option about catagory's name.the right one is from 'movie'or'music'or'book'")
            os._exit()


        headers = [{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"},
                   {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"},]
        header = random.choice(headers)

        request = urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)

        html = response.read().decode('utf-8')
        selector = etree.HTML(html)
        a_tag =  selector.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/h3/a/@onclick')[0]

        #print(a_tag)
        partten = re.compile(r'sid: (\d+)',re.S)

        filmID = partten.findall(a_tag)[0]

        return filmID




