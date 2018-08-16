#-*- coding: utf-8 -*-

# BeautifulSoup 모듈을 import 합니다. 
from bs4 import BeautifulSoup
# requests는 페이지를 요청한 응답을 받을때 사용합니다.
import urllib.request
from test.support import temp_cwd

'''
url="http://www.op.gg/champion/gnar/statistics/top/matchup"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'html.parser')
# div 태그의 class 명이 'test'인 항목만 가져와서 출력해라
elements = soup.findAll('tr', {'class':'Row'})
for i in elements:
   print (i)
'''
import time


from selenium import webdriver


driver = webdriver.Firefox(executable_path =r"/Library/Frameworks/Python.framework/Versions/3.5/bin/geckodriver")
targetURL ='http://www.op.gg/champion/gnar/statistics/top/matchup'
driver.get(targetURL)



#chromedriver = "/Users/adam/Downloads/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver

#driver = webdriver.Chrome()
#driver.get("http://www.op.gg/champion/gnar/statistics/top/matchup")

'''
content = driver.find_element_by_class_name('Cell Button')
time.sleep(10)
content.click()
print(content)
'''

#driver.execute_script("$.OP.GG.champion.Counter.Change(ChampionMatchUpContent.RealContent, 150, 86, 'TOP');")
#time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#prodList = soup.find_all("div", {"class": "ChampionName"})

for child in soup.find_all("div", {"class":"RealContent"}):
    blue_win = child.find("div", {"class":"Champion Blue"}).find("span", {"class":"tip __tipped__"})
    #print(blue_win)
    red_win = child.find("div", {"class":"Champion Red"}).find("span", {"class":"tip __tipped__"})
    #print(red_win)


bluesolokill = ""
redsolokill = ""    
for solokillrate in soup.find_all("table", {"class":"CounterChampionStatsTable"}) :
    temp = solokillrate.find("tbody", {"class":"Content"}).find("tr", {"class":"Row"}).children
    #Content에 들어있는 첫번재 Row의 children중에서 인덱스 1 일때 왼쪽, 인덱스 1일때 오른쪽의 solokill rate가 들어있음.
    for index, child in enumerate(temp):
        if index == 1:
            blue_solokill = child
            #print (blue_solokill)
        elif index == 5:
            red_solokill = child
            #print (red_solokill)
    
            
blue_win_str = str(blue_win)
blue_win_str = blue_win_str.replace('<span class="tip __tipped__">', '')
blue_win_str = blue_win_str.replace('</span>', '')
red_win_str = str(red_win)
red_win_str = red_win_str.replace('<span class="tip __tipped__">', '')
red_win_str = red_win_str.replace('</span>', '')
print('블루 승률', blue_win_str)
print('레드 승률', red_win_str)

blue_solokill_str = str(blue_solokill)
blue_solokill_str = blue_solokill_str.replace('<td class="Cell Value Left ">', '')
blue_solokill_str = blue_solokill_str.replace('<td class="Cell Value Left Fill">', '')
blue_solokill_str = blue_solokill_str.replace('<span class="Change">', '')
blue_solokill_str = blue_solokill_str.replace('<i class="__spSite __spSite-', '')
blue_solokill_str = blue_solokill_str.replace('"></i>', '')
blue_solokill_str = blue_solokill_str.replace('\t', '')
blue_solokill_str = blue_solokill_str.replace('\n', '')
print('블루 솔로킬 확률', blue_solokill_str[:5])

red_solokill_str = str(red_solokill)
red_solokill_str = red_solokill_str.replace('<td class="Cell Value Right ">', '')
red_solokill_str = red_solokill_str.replace('<td class="Cell Value Right Fill">', '')
red_solokill_str = red_solokill_str.replace('<span class="Change">', '')
red_solokill_str = red_solokill_str.replace('<i class="__spSite __spSite-', '')
red_solokill_str = red_solokill_str.replace('"></i>', '')
red_solokill_str = red_solokill_str.replace('\t', '')
red_solokill_str = red_solokill_str.replace('\n', '')
print('레드 솔로킬 확률', red_solokill_str[:5])

driver.quit()


'''
url = "http://www.op.gg/champion/" + 'gnar' + "/statistics/top/matchup"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'html.parser')
'''
'''
winratio = soup.findAll('td', {'class':'Cell WinRatio'})
enemyname = soup.findAll('img', {'class' :'Image'})
    
    
winratiostr = str(winratio)

winratiostr = winratiostr.replace('</td>, <td class="Cell WinRatio">', '')
winratiostr = winratiostr.replace('\t', '')

enemynamestr = str(enemyname)




#index위치를 찾아서 그 앞으로 다 잘라냄 (해당 문자열은 잘리지 않음)
index = enemynamestr.find('<img class="Image" src="//sk2.op.gg/images/lol/champion/Kennen.png">')
enemynamestr = enemynamestr[index:]

enemynamestr = enemynamestr.replace('</img>, <img class="Image" src="//sk2.op.gg/images/lol/champion/', '')
enemynamestr = enemynamestr.replace('png">', '')
enemynamestr = enemynamestr.replace('\t', '')

print (enemynamestr)
'''
    