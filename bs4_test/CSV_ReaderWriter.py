'''
Created on 2016. 11. 10.

@author: HyeonWoo
'''
#-*- coding: utf-8 -*-

import csv
import math
from builtins import range

how_many_champs = 136
how_many_properties = 48



  

def initiate_counterpick_data(counterpick_data, array):

    for i in range(0,how_many_champs):
        for j in range(0,how_many_champs):
            counterpick_data[i][j] = 0
    #챔프한글이름입력(세로) 
    #챔프넘버 = 인덱스 넘버로 맞추자!champ_number_data는 인덱스가 1씩 차이나지만 카운터픽 데이터는 그대로 맞출것 
    for i in range(2, how_many_champs):
        counterpick_data[i][0] = data_num_to_champ_name_korean(i, array)
        counterpick_data[0][i] = data_num_to_champ_name_korean(i, array)

def write_csv_champ_data(champ_data, filename):
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/' + filename +'.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    
    array = [[0]*how_many_properties for row in range(how_many_champs-1)]    
    for i in range (0, how_many_champs-1) :
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        for j in range (0,how_many_properties):
            array[i][j] = champ_data[i+1][j]

    
    for index, i in enumerate(array):
        #champ_datad[0]은 비어있는 라인. (처음에 챔프넘버 = 인덱스 넘버로 쓰고싶다고 찡찡거리면서 첫칸 비우고 받아왔기 때문) 
        #즉 비어있는 라인 문제를 해결하기 위해서는 write할때 첫줄부터 차있는 새 array를 만들어서 써야 한다. 
        csvWriter.writerow(array[index])
    f.close()

def write_csv_counterpick_data(counterpick_data, filename):
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/' + filename +'.csv'
    f = open(filepath, 'w',newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(counterpick_data):
        csvWriter.writerow(counterpick_data[index])
    f.close()
    
def read_csv_counterpick_data(filename):
    counterpick_data = [[0]*how_many_champs for row in range(how_many_champs)]
    
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/' + filename +'.csv'
    f = open(filepath, 'r', encoding="utf-8")
    
    csvReader = csv.reader(f)
    for index, i in enumerate(csvReader):
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        for j in range (0,how_many_champs):
            counterpick_data[index][j] = i[j]
        
    return counterpick_data
    f.close()

def read_csv_champ_data():
 
 
    #바로 밑에!!!! 여기서 이지랄하다가 csv파일에 하나씩 밀려서 저장되가지고 자바에서 받을때 이상해짐. 
    #csv를 넘버스로 읽어서 볼때는 이상해보이지만 챔프 넘버(자바)만 제대로 인지하고 있으면 자바랑 파이썬 내에서는 자바챔프넘버 = 인덱스 넘버이므로 아무 문제가 없다
    #다만 넘버스로 csv읽을때 졸라 헷갈림  
    
    
    #데이터 사용할때는 array[내가 원하는챔프][불러오기를 원하는 속성] 으로 호출 
    array = [[0]*how_many_properties for row in range(how_many_champs)]
    f = open('/Users/HyeonWoo/Google 드라이브/LOLcoach/champ_data_csv.csv', 'r', encoding="utf-8")  
    csvReader = csv.reader(f)    #reader로 파일을 읽는다.   
    for index, i in enumerate(csvReader):
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        for j in range (0,how_many_properties):
            array[index+1][j] = i[j]
    f.close()
    return array

def read_csv_with_file_name_champ_data(filename):
 
 
    #바로 밑에!!!! 여기서 이지랄하다가 csv파일에 하나씩 밀려서 저장되가지고 자바에서 받을때 이상해짐. 
    #csv를 넘버스로 읽어서 볼때는 이상해보이지만 챔프 넘버(자바)만 제대로 인지하고 있으면 자바랑 파이썬 내에서는 자바챔프넘버 = 인덱스 넘버이므로 아무 문제가 없다
    #다만 넘버스로 csv읽을때 졸라 헷갈림  
    
    
    #데이터 사용할때는 array[내가 원하는챔프][불러오기를 원하는 속성] 으로 호출 
    array = [[0]*how_many_properties for row in range(how_many_champs)]
    f = open('/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/champ_data_csv_'+filename+'.csv', 'r', encoding="utf-8")  
    csvReader = csv.reader(f)    #reader로 파일을 읽는다.   
    for index, i in enumerate(csvReader):
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        for j in range (0,how_many_properties):
            array[index+1][j] = i[j]
    f.close()
    return array



def read_csv_champ_number_data():
    #챔프는 134개지만 어레이가 0부터 시작하는걸 감안해 참조 번호 =챔프번호 그대로 쓰기 위해 하나 더 늘림
    #champ_number_data.csv 를 불러온다.
    #앞부분이 챔프넘버, B가 자바챔프넘버(인덱스1), C가 op.gg javascript넘버(인덱스2), D가 op.gg 링크네임(인덱스3)    
    #앞쪽 숫자가 가로 개수, 뒷쪽 숫자가 세로 개수
    #세로 인덱스는 numbers파일과 같고(인덱스 번호=자바챔프번호)
    #가로인덱스는 0:한글이름, 1:자바넘버, 2:op.gg자바스크립트넘버, 3:op.gg이름    
    array = [[0]*4 for row in range(how_many_champs)]
    f = open('/Users/HyeonWoo/Google 드라이브/LOLcoach/champ_number_data_csv.csv', 'r', encoding="utf-8")  
    csvReader = csv.reader(f)    #reader로 파일을 읽는다.   
    for index, i in enumerate(csvReader):
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        array[index+1][0] = i[0]
        array[index+1][1] = i[1]
        array[index+1][2] = i[2]
        array[index+1][3] = i[3]
    return array

def data_num_to_champ_name_korean(number, array) :         
    return array[number][0]    

def data_num_to_champ_name_english(number, array) :         
    return array[number][3]
    
def data_num_to_opgg_num(number, array):
    return array[number][2]

   

