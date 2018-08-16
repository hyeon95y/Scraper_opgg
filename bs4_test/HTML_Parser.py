'''
Created on 2016. 11. 11.

@author: HyeonWoo
'''
#-*- coding: utf-8 -*-

import csv
import CSV_ReaderWriter as userCsv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

how_many_champs = 136
#여기서 먼저 선언함으로써 뒤에 나오는 같은 코드는 값 할당의 역할만 하고, 이제 얘가 계속 호출된다. 
champ_checked = []

def write_csv_winrate_and_pickrate(champ_data,  \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate):
    print('hey!')
    
    
    #이 아래로는 csv파일 작성 
    now = time.localtime()
    
    #01시 01분과 같은 문자열 문제 해결하기
    filename = 'champ_data_csv' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_champ_data(champ_data, filename)
    
    filename = 'counterpick_data_top_matchup_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_counterpick_data(counterpick_data_top_matchup_rate, filename)
    filename = 'counterpick_data_jungle_matchup_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_counterpick_data(counterpick_data_jungle_matchup_rate, filename)
    filename = 'counterpick_data_mid_matchup_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_counterpick_data(counterpick_data_mid_matchup_rate, filename)
    filename = 'counterpick_data_adc_matchup_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_counterpick_data(counterpick_data_adc_matchup_rate, filename)
    filename = 'counterpick_data_sup_matchup_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    userCsv.write_csv_counterpick_data(counterpick_data_sup_matchup_rate, filename)




def write_csv_winrate_and_solokillrate(lane, counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation):
    #이 아래로는 csv파일 작성 
    now = time.localtime()
    #01시 01분과 같은 문자열 문제 해결하기 
    if lane =='top' :
        filename = 'counterpick_data_top_win_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_win_rate, filename)
        filename = 'counterpick_data_top_solokill_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_solokill_rate, filename)
        filename = 'counterpick_data_top_cs_amount' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_cs_amount, filename)
        filename = 'counterpick_data_top_destroy_first_turret' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_destroy_first_turret, filename)
        filename = 'counterpick_data_top_total_deal' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_total_deal, filename)
        filename = 'counterpick_data_top_kill_participation' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_kill_participation, filename)
    if lane =='jungle' :
        filename = 'counterpick_data_jungle_win_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_win_rate, filename)
        filename = 'counterpick_data_jungle_solokill_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_solokill_rate, filename)
        filename = 'counterpick_data_jungle_cs_amount' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_cs_amount, filename)
        filename = 'counterpick_data_jungle_destroy_first_turret' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_destroy_first_turret, filename)
        filename = 'counterpick_data_jungle_total_deal' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_total_deal, filename)
        filename = 'counterpick_data_jungle_kill_participation' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_kill_participation, filename)
    if lane =='mid' :
        filename = 'counterpick_data_mid_win_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_win_rate, filename)
        filename = 'counterpick_data_mid_solokill_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_solokill_rate, filename)
        filename = 'counterpick_data_mid_cs_amount' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_cs_amount, filename)
        filename = 'counterpick_data_mid_destroy_first_turret' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_destroy_first_turret, filename)
        filename = 'counterpick_data_mid_total_deal' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_total_deal, filename)
        filename = 'counterpick_data_mid_kill_participation' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_kill_participation, filename)
    if lane =='adc' :
        filename = 'counterpick_data_adc_win_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_win_rate, filename)
        filename = 'counterpick_data_adc_solokill_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_solokill_rate, filename)
        filename = 'counterpick_data_adc_cs_amount' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_cs_amount, filename)
        filename = 'counterpick_data_adc_destroy_first_turret' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_destroy_first_turret, filename)
        filename = 'counterpick_data_adc_total_deal' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_total_deal, filename)
        filename = 'counterpick_data_adc_kill_participation' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_kill_participation, filename)
    if lane =='sup' :
        filename = 'counterpick_data_sup_win_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_win_rate, filename)
        filename = 'counterpick_data_sup_solokill_rate' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_solokill_rate, filename)
        filename = 'counterpick_data_sup_cs_amount' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_cs_amount, filename)
        filename = 'counterpick_data_sup_destroy_first_turret' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_destroy_first_turret, filename)
        filename = 'counterpick_data_sup_total_deal' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_total_deal, filename)
        filename = 'counterpick_data_sup_kill_participation' + '_' + str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
        userCsv.write_csv_counterpick_data(counterpick_data_kill_participation, filename)

#파싱알고리즘은 여기에 따로 떼서 관리 
def parsing_algorithm_for_winrate_and_pickrate(lane_name, soup, i, champ_data, champ_number_data,  \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate):
    print('parsing')
    #find_line_available에서 try로 감싸고 있기는 한데, 그게 페이지가 떴나 안떴나만 확인할수 있지 페이지가 떴다고 해서
    #데이터가 존재한다는 소리는 아님. (server error라는 페이지가 뜬다) 그래서 페이지는 떴지만 원하는 코드로 없을때
    #try exception으로 챔프 데이터가 없음을 알려줘야함. 근데 여기서 exception이 뜨면 밖에서도 exception으로 뜨는지? 잘 모르겠음. 테스트해볼것
    
    #여기서 파싱하고 데이터 저장하기 전에 모든 데이터를 0으로 초기화시켜놓아야함(라인가능,픽률, 승률) 
    
    try :
        lane = ['', '', '', '', '']
        
        lane_index = 0
        for child in soup.find("div", {"class":"ChampionRole"}).find_all("li", {"class":"Item"}):
            data = ['', '']
            ratio = ''
            
            lane[lane_index] = child.find("div", {"class" : "Role"}).find("div", {"class" : "Label"})
            lane_str = str(lane[lane_index])
            lane_str = lane_str.replace('<div class="Label">', '').replace('</div>', '').replace('\n', '')
            lane_index = lane_index + 1
            print(lane_str)
            
            ratio = child.find("div", {"class" : "Role"}).find("div", {"class" : "Value"})
            ratio_str = str(ratio)
            ratio_str = ratio_str.replace('<div class="Value">', '').replace('</div>', '').replace('\n', '').replace('%', '')
            print(ratio_str)
            
            index = 0
            for child2 in child.find_all("span", {"class" : "Value tip __tipped__"}) :
                data[index] = str(child2)
                data[index] = data[index].replace('<span class="Value tip __tipped__">', '').replace('<small>','').replace('</small>', '').replace('</span>', '')
                data[index] = data[index].replace('\t', '').replace('(', '').replace(')', '')
                space = data[index].find('위')
                data[index] = data[index][space:]
                data[index] = data[index].replace('위', '').replace('\n', '').replace('%', '')
                index = index+1
            print(data[0])
            print(data[1])
            
            #csv 는 라인 - 픽률 - 승률 순
            #파싱은 라인 - 승률 - 픽률 순임 
            
            if lane_str == '탑' :
               #champ_data[i][2] = 'TRUE'
               champ_data[i][12] = data[0]
               champ_data[i][7] = data[1]
               champ_data[i][17] = ratio_str 
            if lane_str == '정글' :
               #champ_data[i][3] = 'TRUE'
               champ_data[i][13] = data[0]
               champ_data[i][8] = data[1]
               champ_data[i][18] = ratio_str
            if lane_str == '미드' :
               #champ_data[i][4] = 'TRUE'
               champ_data[i][14] = data[0]
               champ_data[i][9] = data[1]
               champ_data[i][19] = ratio_str
            if lane_str == '원딜' :
               #champ_data[i][5] = 'TRUE'
               champ_data[i][15] = data[0]
               champ_data[i][10] = data[1]
               champ_data[i][20] = ratio_str
            if lane_str == '서포터' :
               #champ_data[i][6] = 'TRUE'
               champ_data[i][16] = data[0]
               champ_data[i][11] = data[1]
               champ_data[i][21] = ratio_str
        #이제 array에 데이터 넣어야 함. 
        #champ_data[i][2] : 탑
        #champ_data[i][7] : 탑픽률 
        #champ_data[i][12] : 탑승률 
        
        champ_name = []
        champ_value = []
        how_many_champs_for_matchup_rate = 0
        '''
        #Row_active
        row_active_name = soup.find("tr", {"class" : "Row active"}).find("td", {"class" : "Cell Champion"})
        row_active_name_str = str(row_active_name)
        row_active_name_str = row_active_name_str.replace('<td class="Cell Champion">', '').replace('\n', '').replace('\t', '')
        space = row_active_name_str.find('>')
        row_active_name_str = row_active_name_str[space:]
        row_active_name_str = row_active_name_str.replace('</td>', '').replace('>', '')
        print(row_active_name_str)
        row_active_value = soup.find("tr", {"class" : "Row active"}).find("td", {"class" : "Cell Value sorted"})
        row_active_value_str = str(row_active_value)
        row_active_value_str = row_active_value_str.replace('<td class="Cell Value sorted">', '').replace('\t', '').replace('\n', '')
        space = row_active_value_str.find('%')
        row_active_value_str = row_active_value_str[:space]
        print(row_active_value_str)
        champ_name.append(row_active_name_str)
        champ_value.append(row_active_value_str)
        how_many_champs_for_matchup_rate += 1
        print('챔프넘버는 : ', champ_name_to_champ_num(champ_number_data, row_active_name_str))
        '''
        #이유는 모르겠는데 Row만 돌려도 Row Active결과가 포함되서 나온다 ???? 왜지???
        index = 0
        for child in soup.find("div", {"class":"SideContent"}).find_all("tr", {"class" : "Row"}) :
            if index >= 1:
                row_active_name = child.find("td", {"class" : "Cell Champion"})
                row_active_name_str = str(row_active_name)
                row_active_name_str = row_active_name_str.replace('<td class="Cell Champion">', '').replace('\n', '').replace('\t', '')
                space = row_active_name_str.find('>')
                row_active_name_str = row_active_name_str[space:]
                row_active_name_str = row_active_name_str.replace('</td>', '').replace('>', '')
                #print(row_active_name_str)
                row_active_value = child.find("td", {"class" : "Cell Value sorted"})
                row_active_value_str = str(row_active_value)
                row_active_value_str = row_active_value_str.replace('<td class="Cell Value sorted">', '').replace('\t', '').replace('\n', '')
                space = row_active_value_str.find('%')
                row_active_value_str = row_active_value_str[:space]
                #print(row_active_value_str)
                #print('챔프넘버는 : ', champ_name_to_champ_num(champ_number_data, row_active_name_str))
                
                champ_name.append(row_active_name_str)
                champ_value.append(row_active_value_str)
                how_many_champs_for_matchup_rate +=1
            index = index+1
        #print('index는 ', index)
        #print('lane은 ', lane_name)
        #print(champ_name)
        #print(champ_value)
        for j in range (0, index-1) :
            if lane_name == "top" :
                #print('내 챔프는 ', i, '적 챔프는 ', champ_name_to_champ_num(champ_number_data, champ_name[j]), '매치업 확률은 ', champ_value[j] )
                counterpick_data_top_matchup_rate[i][champ_name_to_champ_num(champ_number_data, champ_name[j])] = champ_value[j]
            if lane_name == "jungle" :
                counterpick_data_jungle_matchup_rate[i][champ_name_to_champ_num(champ_number_data, champ_name[j])] = champ_value[j]
            if lane_name == "mid" :
                counterpick_data_mid_matchup_rate[i][champ_name_to_champ_num(champ_number_data, champ_name[j])] = champ_value[j]
            if lane_name == "adc" :
                counterpick_data_adc_matchup_rate[i][champ_name_to_champ_num(champ_number_data, champ_name[j])] = champ_value[j]
            if lane_name == "sup" :
                counterpick_data_sup_matchup_rate[i][champ_name_to_champ_num(champ_number_data, champ_name[j])] = champ_value[j]
        
    except : 
        print('페이지자체는  떴지만 server error페이지가 떴다 고로 이 챔프의 이 라인은 없다 ' )

def parsing_algorithm_for_winrate_and_solokillrate(soup, i, j, lane_number,champ_number_data, counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation):
    print('parsing')
    #try 블록안에서 파싱함. 여기서부터 파싱! html이 제대로 긁히지 않았을 경우(챔프가 고인이거나, 위에서 timeout문제로 제대로 긁어오지 못한) 오류처리하기 위함 
    try :
                        
        #승률 파싱하는 부분 
        for child in soup.find_all("div", {"class":"RealContent"}):
            blue_win = child.find("div", {"class":"Champion Blue"}).find("span", {"class":"tip __tipped__"})
            #print(blue_win)
            red_win = child.find("div", {"class":"Champion Red"}).find("span", {"class":"tip __tipped__"})
            #print(red_win)
            
        print('내챔프 :', userCsv.data_num_to_champ_name_korean(i, champ_number_data), ' , 적챔프 :', userCsv.data_num_to_champ_name_korean(j, champ_number_data))
        blue_win_str = str(blue_win)
        blue_win_str = blue_win_str.replace('<span class="tip __tipped__">', '')
        blue_win_str = blue_win_str.replace('</span>', '')
        red_win_str = str(red_win)
        red_win_str = red_win_str.replace('<span class="tip __tipped__">', '')
        red_win_str = red_win_str.replace('</span>', '')
        print('블루 승률', blue_win_str)
        print('레드 승률', red_win_str)
        #str로 저장한거 보여주기 
        
        #st에서 '%'제거하고 문자열 마무리 -> floatdㅡ로 변환 
        space = blue_win_str.find('%')
        blue_win_float = float(blue_win_str[:space])
        space = red_win_str.find('%')
        red_win_float = float(red_win_str[:space])
        '''
        print(blue_win_float)
        print(red_win_float)
        '''
        
        counterpick_data_win_rate[i][j] = blue_win_float
        counterpick_data_win_rate[j][i] = red_win_float

        #솔로킬 파싱하는 부분 
        bluesolokill = ""
        redsolokill = ""    
        for solokillrate in soup.find_all("table", {"class":"CounterChampionStatsTable"}) :
            temp = solokillrate.find("tbody", {"class":"Content"}).find("tr", {"class":"Row"}).children
        #Content에 들어있는 첫번재 Row의 children중에서 인덱스 1 일때 왼쪽, 인덱스 5일때 오른쪽의 solokill rate가 들어있음.
            for index, child in enumerate(temp):
                if index == 1:
                    blue_solokill = child
                        #print (blue_solokill)
                elif index == 5:
                    red_solokill = child
                        #print (red_solokill)
        blue_solokill_str = str(blue_solokill)
        blue_solokill_str = blue_solokill_str.replace('<td class="Cell Value Left ">', '')
        blue_solokill_str = blue_solokill_str.replace('<td class="Cell Value Left Fill">', '')
        blue_solokill_str = blue_solokill_str.replace('<span class="Change">', '')
        blue_solokill_str = blue_solokill_str.replace('<i class="__spSite __spSite-', '')
        blue_solokill_str = blue_solokill_str.replace('"></i>', '')
        blue_solokill_str = blue_solokill_str.replace('\t', '')
        blue_solokill_str = blue_solokill_str.replace('\n', '')
        if lane_number==2 or lane_number==3 or lane_number==4 or lane_number==5 :
            print('블루 솔로킬 확률', blue_solokill_str[:5])
        if lane_number==6 :
            print('블루 킬관여율 차이', blue_solokill_str[:5])

        red_solokill_str = str(red_solokill)
        red_solokill_str = red_solokill_str.replace('<td class="Cell Value Right ">', '')
        red_solokill_str = red_solokill_str.replace('<td class="Cell Value Right Fill">', '')
        red_solokill_str = red_solokill_str.replace('<span class="Change">', '')
        red_solokill_str = red_solokill_str.replace('<i class="__spSite __spSite-', '')
        red_solokill_str = red_solokill_str.replace('"></i>', '')
        red_solokill_str = red_solokill_str.replace('\t', '')
        red_solokill_str = red_solokill_str.replace('\n', '')
        if lane_number==2 or lane_number==3 or lane_number==4 or lane_number==5 :
            print('레드 솔로킬 확률', red_solokill_str[:5])
        if lane_number==6 :
            print('레드 킬관여율 차이', red_solokill_str[:5])               
        #str로 저장한거 보여주기 
        
        #st에서 '%'제거하고 문자열 마무리 -> float으로 변환   
        if lane_number==2 or lane_number==3 or lane_number==4 or lane_number==5 :
            space = blue_solokill_str.find('%')
            blue_solokill_float = float(blue_solokill_str[:space])
            space = red_solokill_str.find('%')
            red_solokill_float = float(red_solokill_str[:space])
        if lane_number == 6 :
            space = blue_solokill_str.find(':')
            blue_solokill_float = float(blue_solokill_str[:space])
            space = red_solokill_str.find(':')
            red_solokill_float = float(red_solokill_str[:space])
        '''
        print(blue_solokill_float)
        print(red_solokill_float)
        '''
        counterpick_data_solokill_rate[i][j] = blue_solokill_float
        counterpick_data_solokill_rate[j][i] = red_solokill_float
        
        #cs 파싱하는 부분 Win일수도 있고 Lose일수도 있기때문에 두번째 요소를 불러와야 한다.
        index = 1
        for child in soup.find("div", {"class" : "PieGraph"} ).find_all("div", {"class":"Content"}) :
            #print('index는 ', index, '내용 ', child )
            if index ==2 :
                blue_cs = child
            index +=1
        
        #print(blue_cs)
        blue_cs_str = str(blue_cs)

        blue_cs_str = blue_cs_str.replace('<div class="DiffValue Lose tip __tipped__">', '').replace('<div class="DiffValue Win tip __tipped__">', '')
        blue_cs_str = blue_cs_str.replace('</div>', '').replace(' ', '').replace('\n', '').replace('\t', '').replace('<divclass="Content">', '')
        #print(blue_cs_str)
        blue_cs_float = float(blue_cs_str)
        red_cs_float = blue_cs_float * (-1)
        if lane_number==2 or lane_number==3 or lane_number==4 or lane_number == 5 :
            print('블루 cs차이 : ',blue_cs_float)
        if lane_number==6 :
            print('블루 분당골드획득량 차이 : ', blue_cs_float)
        if lane_number==2 or lane_number==3 or lane_number==4 or lane_number == 5 :
            print('레드 cs차이 : ',red_cs_float)
        if lane_number==6 :
            print('레드 분당골드획득량 차이 : ', red_cs_float)
       
        counterpick_data_cs_amount[i][j] = blue_cs_float
        counterpick_data_cs_amount[j][i] = red_cs_float
        
        #첫포탑(5번째 Row), 킬관여율(3번째 Row), 총딜량(4번 Row) 파싱하는 부분 
        index = 1
        #다섯번째 Row를 가져옴 
        for child in soup.find("tbody", {"class" : "Content"}).find_all("tr", {"class" : "Row"}) :
            
            
            #print('현재 인덱스 넘버 :', index, '라인넘버 : ', lane_number)
            #print(child)
            if index ==3 and (lane_number ==2 or lane_number==3 or lane_number==4 or lane_number==5) :
                kill_participation = child.children
            if index ==2 and lane_number==6 :
                kill_participation = child.children
            if index ==4 and (lane_number ==2 or lane_number==3 or lane_number==4 or lane_number==5) :
                total_deal = child.children
            if index == 5 and (lane_number ==2  or lane_number==4 or lane_number==5) : 
                turret = child.children
            index +=1
        #그 Row의 자식중 첫번째와 5번째 자식을 불러옴. find로 하지 않는 이유는 클래스의 이름이 변하기 때문에 어쩔수 없이 위치로 하는 것 
        if lane_number==2 or lane_number==4 or lane_number==5 :
            for index, child in enumerate(turret):
                if index == 1:
                    blue_turret = child
                        #print (blue_solokill)
                elif index == 5:
                    red_turret = child
                    #print(blue_turret)
                    #print(red_turret)
                    blue_turret_str = str(blue_turret)
                    blue_turret_str = blue_turret_str.replace('<td class="Cell Value Left ">', '').replace('<td class="Cell Value Left Fill">', '').replace('<span class="Change">', '').replace('\t', '')
                    blue_turret_str = blue_turret_str.replace('<i class="__spSite __spSite-147"></i>', '').replace('</td>', '').replace('</span>', '')
                    blue_turret_str = blue_turret_str.replace('\n', '')
                    blue_turret_str = blue_turret_str[:5]
                    blue_turret_float = float(blue_turret_str[:2]) *60 + float(blue_turret_str[3:5])
                    print('블루 포탑 :', blue_turret_str, ',', blue_turret_float)
                    red_turret_str = str(red_turret)
                    red_turret_str = red_turret_str.replace('<td class="Cell Value Right ">', '').replace('<td class="Cell Value Right Fill">', '').replace('<span class="Change">', '').replace('\t', '')
                    red_turret_str = red_turret_str.replace('<i class="__spSite __spSite-147"></i>', '').replace('</td>', '').replace('</span>', '')
                    red_turret_str = red_turret_str.replace('\n', '')
                    red_turret_str = red_turret_str[:5]
                    red_turret_float = float(red_turret_str[:2]) *60 + float(red_turret_str[3:5])
                    print('레드 포탑 :', red_turret_str, ',', red_turret_float)
           
                    counterpick_data_destroy_first_turret[i][j] = blue_turret_float
                    counterpick_data_destroy_first_turret[j][i] = red_turret_float
        
        #킬관여율
        #그 Row의 자식중 첫번째와 5번째 자식을 불러옴. find로 하지 않는 이유는 클래스의 이름이 변하기 때문에 어쩔수 없이 위치로 하는 것 
        for index, child in enumerate(kill_participation):
                if index == 1:
                    blue_kill_participation = child
                elif index == 5:
                    red_kill_participation = child
        blue_kill_participation_str = str(blue_kill_participation)
        blue_kill_participation_str = blue_kill_participation_str.replace('<td class="Cell Value Left ">', '').replace('<td class="Cell Value Left Fill">', '').replace('<span class="Change">', '').replace('\t', '')
        blue_kill_participation_str = blue_kill_participation_str.replace('</td>', '').replace('</span>', '')
        blue_kill_participation_str = blue_kill_participation_str.replace('\n', '')
        space = blue_kill_participation_str.find('%')
        blue_kill_participation_float = float(blue_kill_participation_str[:space])
        print('블루 킬관여율 :', blue_kill_participation_float)
        red_kill_participation_str = str(red_kill_participation)
        red_kill_participation_str = red_kill_participation_str.replace('<td class="Cell Value Right ">', '').replace('<td class="Cell Value Right Fill">', '').replace('<span class="Change">', '').replace('\t', '')
        red_kill_participation_str = red_kill_participation_str.replace('</td>', '').replace('</span>', '')
        red_kill_participation_str = red_kill_participation_str.replace('\n', '')
        space = red_kill_participation_str.find('%')
        red_kill_participation_float = float(red_kill_participation_str[:space])
        print('레드 킬관여율 :', red_kill_participation_float)
        
        counterpick_data_kill_participation[i][j] = blue_kill_participation_float
        counterpick_data_kill_participation[j][i] = red_kill_participation_float
                       
        #총딜량
        if lane_number ==2 or lane_number==3 or lane_number==4 or lane_number==5 :
            for index, child in enumerate(total_deal):
                if index == 1:
                    blue_total_deal = child
                        #print (blue_solokill)
                elif index == 5:
                    red_total_deal = child
                    #print(blue_total_deal)
                    blue_total_deal_str = str(blue_total_deal)
                    blue_total_deal_str = blue_total_deal_str.replace('<td class="Cell Value Left ">', '').replace('<td class="Cell Value Left Fill">', '').replace('<span class="Change">', '').replace('\t', '')
                    blue_total_deal_str = blue_total_deal_str.replace('</td>', '').replace('</span>', '')
                    blue_total_deal_str = blue_total_deal_str.replace('\n', '').replace(',', '')
                    space = blue_total_deal_str.find('<')
                    blue_total_deal_float = float(blue_total_deal_str[:space])
                    print('블루 총딜량 : ', blue_total_deal_float)  
                    red_total_deal_str = str(red_total_deal)
                    red_total_deal_str = red_total_deal_str.replace('<td class="Cell Value Right ">', '').replace('<td class="Cell Value Right Fill">', '').replace('<span class="Change">', '').replace('\t', '')
                    red_total_deal_str = red_total_deal_str.replace('</td>', '').replace('</span>', '')
                    red_total_deal_str = red_total_deal_str.replace('\n', '').replace(',', '')
                    space = red_total_deal_str.find('<')
                    red_total_deal_float = float(red_total_deal_str[:space])
                    print('레드 총딜량 : ', red_total_deal_float)       
        
                    counterpick_data_total_deal[i][j] = blue_total_deal_float
                    counterpick_data_total_deal[j][i] = red_total_deal_float
        
                    
    except :
        print("상대방이 고인이든가 내가 고인이든가 ")
        champ_checked.append([i,j])
        #어차피 i,j데이터가 없으면 j,i데이터도 없을테니 여기서 append(i,j)하도록 추가해야


'''
#find_some과 같이 직사각형 영역을 채운다 
#이때 blueside와 redside의 영역을 동시에 저장하기 때문에 (의도하지 않은) 대각선 대칭인 직사각형 영역도 채워진다. 
def fill_somechamp_against_somechamp(from_champ_a, to_champ_a, from_champ_b, to_champ_b, champ_data, champ_number_data, driver, lane, file_to_update_winrate, file_to_update_solokillrate) :
    print('fill~~~ ')
    array_winrate = userCsv.read_csv_counterpick_data(file_to_update_winrate) 
    array_solokillrate = userCsv.read_csv_counterpick_data(file_to_update_solokillrate)
    
    if lane == 'top':
        lane_number=2
    elif lane == 'jungle':
        lane_number=3
    elif lane == 'mid':
        lane_number=4
    elif lane == 'adc':
        lane_number=5
    elif lane == 'sup':
        lane_number=6

    if lane == 'top':
        lane_name_lower_case='top'
    elif lane == 'jungle':
        lane_name_lower_case='jungle'
    elif lane == 'mid':
        lane_name_lower_case='mid'
    elif lane == 'adc':
        lane_name_lower_case='adc'
    elif lane == 'sup':
        lane_name_lower_case='support'
        
    if lane == 'top':
        lane_name_upper_case='TOP'
    elif lane == 'jungle':
        lane_name_upper_case='JUNGLE'
    elif lane == 'mid':
        lane_name_upper_case='MID'
    elif lane == 'adc':
        lane_name_upper_case='ADC'
    elif lane == 'sup':
        lane_name_upper_case='SUPPORT'
    print('index1', from_champ_a)
    print('index2', to_champ_a)
    #from_champ_a는 최소값 2, to_champ_b는 최대값 134(헤카림:마지막자바넘버), how_many_champs=135 일때 헤카림까지 나므로 to_champ_b+1 해야 끝까지 
    #[i,j]를 실행했을때 [j,i]를 실행하는것을 막기 위한 리스트 
    champ_checked = []
    for i in range(from_champ_a, to_champ_a+1) :
    #탑가능하면 실행함, champ_data의 2번째 인덱스가 top_available
        if champ_data[i][lane_number] == "TRUE": 
        #top, jungle도 들어오는 indexd에 따라 바꾸기 
        #url설정하고 driverd에 넘겨주는 부분 
            targetURL ='http://www.op.gg/champion/' +userCsv.data_num_to_champ_name_english(i, champ_number_data) +'/statistics/' +lane_name_lower_case+ '/matchup'
            print(targetURL)
            driver.get(targetURL)
        #아리에서 데이터 검사하고(상대챔프 탑챔프인지), 데이터 불러오고(자바스크립트 실행), 파싱 
            #첫 수행에서 i랑은 이미 다 붙어봤기 때문에, 더이상 i랑은 붙어볼 필요가 없음 
            for j in range(from_champ_b, to_champ_b):
            #j가 lane_available TRUE이고 i!=j일때 실행 
                #[i,j] 혹은 [j,i]가 list에 있는지 확인함. 있으면 실행하지 않음. 
                champ_check_int = champ_checked.count([i,j]) + champ_checked.count([j,i])
                if champ_data[j][lane_number] == "TRUE" and i!=j and champ_check_int ==0:

                #자바스크립트의 내용도 라인에 따라서달라진다. 
                    print('내챔프 : ', i,  ' vs 적챔프 : ', j)
                    javascript = "$.OP.GG.champion.Counter.Change(ChampionMatchUpContent.RealContent, " + userCsv.data_num_to_opgg_num(i, champ_number_data) + ", " + userCsv.data_num_to_opgg_num(j, champ_number_data) + ", '"+ lane_name_upper_case +"');"
                    print(javascript)
                    driver.execute_script(javascript)
                    time.sleep(5)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                
                
                    parsing_algorithm_for_winrate_and_solokillrate(soup, i, j, lane_number, array_winrate, array_solokillrate, champ_number_data)
                    champ_checked.append([i,j])
                    #[i,j]를 리스트에 추가해서 나중에 [j,i]가 실행되는 것을 막음 

                    
    #이 아래로는 csv파일 작성 
    userCsv.write_csv_counterpick_data(array_winrate, file_to_update_winrate)
    userCsv.write_csv_counterpick_data(array_solokillrate, file_to_update_solokillrate)    
'''
def find_line_available(champ_number_data, champ_data, driver,  \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate):
    #http://www.op.gg/champion/ezreal/statistics 으로만 입력하면 알아서 가능한 라인의 페이지가 열림.
                #이 챔프가 가는 라인이 어디인지, 라인별 승률과 픽률이 얼마인지 찾아내서 champ_data에 저장하고, champ_data[i][lane_number]도 업데이트 
                
                #-> 챔프별로 페이지 열면서 상대 라인 찾아서 그에 맞춰 자바스크립트 쏘면서 하는게 더 낫지않나? 
                #자바스크립트 매치업에 뜬다는건 아무리 듣보잡이라도 페이지가 존재한다는 뜻.
                #라인별 승률 픽률은 큰 숫자만 표현하므로 저것만 가지고 라인 TRUE FALSE를 판단할수는 없음.
                #자바스크립트 매치업에 뜨느냐 안뜨느냐를 기준으로 판단해야함!
                #자바스크립트 매치업에 안뜨지만 현재챔프와의 전적이 없을뿐 해당 라인의 다른 챔프와 전적이 있을 가능성은 있다
                #자바스크립트 매치업에 뜨면 이 라인의 데이터는 무조건 있다.
                #이 라인인 챔프를 판별하기는 쉬운데(매치업에 뜨면됨) 이 라인이 아닌 챔프는 어떻게 판별하나?
                
                #결국 모든 라인을 모든 챔프에 대해 돌리고 중복만 빼야 하는게 아닌가?(어떤 신박한 챔프가 나올지 모르기 때문에)
                #신박한 챔프의 등장을 찾아내는게 목푠데.. 
                
                #결론 : 이 메소드는 line_available만 판독해서 넣어주는 메소드이며(명시된 라인에 대해서는 승률 픽률 데이터도 수집) 
                #http://www.op.gg/champion/riven/statistics/mid/matchup
                #여기서 챔프이름, 라인 바꿔서 총챔프수x5 번 시행하면 신박한 챔프 포함해서 line_available데이터는 다 뽑힘 
                #명시된 라인에 대해서는 승률, 픽률 데이터도 불러올수 있다. 
                #페이지 두번 로딩안하게 그 과정에서 매치업까지 불러오면 좋겠지만 line_available이 완성안된 상태라 할수 없음
                #결국 이거 한번 돌리고 뒤에꺼 돌리는 방법밖에 없는듯 
                #pros : line_available정확하게 파악해서 뻘수행을 줄임.각 버전마다 신박한 챔프 등장하는것 자동으로 감지
                #cons : 이 메소드를 돌리는 만큼 실행시간이 늘어남 
    lane_name = ['top', 'jungle', 'mid', 'adc', 'support']
    for i in range(134, how_many_champs) :
        win_and_pick_rate = 0
        
        #해당챔프의 데이터 초기화(이전 데이터 삭제)
        #2~6탑가능, 7~11탑승률, 12~16탑픽률 
        for k in range(2,7) :
            champ_data[i][k] = 'FALSE'
        for k in range(7, 17) :
            champ_data[i][k] = 0
            
            
        for j in range(0,5) :            
            try :
                targetURL ='http://www.op.gg/champion/' +userCsv.data_num_to_champ_name_english(i, champ_number_data) +'/statistics/' + lane_name[j]+ '/matchup'
                print(targetURL)
                driver.get(targetURL)
                
                #내챔프랑 적챔프 얼굴뜨고 승률뜨는 그 클래스가 ChampionMatchUpContent. 그게 나오나 안나오나 검사해서 나오면 넘어가고 안나오면 최대 5초 기다림 
                #안나올경우 TimeoutException을 발생시켜서 except로 간다 
                #element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ChampionMatchUpContent")))
                which_one_is_up = 0;
                #정상페이지 1,없음페이지 2 
                for time in range(0,5) :
                    try :
                        element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.ID, "ChampionMatchUpContent")))
                        print(champ_data[i][0], '의 ', lane_name[j], ' 데이터 존재함 ' )
                        which_one_is_up = 1
                        break
                    except :
                        print('data_exist_fail ')
                    try :
                        element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "SectionHeadLine")))
                        print(champ_data[i][0], '의 ', lane_name[j], ' 데이터는 없음(주소를 넣은 결과) ' )
                        which_one_is_up = 2
                        break
                    except :
                        print('data_notexist_fail')
                if which_one_is_up == 2:
                    element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.ID, "ChampionMatchUpContent")))             
                    
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                #print('페이지 로드됨 ')
                #파싱알고리즘 안에서 데이터를 넣으니까 그레이브즈처럼 탑에서 먼저 파싱해버리면 그 이후에 정글은 페이지 로드만 뜨고 데이터가 안들어간다! 
                #line_available은 페이지 로드됨과 동시에 바로 넣기! 
                if j == 0 :
                    champ_data[i][2] = 'TRUE'
                if j == 1 :
                    champ_data[i][3] = 'TRUE'
                if j == 2 :
                    champ_data[i][4] = 'TRUE'
                if j == 3 :
                    champ_data[i][5] = 'TRUE'
                if j == 4 :
                    champ_data[i][6] = 'TRUE'
                
                if win_and_pick_rate == 0 :              
                    parsing_algorithm_for_winrate_and_pickrate(lane_name[j], soup, i, champ_data, champ_number_data,  \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate)
                    print('페이지 로드되고 데이터도 가져옴 ')
                    #제대로 데이터가 뽑혔으면 win_and_pick_rate를 +1 해야한다.
                    #win_and_pick_rate = 1
                    #print(win_and_pick_rate)
                    #원래는 한번 했던건 다시 안하는데,매치업 데이터는 라인별로 따로 존재하므로 다 돌리게 데이터가 존재하면 무조건 다 긁어옴. 
                     
            
            except :
                print(champ_data[i][0], '의 ', lane_name[j], ' 데이터는 없음(except발생시켜서 폭파시킨 결과) ' )    
    #이 아래로는 csv파일 작성 
    write_csv_winrate_and_pickrate(champ_data,  \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate )
    return champ_data

def find_some(from_champ_a, to_champ_a, from_champ_b, to_champ_b, champ_data, champ_number_data, driver, lane, \
              counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation) :
    
    print(lane)
    
     #lane은 'top', 'jungle', 'mid', 'adc', 'sup'과 같이 문자열로 준다 
    if lane == 'top':
        lane_number=2
    elif lane == 'jungle':
        lane_number=3
    elif lane == 'mid':
        lane_number=4
    elif lane == 'adc':
        lane_number=5
    elif lane == 'sup':
        lane_number=6

    if lane == 'top':
        lane_name_lower_case='top'
    elif lane == 'jungle':
        lane_name_lower_case='jungle'
    elif lane == 'mid':
        lane_name_lower_case='mid'
    elif lane == 'adc':
        lane_name_lower_case='adc'
    elif lane == 'sup':
        lane_name_lower_case='support'
        
    if lane == 'top':
        lane_name_upper_case='TOP'
    elif lane == 'jungle':
        lane_name_upper_case='JUNGLE'
    elif lane == 'mid':
        lane_name_upper_case='MID'
    elif lane == 'adc':
        lane_name_upper_case='ADC'
    elif lane == 'sup':
        lane_name_upper_case='SUPPORT'
    #[i,j]를 실행했을때 [j,i]를 실행하는것을 막기위한 리스트 
    champ_checked = []
    #한 챔프만 할 경우를 대비해서, 두번째 인덱스에는 여기까지라고 원하는 챔프 +1의 값이 들어가야함. 따라서 find_all에서는 how_many_champs(135)가 아닌 챔프마지막 번호(134)를 줘야함 
    #요약 호출할때는 원하는 뒷번호를 인덱스로 주고, 여기서 돌릴때는 +1 해서 돌려야 원하는 뒷번호까지 포함해서 나온다 
    for i in range(from_champ_a, to_champ_a+1) :
    #탑가능하면 실행함, champ_data의 2번째 인덱스가 top_available
        if champ_data[i][lane_number] == "TRUE": 
        #top, jungle도 들어오는 indexd에 따라 바꾸기 
        #url설정하고 driverd에 넘겨주는 부분 
            try :
                targetURL ='http://www.op.gg/champion/' +userCsv.data_num_to_champ_name_english(i, champ_number_data) +'/statistics/' +lane_name_lower_case+ '/matchup'
                print(targetURL)
                driver.get(targetURL)
                
                
                
                
                
                
                
                #아리에서 데이터 검사하고(상대챔프 탑챔프인지), 데이터 불러오고(자바스크립트 실행), 파싱 
                #첫 수행에서 i랑은 이미 다 붙어봤기 때문에, 더이상 i랑은 붙어볼 필요가 없음 
                #한 챔프만 할 경우를 대비해서, 두번째 인덱스에는 여기까지라고 원하는 챔프 +1의 값이 들어가야함. 따라서 find_all에서는 how_many_champs(135)가 아닌 챔프마지막 번호(134)를 줘야함 
                for j in range(from_champ_b, to_champ_b+1): #from_champ_b
            #j가 lane_available TRUE이고 i!=j일때 실행 
                #[i,j] 혹은 [j,i]가 list에 있는지 확인함. 있으면 실행하지 않음. 
                    champ_check_int = champ_checked.count([i,j]) + champ_checked.count([j,i])
                    if champ_data[j][lane_number] == "TRUE" and i!=j and champ_check_int ==0:
                
                #자바스크립트의 내용도 라인에 따라서달라진다. 
                        try :
                            print('내챔프 : ', i,  ' vs 적챔프 : ', j)
                            javascript = "$.OP.GG.champion.Counter.Change(ChampionMatchUpContent.RealContent, " + userCsv.data_num_to_opgg_num(i, champ_number_data) + ", " + userCsv.data_num_to_opgg_num(j, champ_number_data) + ", '"+ lane_name_upper_case +"');"
                            print(javascript)
                            driver.execute_script(javascript)
                            #time.sleep(5)
                        
                            which_one_is_up = 0
                            for time in range(0,5) :
                                try :
                                    element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "Versus")))
                                    print('이 매치업 데이터가 존재함 ')
                                    which_one_is_up = 1
                                    break
                                except :
                                    print('data_exist_fail ')
                                try :
                                    element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "ErrorMessage")))
                                    print('이 매치업 데이터가 없음 ')
                                    which_one_is_up = 2
                                    break
                                except :
                                    print('data_notexist_fail')
                            if which_one_is_up == 2:
                                element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "Versus"))) 
                        
                            html = driver.page_source
                            soup = BeautifulSoup(html, 'html.parser')
                
                
                            parsing_algorithm_for_winrate_and_solokillrate(soup, i, j, lane_number, champ_number_data, counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation)
                            champ_checked.append([i,j])
                        except :
                            print('상대의 매치업 데이터가 없다. ')
                            champ_checked.append([i,j])
                    #[i,j]를 리스트에 추가해서 나중에 [j,i]가 실행되는 것을 막음 
            except :
                print('페이지에 문제있음 ')    
    #이 아래로는 csv파일 작성 
    write_csv_winrate_and_solokillrate(lane, counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation)
    
    
def find_all(champ_data, champ_number_data, driver, lane, counterpick_data_win_rate, counterpick_data_solokill_rate) :
    
    find_some(2, how_many_champs-1, 2, how_many_champs-1, champ_data, champ_number_data, driver, lane, counterpick_data_win_rate, counterpick_data_solokill_rate)
   
def champ_name_to_champ_num(champ_number_data, champ_name):
    for i in range(2, how_many_champs) : 
        #print('비교 ::::: 인덱스 ', i, '일때 챔프이름 :', champ_number_data[i][0], ' ,함수에서 받은 챔프이름 : ', champ_name)
        if champ_number_data[i][0].count(champ_name) == 1 :
            return i
'''   
def fill_onechamp_against_onechamp(from_champ_a, from_champ_b, champ_data, champ_number_data, driver, lane, file_to_update_winrate, file_to_update_solokillrate) :
    fill_somechamp_against_somechamp(from_champ_a, from_champ_a, from_champ_b, from_champ_b, champ_data, champ_number_data, driver, lane, file_to_update_winrate, file_to_update_solokillrate)   
    
def fill_onechamp_against_somechamp(from_champ_a, from_champ_b, to_champ_b, champ_data, champ_number_data, driver, lane, file_to_update_winrate, file_to_update_solokillrate) :
    fill_somechamp_against_somechamp(from_champ_a, from_champ_a, from_champ_b, to_champ_b, champ_data, champ_number_data, driver, lane, file_to_update_winrate, file_to_update_solokillrate)
'''
