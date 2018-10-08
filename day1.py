#-*-coding:utf-8 -*-
import urllib.request
url = 'https://tieba.baidu.com/p/4705665446?fr=ala0&pstaala=1&tpl=5&fid=721865&isgod=0&red_tag=1942025657'#只看楼主

def get_img(url):
    page = urllib.request.urlopen(url)
    html = page.read()

    r_img = r'src="(.*?.jpg)" pic'
    imgre = re.compile(r_img)
    img_list = re.findall(r_img,html.decode('utf-8'))

    i = 1
    for img_url in img_list:
        urllib.request.urlretrieve(img_url ,'%i.jpg' %i)
        i += 1
    get_img(url)
