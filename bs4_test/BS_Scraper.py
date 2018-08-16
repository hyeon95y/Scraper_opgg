'''
Created on 2016. 11. 10.

@author: HyeonWoo
'''

#file_name_counterpick global 붙여줘야 내부에서 전역변수로 되어 아래에 불러올수있음

#-*- coding: utf-8 -*-

import csv
import CSV_ReaderWriter as userCsv
import HTML_Parser as userParser
import Array_for_WEKA as userWeka
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import jpype
import os
from selenium.webdriver.common.action_chains import ActionChains

from py4j.java_gateway import JavaGateway

'''
변수 선언부 시작
'''
how_many_champs = 136

#counterpick배열 선언 
counterpick_data_top_win_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_solokill_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_cs_amount = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_destroy_first_turret = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_total_deal = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_kill_participation = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_top_matchup_rate = [[0]*how_many_champs for row in range(how_many_champs)]

counterpick_data_jungle_win_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_solokill_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_cs_amount = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_destroy_first_turret = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_total_deal = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_kill_participation = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_jungle_matchup_rate = [[0]*how_many_champs for row in range(how_many_champs)]

counterpick_data_mid_win_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_solokill_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_cs_amount = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_destroy_first_turret = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_total_deal = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_kill_participation = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_mid_matchup_rate = [[0]*how_many_champs for row in range(how_many_champs)]

counterpick_data_adc_win_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_solokill_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_cs_amount = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_destroy_first_turret = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_total_deal = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_kill_participation = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_adc_matchup_rate = [[0]*how_many_champs for row in range(how_many_champs)]

counterpick_data_sup_win_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_solokill_rate = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_cs_amount = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_destroy_first_turret = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_total_deal = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_kill_participation = [[0]*how_many_champs for row in range(how_many_champs)]
counterpick_data_sup_matchup_rate = [[0]*how_many_champs for row in range(how_many_champs)]


'''
변수 선언부 끝
'''


'''
함수 구현부 시작
'''

def counterpick_data_initiate():
#counterpick_data 초기화(챔프 이름 입력해주고, 나머지는 0으로 초기화)
    userCsv.initiate_counterpick_data(counterpick_data_top_win_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_win_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_win_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_win_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_win_rate, champ_number_data)


    userCsv.initiate_counterpick_data(counterpick_data_top_solokill_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_solokill_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_solokill_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_solokill_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_solokill_rate, champ_number_data)

    userCsv.initiate_counterpick_data(counterpick_data_top_cs_amount, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_cs_amount, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_cs_amount, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_cs_amount, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_cs_amount, champ_number_data)

    userCsv.initiate_counterpick_data(counterpick_data_top_destroy_first_turret, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_destroy_first_turret, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_destroy_first_turret, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_destroy_first_turret, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_destroy_first_turret, champ_number_data)

    userCsv.initiate_counterpick_data(counterpick_data_top_total_deal, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_total_deal, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_total_deal, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_total_deal, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_total_deal, champ_number_data)

    userCsv.initiate_counterpick_data(counterpick_data_top_kill_participation, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_kill_participation, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_kill_participation, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_kill_participation, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_kill_participation, champ_number_data)

    userCsv.initiate_counterpick_data(counterpick_data_top_matchup_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_jungle_matchup_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_mid_matchup_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_adc_matchup_rate, champ_number_data)
    userCsv.initiate_counterpick_data(counterpick_data_sup_matchup_rate, champ_number_data)

#find_all 따로 만들어서 쓰기 보다는 find_some에 인덱스 2, how_many_champs넣어서 써야 유지보수하기 편함
#how_many_champs-1을 넣어야 하는 것이 아닌지??
#어레이 생성할때는 how_many_champs=135 해서 135로 만들어야하고 실제로 생성되는건 0~134기 때문에 생성할때 빼고는 자바넘버 그대로 넣어야 함
#여기서도 134 넣으면 내부에서 range()때문에 +1 추가해서 돌리기 때문에 134를 넣는게 맞음 
def find_counterpick_data_on_opgg(driver):
    userParser.find_some(133, 135, 133, 135, champ_data, champ_number_data, driver, 'top', counterpick_data_top_win_rate, counterpick_data_top_solokill_rate, counterpick_data_top_cs_amount, counterpick_data_top_destroy_first_turret, counterpick_data_top_total_deal, counterpick_data_top_kill_participation)
    now = time.localtime()
    file_name_counterpick_data_top = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    print('filename_counterpick_top : ', file_name_counterpick_data_top)
    userParser.find_some(133, 135, 133, 135, champ_data, champ_number_data, driver, 'jungle', counterpick_data_jungle_win_rate, counterpick_data_jungle_solokill_rate, counterpick_data_jungle_cs_amount, counterpick_data_jungle_destroy_first_turret, counterpick_data_jungle_total_deal, counterpick_data_jungle_kill_participation)
    now = time.localtime()
    file_name_counterpick_data_jungle = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    print('filename_counterpick_jungle : ', file_name_counterpick_data_jungle)
    userParser.find_some(133, 135, 133, 135, champ_data, champ_number_data, driver, 'mid', counterpick_data_mid_win_rate, counterpick_data_mid_solokill_rate,  counterpick_data_mid_cs_amount, counterpick_data_mid_destroy_first_turret, counterpick_data_mid_total_deal, counterpick_data_mid_kill_participation)
    now = time.localtime()
    file_name_counterpick_data_mid = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    print('filename_counterpick_mid : ', file_name_counterpick_data_mid)
    userParser.find_some(133, 135, 133, 135, champ_data, champ_number_data, driver, 'adc', counterpick_data_adc_win_rate, counterpick_data_adc_solokill_rate, counterpick_data_adc_cs_amount, counterpick_data_adc_destroy_first_turret, counterpick_data_adc_total_deal, counterpick_data_adc_kill_participation)
    now = time.localtime()
    file_name_counterpick_data_adc = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    print('filename_counterpick_adc : ', file_name_counterpick_data_adc)
    userParser.find_some(133, 135, 133, 135, champ_data, champ_number_data, driver, 'sup', counterpick_data_sup_win_rate, counterpick_data_sup_solokill_rate, counterpick_data_sup_cs_amount, counterpick_data_sup_destroy_first_turret, counterpick_data_sup_total_deal, counterpick_data_sup_kill_participation)
    now = time.localtime()
    file_name_counterpick_data_sup = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
    print('filename_counterpick_sup : ', file_name_counterpick_data_sup)


def make_csv_array_for_weka():
    counterpick_data_top_win_rate =  userCsv.read_csv_counterpick_data('counterpick_data_top_win_rate_'+file_name_counterpick_data_top)
    counterpick_data_top_solokill_rate = userCsv.read_csv_counterpick_data('counterpick_data_top_solokill_rate_'+file_name_counterpick_data_top)
    counterpick_data_top_cs_amount = userCsv.read_csv_counterpick_data('counterpick_data_top_cs_amount_'+file_name_counterpick_data_top)
    counterpick_data_top_destroy_first_turret = userCsv.read_csv_counterpick_data('counterpick_data_top_destroy_first_turret_'+file_name_counterpick_data_top)
    counterpick_data_top_total_deal = userCsv.read_csv_counterpick_data('counterpick_data_top_total_deal_'+file_name_counterpick_data_top)
    counterpick_data_top_kill_participation = userCsv.read_csv_counterpick_data('counterpick_data_top_kill_participation_'+file_name_counterpick_data_top)
    counterpick_data_top_matchup_rate = userCsv.read_csv_counterpick_data('counterpick_data_top_matchup_rate_'+file_name_champ_data)
    #newarrayfortest =  userCsv.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"top",champ_data,champ_number_data, counterpick_data_top_win_rate, counterpick_data_top_solokill_rate, counterpick_data_top_cs_amount, counterpick_data_top_destroy_first_turret, counterpick_data_top_total_deal, counterpick_data_top_kill_participation, counterpick_data_top_matchup_rate)
    userWeka.make_arff_for_weka(userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"top",champ_data,champ_number_data, counterpick_data_top_win_rate, counterpick_data_top_solokill_rate, counterpick_data_top_cs_amount, counterpick_data_top_destroy_first_turret, counterpick_data_top_total_deal, counterpick_data_top_kill_participation, counterpick_data_top_matchup_rate), "top")


    counterpick_data_jungle_win_rate =  userCsv.read_csv_counterpick_data('counterpick_data_jungle_win_rate_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_solokill_rate = userCsv.read_csv_counterpick_data('counterpick_data_jungle_solokill_rate_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_cs_amount = userCsv.read_csv_counterpick_data('counterpick_data_jungle_cs_amount_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_destroy_first_turret = userCsv.read_csv_counterpick_data('counterpick_data_jungle_destroy_first_turret_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_total_deal = userCsv.read_csv_counterpick_data('counterpick_data_jungle_total_deal_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_kill_participation = userCsv.read_csv_counterpick_data('counterpick_data_jungle_kill_participation_'+file_name_counterpick_data_jungle)
    counterpick_data_jungle_matchup_rate = userCsv.read_csv_counterpick_data('counterpick_data_jungle_matchup_rate_'+file_name_champ_data)
    #newarrayfortest =  userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"jungle",champ_data,champ_number_data, counterpick_data_jungle_win_rate, counterpick_data_jungle_solokill_rate, counterpick_data_jungle_cs_amount, counterpick_data_jungle_destroy_first_turret, counterpick_data_jungle_total_deal, counterpick_data_jungle_kill_participation, counterpick_data_jungle_matchup_rate)
    userWeka.make_arff_for_weka(userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"jungle",champ_data,champ_number_data, counterpick_data_jungle_win_rate, counterpick_data_jungle_solokill_rate, counterpick_data_jungle_cs_amount, counterpick_data_jungle_destroy_first_turret, counterpick_data_jungle_total_deal, counterpick_data_jungle_kill_participation, counterpick_data_jungle_matchup_rate), 'jungle')



    counterpick_data_mid_win_rate =  userCsv.read_csv_counterpick_data('counterpick_data_mid_win_rate_'+file_name_counterpick_data_mid)
    counterpick_data_mid_solokill_rate = userCsv.read_csv_counterpick_data('counterpick_data_mid_solokill_rate_'+file_name_counterpick_data_mid)
    counterpick_data_mid_cs_amount = userCsv.read_csv_counterpick_data('counterpick_data_mid_cs_amount_'+file_name_counterpick_data_mid)
    counterpick_data_mid_destroy_first_turret = userCsv.read_csv_counterpick_data('counterpick_data_mid_destroy_first_turret_'+file_name_counterpick_data_mid)
    counterpick_data_mid_total_deal = userCsv.read_csv_counterpick_data('counterpick_data_mid_total_deal_'+file_name_counterpick_data_mid)
    counterpick_data_mid_kill_participation = userCsv.read_csv_counterpick_data('counterpick_data_mid_kill_participation_'+file_name_counterpick_data_mid)
    counterpick_data_mid_matchup_rate = userCsv.read_csv_counterpick_data('counterpick_data_mid_matchup_rate_'+file_name_champ_data)
    #newarrayfortest =  userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"mid",champ_data,champ_number_data, counterpick_data_mid_win_rate, counterpick_data_mid_solokill_rate, counterpick_data_mid_cs_amount, counterpick_data_mid_destroy_first_turret, counterpick_data_mid_total_deal, counterpick_data_mid_kill_participation, counterpick_data_mid_matchup_rate)
    userWeka.make_arff_for_weka(userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"mid",champ_data,champ_number_data, counterpick_data_mid_win_rate, counterpick_data_mid_solokill_rate, counterpick_data_mid_cs_amount, counterpick_data_mid_destroy_first_turret, counterpick_data_mid_total_deal, counterpick_data_mid_kill_participation, counterpick_data_mid_matchup_rate), 'mid')



    counterpick_data_adc_win_rate =  userCsv.read_csv_counterpick_data('counterpick_data_adc_win_rate_'+file_name_counterpick_data_adc)
    counterpick_data_adc_solokill_rate = userCsv.read_csv_counterpick_data('counterpick_data_adc_solokill_rate_'+file_name_counterpick_data_adc)
    counterpick_data_adc_cs_amount = userCsv.read_csv_counterpick_data('counterpick_data_adc_cs_amount_'+file_name_counterpick_data_adc)
    counterpick_data_adc_destroy_first_turret = userCsv.read_csv_counterpick_data('counterpick_data_adc_destroy_first_turret_'+file_name_counterpick_data_adc)
    counterpick_data_adc_total_deal = userCsv.read_csv_counterpick_data('counterpick_data_adc_total_deal_'+file_name_counterpick_data_adc)
    counterpick_data_adc_kill_participation = userCsv.read_csv_counterpick_data('counterpick_data_adc_kill_participation_'+file_name_counterpick_data_adc)
    counterpick_data_adc_matchup_rate = userCsv.read_csv_counterpick_data('counterpick_data_adc_matchup_rate_'+file_name_champ_data)
    #newarrayfortest =  userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"adc",champ_data,champ_number_data, counterpick_data_adc_win_rate, counterpick_data_adc_solokill_rate, counterpick_data_adc_cs_amount, counterpick_data_adc_destroy_first_turret, counterpick_data_adc_total_deal, counterpick_data_adc_kill_participation, counterpick_data_adc_matchup_rate)
    userWeka.make_arff_for_weka(userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"adc",champ_data,champ_number_data, counterpick_data_adc_win_rate, counterpick_data_adc_solokill_rate, counterpick_data_adc_cs_amount, counterpick_data_adc_destroy_first_turret, counterpick_data_adc_total_deal, counterpick_data_adc_kill_participation, counterpick_data_adc_matchup_rate), 'adc')



    counterpick_data_sup_win_rate =  userCsv.read_csv_counterpick_data('counterpick_data_sup_win_rate_'+file_name_counterpick_data_sup)
    counterpick_data_sup_solokill_rate = userCsv.read_csv_counterpick_data('counterpick_data_sup_solokill_rate_'+file_name_counterpick_data_sup)
    counterpick_data_sup_cs_amount = userCsv.read_csv_counterpick_data('counterpick_data_sup_cs_amount_'+file_name_counterpick_data_sup)
    counterpick_data_sup_destroy_first_turret = userCsv.read_csv_counterpick_data('counterpick_data_sup_destroy_first_turret_'+file_name_counterpick_data_sup)
    counterpick_data_sup_total_deal = userCsv.read_csv_counterpick_data('counterpick_data_sup_total_deal_'+file_name_counterpick_data_sup)
    counterpick_data_sup_kill_participation = userCsv.read_csv_counterpick_data('counterpick_data_sup_kill_participation_'+file_name_counterpick_data_sup)
    counterpick_data_sup_matchup_rate = userCsv.read_csv_counterpick_data('counterpick_data_sup_matchup_rate_'+file_name_champ_data)
    #newarrayfortest =  userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"sup",champ_data,champ_number_data, counterpick_data_sup_win_rate, counterpick_data_sup_solokill_rate, counterpick_data_sup_cs_amount, counterpick_data_sup_destroy_first_turret, counterpick_data_sup_total_deal, counterpick_data_sup_kill_participation, counterpick_data_sup_matchup_rate)
    userWeka.make_arff_for_weka(userWeka.make_csv_file_for_weka(1, 0.1, 0.1, 0.1, 0.1, 0.1,"sup",champ_data,champ_number_data, counterpick_data_sup_win_rate, counterpick_data_sup_solokill_rate, counterpick_data_sup_cs_amount, counterpick_data_sup_destroy_first_turret, counterpick_data_sup_total_deal, counterpick_data_sup_kill_participation, counterpick_data_sup_matchup_rate), 'sup')

'''
def make_first_pick_csv_and_convert_it_to_dat ():
    #패스 설정해서 불러오기
    csvpath = '/Users/HyeonWoo/NetBeansProjects/Ahri_Senpai/dist/lib/opencsv-3.8.jar'
    jsouppath = '/Users/HyeonWoo/NetBeansProjects/Ahri_Senpai/dist/lib/jsoup-1.10.1.jar'
    wekapath = '/Applications/WEKA/weka-3-8-0/weka.jar'
    classpath = '/Users/HyeonWoo/NetBeansProjects/Ahri_Senpai/build/classes' + ":" + csvpath +":" + jsouppath + ":" + wekapath


    #JVM실행 
    jpype.startJVM('/Library/Java/JavaVirtualMachines/jdk1.8.0_112.jdk/Contents/MacOS/libjli.dylib', "-Djava.class.path=%s" % (classpath))

    #패키지 가져오기 
    testPkg = jpype.JPackage('ahri_senpai') # get the package
    #클래스 가져오기
    for_python = testPkg.for_python # get the class
    #변수에 클래스 할당
    fp = for_python()

    #weka돌려서 클러스터링 하고, 주관적인 특성까지 만족하는 선픽 뽑아내서 first_pick_available_csv 파일 생성하는 함수 실행
    #이름은 upload지만 dat생성하는 메소드임 헷갈리지 말것!
    fp.make_csv_file(file_name_champ_data)
    fp.upload_Object(file_name_champ_data, file_name_counterpick_data_top, file_name_counterpick_data_jungle, file_name_counterpick_data_mid, file_name_counterpick_data_adc, file_name_counterpick_data_sup)
    #sw.make_csv_file(file_name_champ_data)
    #sw.for_phyton(file_name_champ_data, file_name_counterpick_data_top, file_name_counterpick_data_jungle, file_name_counterpick_data_mid, file_name_counterpick_data_adc, file_name_counterpick_data_sup)
    #JVM 종료
    jpype.shutdownJVM()
'''
    
def make_first_pick_csv_and_convert_it_to_dat_with_py4j():
    
    gateway = JavaGateway()                   # connect to the JVM
    print('py4j실행됨')

    fp = gateway.entry_point        # get the AdditionApplication instance

    fp.make_csv_file(file_name_champ_data)
    fp.upload_Object(file_name_champ_data, file_name_counterpick_data_top, file_name_counterpick_data_jungle, file_name_counterpick_data_mid, file_name_counterpick_data_adc, file_name_counterpick_data_sup)


def run_selenium_to_upload_dat(driver):

    targetURL = 'http://dasguteleben.me/admin/center/'
    print(targetURL)
    #driver는 이미 앞에서 불러옴
    driver.get(targetURL)

    #로그인
    username = driver.find_elements_by_class_name('input_info')
    username[0].click()
    username[0].send_keys('hyeon95y@naver.com')
    username[1].click()
    username[1].send_keys('tato951854!')

    #양식 제출
    form = driver.find_element_by_class_name('btn_login').click()


    #관리자 페이지 들어가서 2초 기다렸다가, 게시글 수정 페이지로 주소를 통해 직접 접속
    time.sleep(2)
    targetURL = 'http://dasguteleben.me/admin/entry/post/?id=26'
    driver.get(targetURL)


    # #document를 불러오는 방법 (글을 쓰는 부분이 #document로 되어있어서(아마 HTML을 내부에 탑재하는 방법인듯) 일반적인 element_find로는 불러와지지 않음)
    textarea = driver.find_element_by_css_selector('iframe')
    

    #글 작성 부분을 클릭하고
    textarea.click()

    #백스페이스로 내용 다 지워버림
    #Action.. 어쩌고는 셀레니움 3의 버그라는 말도 있는데, 여튼 동작하지 않음
    #send_keys를 이용하여 동작시킨다. 
    for i in range(0, 150) :
        textarea.send_keys(Keys.BACK_SPACE)
        i = i + 1
    for i in range(0, 150) :
        textarea.send_keys(Keys.DELETE)
        i = i + 1

    #'파일'클릭해서 파일추가하는 팝업을 띄움
    uploadfile = driver.find_elements_by_class_name('tx-text')
    uploadfile[3].click()



     #driver에 팝업창을 탑재

    #원래창의 handle을 저장해둠
    parent_h = driver.current_window_handle
    #이친구의 윈도우 핸들을 따로 불러옴. 윈도우 핸들에서 팝업과 관련된 내용을 건드릴수 있는듯.
    handles = driver.window_handles
    #driver에 현 페이지(게시글작성)의 핸들(추상적인개념인듯)에서 팝업된 창을 연결킨다 
    driver.switch_to_window(handles.pop())
    #driver.switch_to_window(driver.window_handles.pop())으로 써도 상관없을듯
    #현재 드라이버의 윈도우 핸들의 팝업된 창으로 스위치한다.

    #'파일찾기' 버튼눌러 탐색기 띄움
    time.sleep(3)
    find_file = driver.find_element_by_id('uploadfile')
    find_file.click()

    #opencv통해 탐색기 컨트롤(실제로 파일 업로드되는부분)
    time.sleep(5)

    #확인버튼
    find_button = driver.find_elements_by_class_name('btnlink')
    find_button[2].click()

    #driver에 원래페이지(게시글작성)을 연결시킴.
    driver.switch_to_window(parent_h)

    #원페이지 연결됐는지 테스트
    textarea = driver.find_element_by_css_selector('iframe')
    textarea.send_keys('hihihihi')

    #발행후 종료(발행하는 버튼 아직 구현하지 않음)
    print('종료 5초전')
    time.sleep(5)
    driver.quit()
    
def tkinter_test():
    #윈도우에서와 맥에서의 제어가 다름. 고로 집에가서 윈도우로 해야함
    print('this is test')
    
def update_date_for_notice():
    f = open("/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/ahri_senpai_notice.txt", 'r',  encoding="utf-8")
    texts = []
    
    
    lines = f.readlines()
    for line in lines:
        texts.append(line)
        #print(line)
    
        
    print('여기서부터는 texts에 저장된 내용')
    #for i in range(0,9) :
        #print(texts[i])
    now = time.localtime()   
    today = str(now.tm_year) +'.'+ str('%02d'%(now.tm_mon)) +'.'+ str('%02d'%(now.tm_mday)) +'\n'
    print(today)  
    
    texts[3] = today  
    
    #for i in range(0,9) :
        #print(texts[i])                                                            
    
    f.close()
    
    f = open("/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/ahri_senpai_notice.txt", 'w',  encoding="utf-8")
    for i in range(0, 9):
        data = texts[i]
        f.write(data)
    f.close()
    

'''
함수 구현부 끝
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''함수 구현부 - 테스트함수 '''


















































''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
이 아래부터 프로그램 동작
'''
if __name__ == '__main__':
    pass


#프로세스0 업데이트 파일 날짜 수정
update_date_for_notice()

#프로세스 1
#champ_number_data.csv 파일 오픈 
#한글이름 - 자바넘버 - 오피지지넘버 - 오피지지영문이름 변환시켜주는 데이터  
champ_number_data = userCsv.read_csv_champ_number_data()  



#프로세스2
#champ_data.csv 파일 오픈
champ_data = userCsv.read_csv_champ_data()   



#프로세스3
#counterpick_data 초기화(챔프 이름 입력해주고, 나머지는 0으로 초기화)
counterpick_data_initiate()



#프로세스4
#geckodriver load 
#driver = webdriver.Firefox(executable_path =r"/Library/Frameworks/Python.framework/Versions/3.5/bin/geckodriver")



#프로세스5
#첫번째 인덱스, 두번째 인덱스 챔프 대상으로 페이지 접속하고, 자바스크립트 쏘고, html 가져오고, 파싱해서 csv에 저장까지 해주는 함수 
#모든챔프에 대해서 돌리려면 인덱스 2, how_many_champs로 사용할것 
#line_available_load
'''
champ_data = userParser.find_line_available(champ_number_data, champ_data, driver, \
                                            counterpick_data_top_matchup_rate, counterpick_data_jungle_matchup_rate, counterpick_data_mid_matchup_rate,\
                                            counterpick_data_adc_matchup_rate, counterpick_data_sup_matchup_rate)
now = time.localtime()
file_name_champ_data = str('%02d'%(now.tm_year)) + str('%02d'%(now.tm_mon)) + str('%02d'%(now.tm_mday)) + '_'+ str('%02d'%(now.tm_hour)) + str('%02d'%(now.tm_min))
print('filename_champdata : ', file_name_champ_data)
'''



#프로세스6
#오피지지에서 카운터픽 데이터 긁어오기
#find_counterpick_data_on_opgg(driver)



#프로세스7
#크롤링을 하지 않고 진행할경우 기존 파일 불러오는 코드 
#크롤링을 하지 않고 진행할 경우(크롤링을 할 경우 이 부분은 주석처리)

file_name_champ_data = '20170328_2213'
file_name_counterpick_data_top = '20170329_0010'
file_name_counterpick_data_jungle = '20170329_0144'
file_name_counterpick_data_mid = '20170329_0320'
file_name_counterpick_data_adc = '20170329_0333'
file_name_counterpick_data_sup = '20170329_0454'

#아래부분은 크롤링을 하더라도 유지해야한다(아마도)
#챔프데이터 새로운 파일, 혹은 위에서 지정하는 옛날파일로 갱신하는 부분
champ_data = userCsv.read_csv_with_file_name_champ_data(file_name_champ_data)



#프로세스8
#weka를 위한 array를 csv로 생성
make_csv_array_for_weka()



#프로세스9
'''
Ahri_Senpai.java 실행(from Netbeans)
1. weka 실행시켜서 first_pick_available_csv 생성(make_csv_file)
2. csv파일 읽어서 dat파일로 변환함(upload_Object)
'''   
make_first_pick_csv_and_convert_it_to_dat_with_py4j()



#프로세스10
'''
Selenium실행시켜 티스토리 접속, opencv이용하여 탐색기조작하여 파일 업로드 
'''
#run_selenium_to_upload_dat(driver)


#프로세스11 tkinter test




