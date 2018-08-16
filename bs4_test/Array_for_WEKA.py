'''
Created on 2016. 12. 21.

@author: HyeonWoo
'''
#-*- coding: utf-8 -*-

import csv
import math
from builtins import range

how_many_champs = 136
how_many_properties = 48

def make_arff_for_weka(wekaArray2, lane):
    
    #wekaArray2[i][j]의 i가 세로, j가 가로
    how_many_rows = len(wekaArray2)
    how_many_columns = len(wekaArray2[0])
    
    #print('row 수 ' + str(how_many_rows))
    #print('column 수 ' + str(how_many_columns))
    
    #기본값은 numeric으로 설정되어 있고,nominal만 따로 변경해줄것.
    nominal_or_numeric = ['numeric']*how_many_columns
    
    
    #이 부분은 들어오는 배열에 따라 달라짐.
    #여기서는 첫번째 column만 nominal이므로 그 부분만 변경
    nominal_or_numeric[0] = 'nominal'
    #요기까지
    
    
    #파일 열기 
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/ARFF_File_For_WEKA_' + lane +'.arff'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    
    
    #파일에 쓰일 스트링 생성 
    string = ''
    string = string + '@relation whatever \n'
    
    #column(attribute) 기록 
    for j in range(0, how_many_columns):
        if nominal_or_numeric[j] == 'nominal' :
            string = string + '@attribute ' + wekaArray2[0][j] + ' { '
            #print('\n' + string)
            
            string = string + wekaArray2[1][j]
            for i in range(2, how_many_rows) :
                string = string + ', ' + wekaArray2[i][j] 
                #print('\n' + string)
                #print('\n i값은 : ' + str(i))
            
            string = string + '} \n'
        if nominal_or_numeric[j] == 'numeric' :
            string = string + '@attribute ' + wekaArray2[0][j] + ' numeric \n'
    
    string = string + '\n@data\n'
            
    #data(row) 기록
    for i in range(1, how_many_rows) :
        string = string + wekaArray2[i][0]
        for j in range (1, how_many_columns) : 
            string = string + ', ' + str(wekaArray2[i][j]) 
            
        string = string + '\n'
        #print('\n' + string)
        #print('\n i값은 : ' + str(i))
    
    
    #파일 기록하고 닫기
    f.write(string)
    f.close()
    

def make_csv_file_for_weka(weight1, weight2, weight3, weight4, weight5, weight6, lane,champ_data,champ_number_data, counterpick_data_win_rate, counterpick_data_solokill_rate, counterpick_data_cs_amount, counterpick_data_destroy_first_turret, counterpick_data_total_deal, counterpick_data_kill_participation, counterpick_data_matchup_rate):
    #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
    #champ_data[챔프넘버][0]에 한국 이름이 들어가있다. 
    #챔프 이름에 공백 제거 
    for  i in range (2, how_many_champs):
        #index는 1일때부터 가렌의 데이터를 긁어오기 시작하는데, 이때 array의 인덱스는 2(챔프넘버)에 맞추고 싶으므로 +1해서 저장해준다.
        champ_data[i][0] = champ_data[i][0].replace(' ', '')
    
    how_many_champs_in_this_lane = 0
    champs_in_this_lane = []
    #탑일경우 
    if lane =="top" :
        for i in range (2, how_many_champs) :
            if champ_data[i][2] == "TRUE" and champ_data[i][7] != '0':                
                champs_in_this_lane.append(i)
                how_many_champs_in_this_lane = how_many_champs_in_this_lane + 1
    if lane=="jungle" :
        for i in range (2, how_many_champs) :
            if champ_data[i][3] == "TRUE" and champ_data[i][8] != '0': 
                champs_in_this_lane.append(i)
                how_many_champs_in_this_lane = how_many_champs_in_this_lane + 1               
    if lane=="mid" :
        for i in range (2, how_many_champs) :
            if champ_data[i][4] == "TRUE" and champ_data[i][9] != '0': 
                champs_in_this_lane.append(i)
                how_many_champs_in_this_lane = how_many_champs_in_this_lane + 1
    if lane=="adc" :
        for i in range (2, how_many_champs) :
            if champ_data[i][5] == "TRUE" and champ_data[i][10] != '0': 
                champs_in_this_lane.append(i)
                how_many_champs_in_this_lane = how_many_champs_in_this_lane + 1
    if lane=="sup" :
        for i in range (2, how_many_champs) :
            if champ_data[i][6] == "TRUE" and champ_data[i][11] != '0': 
                champs_in_this_lane.append(i)
                how_many_champs_in_this_lane = how_many_champs_in_this_lane + 1
    
    #print(champs_in_this_lane)
    #print(how_many_champs_in_this_lane)
    
    if lane == "top" :
        userproperties = ['픽률비중곱해진승률', '픽률비중곱해진솔로킬', '픽률비중곱해진cs', '픽률비중곱해진포탑', '픽률비중곱해진총딜', '픽률비중곱해진킬관여']
    if lane == "jungle" :
        userproperties = ['픽률비중곱해진승률', '픽률비중곱해진솔로킬', '픽률비중곱해진cs',  '픽률비중곱해진총딜', '픽률비중곱해진킬관여']
    if lane == "mid" :
        userproperties = ['픽률비중곱해진승률', '픽률비중곱해진솔로킬', '픽률비중곱해진cs', '픽률비중곱해진포탑', '픽률비중곱해진총딜', '픽률비중곱해진킬관여']
    if lane == "adc" :
        userproperties = ['픽률비중곱해진승률', '픽률비중곱해진솔로킬', '픽률비중곱해진cs', '픽률비중곱해진포탑', '픽률비중곱해진총딜', '픽률비중곱해진킬관여']
    if lane == "sup" :
        userproperties = ['픽률비중곱해진승률', '픽률비중곱해진분당획득골드(cs)',  '픽률비중곱해진킬관여']
    how_many_properties_for_line = len(userproperties)
    #how_many_properties_for_line = 6

    #표준화를 위한 각 컬럼의 총합     
    total_amount_of_each_line=[0]*(how_many_champs_in_this_lane*how_many_properties_for_line)
    #표준화를 위한 각 컬럼의 요소수 
    how_many_data_in_this_line=[0]*(how_many_champs_in_this_lane*how_many_properties_for_line)
    #표준화를 위한 각 컬럼의평균 
    average_of_each_line=[0]*(how_many_champs_in_this_lane*how_many_properties_for_line)
    #SDV 계산을 위한 (값-평균)^의 시그마가 저장되는 리스트 
    temp = [0]*(how_many_champs_in_this_lane*how_many_properties_for_line)
    #표준화를 위한 각 컬럼의 SDV
    standard_deviation_of_each_line = [0]*(how_many_champs_in_this_lane*how_many_properties_for_line)    
    
    
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    basicArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #print(basicArray[0].__len__())
    #앞쪽 인덱스가 세로, 뒤쪽 인덱스가 가로인듯 
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:               
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:                
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                basicArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                basicArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                basicArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                basicArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                basicArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 
            if j>=0 and j<(how_many_champs_in_this_lane) and i>=0 and i<how_many_champs_in_this_lane :                
                if counterpick_data_win_rate[champs_in_this_lane[i]][champs_in_this_lane[j]] != '0' :
                    #print('index i 는 ',i, 'index j는 ', j )
                    basicArray[i+1][j+1] =  str(counterpick_data_win_rate[champs_in_this_lane[i]][champs_in_this_lane[j]])
                    total_amount_of_each_line[j] += float(counterpick_data_win_rate[champs_in_this_lane[i]][champs_in_this_lane[j]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_win_rate[champs_in_this_lane[i]][champs_in_this_lane[j]] == '0':
                    basicArray[i+1][j+1]= '?'
            #솔로킬 
            elif j>=how_many_champs_in_this_lane and j<(how_many_champs_in_this_lane*2) and i>=0 and i<how_many_champs_in_this_lane :                
                if counterpick_data_solokill_rate[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane]] != '0':
                    basicArray[i+1][j+1] =  str(counterpick_data_solokill_rate[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane]]) 
                    total_amount_of_each_line[j] += float(counterpick_data_solokill_rate[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_solokill_rate[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane]] == '0' :
                    basicArray[i+1][j+1] = '?'
            #씨에스 
            elif j>=how_many_champs_in_this_lane*2 and j<(how_many_champs_in_this_lane*3) and i>=0 and i<how_many_champs_in_this_lane :
                if counterpick_data_cs_amount[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*2]] != '0' :               
                    basicArray[i+1][j+1] =  str(counterpick_data_cs_amount[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*2]]) 
                    total_amount_of_each_line[j] += float(counterpick_data_cs_amount[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*2]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_cs_amount[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*2]] == '0' :
                    basicArray[i+1][j+1] = '?'
            #포탑 
            elif j>=how_many_champs_in_this_lane*3 and j<(how_many_champs_in_this_lane*4) and i>=0 and i<how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if counterpick_data_destroy_first_turret[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*3]] != '0':
                    basicArray[i+1][j+1] =  str(counterpick_data_destroy_first_turret[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*3]])
                    total_amount_of_each_line[j] += float(counterpick_data_destroy_first_turret[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*3]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_destroy_first_turret[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*3]] == '0':
                    basicArray[i+1][j+1] = '?'
            #딜 
            elif j>=how_many_champs_in_this_lane*4 and j<(how_many_champs_in_this_lane*5) and i>=0 and i<how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if counterpick_data_total_deal[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*4]]!= '0':
                    basicArray[i+1][j+1] =  str(counterpick_data_total_deal[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*4]])
                    total_amount_of_each_line[j] += float(counterpick_data_total_deal[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*4]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_total_deal[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*4]] == '0' :
                    basicArray[i+1][j+1] = '?'
            #킬관여
            elif j>=how_many_champs_in_this_lane*5 and j<(how_many_champs_in_this_lane*6) and i>=0 and i<how_many_champs_in_this_lane and how_many_properties_for_line>=6 :                
                if counterpick_data_kill_participation[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*5]] != '0' :
                    basicArray[i+1][j+1] =  str(counterpick_data_kill_participation[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*5]]) 
                    total_amount_of_each_line[j] += float(counterpick_data_kill_participation[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*5]])
                    how_many_data_in_this_line[j] += 1
                if counterpick_data_kill_participation[champs_in_this_lane[i]][champs_in_this_lane[j-how_many_champs_in_this_lane*5]]== '0' :
                    basicArray[i+1][j+1] ='?'
    
    #데이터 집어넣는 와중에 각 컬럼의 총량이랑 요소수는 계산된다. 
    #각 컬럼의 평균값 계산 
    for j in range (0, how_many_champs_in_this_lane*how_many_properties_for_line) : 
        if how_many_data_in_this_line[j] != 0 :
            average_of_each_line[j] = total_amount_of_each_line[j] / how_many_data_in_this_line[j]
    #각 컬럼의 시그마 (값-평균)^2 계산 
    for j in range (1, how_many_champs_in_this_lane*how_many_properties_for_line+1) :
        if how_many_data_in_this_line[j-1] != 0 :
            for i in range (1, how_many_champs_in_this_lane) :
                if basicArray[i][j] != '?' :
                    temp[j-1] += math.pow((float(basicArray[i][j]) - float(average_of_each_line[j-1])), 2)
    #각 컬럼의 SDV계산 
    for j in range (0, how_many_champs_in_this_lane*how_many_properties_for_line) :
        if how_many_data_in_this_line[j] != 0 :
            standard_deviation_of_each_line[j] = math.sqrt(temp[j]/how_many_data_in_this_line[j])
    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/basicArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(basicArray): 
        csvWriter.writerow(basicArray[index])
    f.close() 
    
    
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    standardizedArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #print(standardizedArray[0].__len__())
    #앞쪽 인덱스가 세로, 뒤쪽 인덱스가 가로인듯 
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:             
                standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                standardizedArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                standardizedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                standardizedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                standardizedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                standardizedArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                if basicArray[i][j] == '?':
                    standardizedArray[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                if basicArray[i][j] == '?' :
                    standardizedArray[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1] 
                if basicArray[i][j] == '?' :
                    standardizedArray[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                if basicArray[i][j] == '?' :
                    standardizedArray[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                if basicArray[i][j] == '?' :
                    standardizedArray[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6:                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    standardizedArray[i][j] =  (float(basicArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                if basicArray[i][j] == '?' :
                    standardizedArray[i][j] ='?'
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/standardizedArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(standardizedArray): 
        csvWriter.writerow(standardizedArray[index])
    f.close() 
    
    
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    pickrateweightedArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #print(standardizedArray[0].__len__())
    #앞쪽 인덱스가 세로, 뒤쪽 인덱스가 가로인듯 
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                pickrateweightedArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                pickrateweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                pickrateweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                pickrateweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                pickrateweightedArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 * 상대 챔프의 등장 확률. 상대 챔프가 등장할 확률이 높으면 큰 의미를 가지고, 낮으면 작은 의미를 가짐. 나의 등장 확률은 전혀 영향 x
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?':
                    pickrateweightedArray[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?' :
                    pickrateweightedArray[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?' :
                    pickrateweightedArray[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?' :
                    pickrateweightedArray[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?' :
                    pickrateweightedArray[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6:                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        pickrateweightedArray[i][j] =  float(standardizedArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                if basicArray[i][j] == '?' :
                    pickrateweightedArray[i][j] ='?'
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/pickrateweightedArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(pickrateweightedArray): 
        csvWriter.writerow(pickrateweightedArray[index])
    f.close() 
    
    #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
    userweight = [100000*weight1, 100000*weight2, 100000*weight3, 100000*weight4, 100000*weight5, 100000*weight6]
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    userweightedArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                userweightedArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                userweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                userweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                userweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                userweightedArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[0]
                if basicArray[i][j] == '?':
                    userweightedArray[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[1]
                if basicArray[i][j] == '?' :
                    userweightedArray[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[2] 
                if basicArray[i][j] == '?' :
                    userweightedArray[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[3]
                if basicArray[i][j] == '?' :
                    userweightedArray[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[4]
                if basicArray[i][j] == '?' :
                    userweightedArray[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6 :                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    userweightedArray[i][j] =  pickrateweightedArray[i][j] * userweight[5]
                if basicArray[i][j] == '?' :
                    userweightedArray[i][j] ='?'
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/userweightedArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(userweightedArray): 
        csvWriter.writerow(userweightedArray[index])
    f.close() 
    
    
    
    
    
    #이 아래로는 사용자가 보기 위한 속성을 만드는 어레이
    #플랫에다가 픽률을 곱한 데이터를 뽑아낸다. 
    
    
    
    #위에서 표준화할때 썼던 변수 재활용 
   
    #평균을 구하기 위한 각 컬럼의 총합     
    total_amount_of_each_line=[[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #평균을 구하기 위한 각 컬럼의 요소수 
    how_many_data_in_this_line=[[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #각 컬럼의평균 
    average_of_each_line=[[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    '''
    #SDV 계산을 위한 (값-평균)^의 시그마가 저장되는 리스트 
    temp = [0]*(how_many_champs_in_this_lane*how_many_properties_for_line)
    #표준화를 위한 각 컬럼의 SDV
    standard_deviation_of_each_line = [0]*(how_many_champs_in_this_lane*how_many_properties_for_line)    
    '''
    
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    flatweightedArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    #print(basicArray[0].__len__())
    #앞쪽 인덱스가 세로, 뒤쪽 인덱스가 가로인듯 
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                flatweightedArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                flatweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                flatweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                flatweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                flatweightedArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 * 상대 챔프의 등장 확률. 상대 챔프가 등장할 확률이 높으면 큰 의미를 가지고, 낮으면 작은 의미를 가짐. 나의 등장 확률은 전혀 영향 x
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    
                    total_amount_of_each_line[i-1][0] += float(flatweightedArray[i][j])
                    how_many_data_in_this_line[i-1][0] += 1
                    '''
                    if i-1 == 1 :
                        print('더해진 값은 ', flatweightedArray[i][j])
                        print('현재 total_amount_of_each_line은 ', total_amount_of_each_line[i-1][0])
                        print('데이터 개수는 ', how_many_data_in_this_line[i-1][0])
                    '''
                if basicArray[i][j] == '?':
                    flatweightedArray[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    total_amount_of_each_line[i-1][1] += float(flatweightedArray[i][j])
                    how_many_data_in_this_line[i-1][1] += 1
                if basicArray[i][j] == '?' :
                    flatweightedArray[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    total_amount_of_each_line[i-1][2] += float(flatweightedArray[i][j])
                    how_many_data_in_this_line[i-1][2] += 1
                if basicArray[i][j] == '?' :
                    flatweightedArray[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    total_amount_of_each_line[i-1][3] += float(flatweightedArray[i][j])
                    how_many_data_in_this_line[i-1][3] += 1
                if basicArray[i][j] == '?' :
                    flatweightedArray[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    total_amount_of_each_line[i-1][4] += float(flatweightedArray[i][j])
                    how_many_data_in_this_line[i-1][4] += 1
                if basicArray[i][j] == '?' :
                    flatweightedArray[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6:                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    if lane == 'top' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                    if lane == 'jungle' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][8])
                    if lane == 'mid' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][9])
                    if lane == 'adc' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][10])
                    if lane == 'sup' :
                        flatweightedArray[i][j] =  float(basicArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][11])
                    if len(userproperties) >= 5:
                        total_amount_of_each_line[i-1][5] += float(flatweightedArray[i][j])
                        how_many_data_in_this_line[i-1][5] += 1
                    
                if basicArray[i][j] == '?' :
                    flatweightedArray[i][j] ='?'
                    
    #각 컬럼의 평균값 계산 
    for i in range (0, how_many_champs_in_this_lane) :
        for j in range (0, len(userproperties)) :
            if how_many_data_in_this_line[j] != 0 and how_many_data_in_this_line[i][j] != 0:
                average_of_each_line[i][j] = total_amount_of_each_line[i][j] / how_many_data_in_this_line[i][j]                
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/flatweightedArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(flatweightedArray): 
        csvWriter.writerow(flatweightedArray[index])
    f.close() 
    
    
    
    
    
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    wekaArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                wekaArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                wekaArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                wekaArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                wekaArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                wekaArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                wekaArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                wekaArray[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?':
                    wekaArray[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6 :                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray[i][j] ='?'
            #눈으로 보기 위한 속성들
            elif j>how_many_champs_in_this_lane*how_many_properties_for_line and j<=(how_many_champs_in_this_lane*6+len(userproperties)) and i>0 and i<=how_many_champs_in_this_lane : 
                #단순히 픽률을 곱해진 승률을 평균낸것(크기제한없음)
                #wekaArray[i][j] = average_of_each_line[i-1][j-(how_many_champs_in_this_lane*6+1)]
                #승률을 비중을 적용해서 평균낸것(최소값 0, 최대값 100)
                #100만 나누면 되는데 weka에서 미치는 영향 최소화하기위해 일부러 10000을 더 나눴다. 
                wekaArray[i][j] = average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)] * float(how_many_data_in_this_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)]) / 100 /10000
                
                #if i-1 == 1 and j-(how_many_champs_in_this_lane*6+1) ==1 :
                #    print(total_amount_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)])
                #    print(how_many_data_in_this_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)])
                #    print(average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)])
                
                
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/wekaArray_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(wekaArray): 
        csvWriter.writerow(wekaArray[index])
    f.close() 
    
    
    
    #승률만 상대챔프에대한승률*픽률비중이 아닌 전체 승률로 바꿔줌.
    
    #각 컬럼의 평균값 계산 
    for i in range (0, how_many_champs_in_this_lane) :
        for j in range (0, len(userproperties)) :
            if how_many_data_in_this_line[j] != 0 and j == 0:
                if lane == 'top' :
                    average_of_each_line[i][j] = float(champ_data[champs_in_this_lane[i]][12])
                if lane == 'jungle' :
                    average_of_each_line[i][j] = float(champ_data[champs_in_this_lane[i]][13]) 
                if lane == 'mid' :
                    average_of_each_line[i][j] = float(champ_data[champs_in_this_lane[i]][14])
                if lane == 'adc' :
                    average_of_each_line[i][j] = float(champ_data[champs_in_this_lane[i]][15])
                if lane == 'sup' :
                    average_of_each_line[i][j] = float(champ_data[champs_in_this_lane[i]][16])
    
    
    #wekaArray와 wekaArray2의 차이는?
    #1은 보기위한 지표에 승률*픽률평균이 들어가있고 2는 그냥 오피지지에서 긁어온 평균이 들어가있는듯.
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수 
    wekaArray2= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:  
                wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:   
                if lane == 'sup':
                    wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'킬관여율차이'            
                else :
                    wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'             
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:              
                if lane == 'sup':
                    wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'분당cs'
                else :    
                    wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1 and how_many_properties_for_line>=4:               
                wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1 and how_many_properties_for_line>=5:             
                wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1 and how_many_properties_for_line>=6:            
                wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= how_many_properties_for_line*how_many_champs_in_this_lane and j< how_many_properties_for_line*how_many_champs_in_this_lane+len(userproperties) :
                wekaArray2[i][j+1] = userproperties[j-how_many_properties_for_line*how_many_champs_in_this_lane]
                #print(j-6*how_many_champs_in_this_lane)      
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                wekaArray2[i+1][j] = champ_data[champs_in_this_lane[i]][0]        
            #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                wekaArray2[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                wekaArray2[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                wekaArray2[i][j] = '챔프이름'
            
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여     
            #how_many_champs_in_this_lane 일때 헤카림 
            #승률 
            if j>0 and j<=(how_many_champs_in_this_lane) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    #print('index i 는 ',i, 'index j는 ', j )
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?':
                    wekaArray2[i][j]= '?'
            #솔로킬 
            elif j>how_many_champs_in_this_lane and j<=(how_many_champs_in_this_lane*2) and i>0 and i<=how_many_champs_in_this_lane :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray2[i][j] = '?'
            #씨에스 
            elif j>how_many_champs_in_this_lane*2 and j<=(how_many_champs_in_this_lane*3) and i>0 and i<=how_many_champs_in_this_lane :
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray2[i][j] = '?'
            #포탑 
            elif j>how_many_champs_in_this_lane*3 and j<=(how_many_champs_in_this_lane*4) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=4 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray2[i][j] = '?'
            #딜 
            elif j>how_many_champs_in_this_lane*4 and j<=(how_many_champs_in_this_lane*5) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=5 :                
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray2[i][j] = '?'
            #킬관여
            elif j>how_many_champs_in_this_lane*5 and j<=(how_many_champs_in_this_lane*6) and i>0 and i<=how_many_champs_in_this_lane and how_many_properties_for_line>=6 :                  
                if basicArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0 :
                    wekaArray2[i][j] =  userweightedArray[i][j]
                if basicArray[i][j] == '?' :
                    wekaArray2[i][j] ='?'
            #눈으로 보기 위한 속성들
            elif j>how_many_champs_in_this_lane*how_many_properties_for_line and j<=(how_many_champs_in_this_lane*how_many_properties_for_line+len(userproperties)) and i>0 and i<=how_many_champs_in_this_lane : 
                #단순히 픽률을 곱해진 승률을 평균낸것(크기제한없음)
                #wekaArray2[i][j] = average_of_each_line[i-1][j-(how_many_champs_in_this_lane*6+1)]
                #승률을 비중을 적용해서 평균낸것(최소값 0, 최대값 100)
                #100만 나누면 되는데 weka에서 미치는 영향 최소화하기위해 일부러 10000을 더 나눴다. 
                
                
                if j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) != 0 and j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) != 2:
                    wekaArray2[i][j] = average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)] * float(how_many_data_in_this_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)]) / 100 /10000
                elif (j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) == 0 or j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) ==2) and average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)] !=0:
                    wekaArray2[i][j] = average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)] 
                elif (j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) == 0 or j-(how_many_champs_in_this_lane*how_many_properties_for_line+1) ==2) and average_of_each_line[i-1][j-(how_many_champs_in_this_lane*how_many_properties_for_line+1)] ==0:
                    wekaArray2[i][j] = '?'
                
                
                #if i-1 == 1 and j-(how_many_champs_in_this_lane*6+1) ==1 :
                #    print(total_amount_of_each_line[i-1][j-(how_many_champs_in_this_lane*6+1)])
                #    print(how_many_data_in_this_line[i-1][j-(how_many_champs_in_this_lane*6+1)])
                #    print(average_of_each_line[i-1][j-(how_many_champs_in_this_lane*6+1)])
                
                
                    
    #파일쓰기
    filepath = '/Users/HyeonWoo/Google 드라이브/LOLcoach/data_from_python/wekaArray2_' + lane + '.csv'
    f = open(filepath, 'w', newline='', encoding="utf-8")
    csvWriter = csv.writer(f)
    for index, i in enumerate(wekaArray2): 
        csvWriter.writerow(wekaArray2[index])
    f.close() 
    
    
        
    '''
    #앞쪽이 가로 개수, 뒷쪽이 세로 개수     
    total_amount_of_weighted_data = [[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    total_number_of_weighted_data = [[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    average_of_weighted_data = [[0]*(len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]
    for i in range (1, how_many_champs_in_this_lane+1):
        for j in range (1, how_many_champs_in_this_lane) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][0] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][0] += 1
        for j in range (how_many_champs_in_this_lane, how_many_champs_in_this_lane*2) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][1] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][1] += 1
        for j in range (how_many_champs_in_this_lane*2, how_many_champs_in_this_lane*3) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][2] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][2] += 1
        for j in range (how_many_champs_in_this_lane*3, how_many_champs_in_this_lane*4) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][3] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][3] += 1
        for j in range (how_many_champs_in_this_lane*4, how_many_champs_in_this_lane*5) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][4] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][4] += 1
        for j in range (how_many_champs_in_this_lane*5, how_many_champs_in_this_lane*6) : 
            if weightedArray[i][j] != '0' and weightedArray[i][j] != '?' :
                print(i, ',', j)
                total_amount_of_weighted_data[i-1][5] += weightedArray[i][j]
                total_number_of_weighted_data[i-1][5] += 1
    for j in range (0, len(userproperties)) :
        for i in range (0, how_many_champs_in_this_lane) :
            print(i, ',', j)
            #앞쪽이 세로, 뒤쪽이 가로 
            average_of_weighted_data[i][j] = total_amount_of_weighted_data[i][j] / total_number_of_weighted_data[i][j]
    
    #비중이 곱해지지 않은 행렬을 스케일링         
    zscoreArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]   
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:
               
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1:
               
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                zscoreArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
               
            
            
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                zscoreArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                
                #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                zscoreArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                zscoreArray[i][j] = '챔프이름'
                
            elif i>0 and j>0 and j <= how_many_champs_in_this_lane*6:
                if newArray[i][j] != '?' and standard_deviation_of_each_line[j-1] != 0:
                    zscoreArray[i][j] = (float(newArray[i][j]) - average_of_each_line[j-1]) / standard_deviation_of_each_line[j-1]
                    #if j==1 :
                    #    print(newArray[i][j])
                    #    print(average_of_each_line[j-1])
                    #    print(standard_deviation_of_each_line[j-1])
                if newArray[i][j] == '?' :
                    zscoreArray[i][j] = '?'
    
    #스케일링된 행렬에 비중을 곱함
    
    #스케일링된 zscore에 챔프 비중을 곱함. 
    newweightedArray = [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties)) for row in range(how_many_champs_in_this_lane+1)]   
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1+len(userproperties))  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:
                
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:
               
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:
                
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1:
                
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1:
               
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1:
                
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            elif i == 0 and j>= 6*how_many_champs_in_this_lane and j< 6*how_many_champs_in_this_lane+len(userproperties) :
                newweightedArray[i][j+1] = userproperties[j-6*how_many_champs_in_this_lane]
                
            
            
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                newweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                
                #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                newweightedArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                newweightedArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                newweightedArray[i][j] = '챔프이름'
            
            #승률     
            elif i>0 and j>0 and j<how_many_champs_in_this_lane and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
            #솔로킬     
            elif i>0 and j>=how_many_champs_in_this_lane and j<how_many_champs_in_this_lane*2 and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
            #씨에스 
            elif i>0 and j>=how_many_champs_in_this_lane*2 and j<how_many_champs_in_this_lane*3 and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
            #포탑 
            elif i>0 and j>=how_many_champs_in_this_lane*3 and j<how_many_champs_in_this_lane*4 and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
            #딜량   
            elif i>0 and j>=how_many_champs_in_this_lane*4 and j<how_many_champs_in_this_lane*5 and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])*10000
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
            #킬관여    
            elif i>0 and j>=how_many_champs_in_this_lane*5 and j<how_many_champs_in_this_lane*6 and standard_deviation_of_each_line[j-1] != 0:
                if zscoreArray[i][j] != '?' :
                    newweightedArray[i][j] = float(zscoreArray[i][j]) * float(champ_data[champs_in_this_lane[(j-1)%how_many_champs_in_this_lane]][7])
                if zscoreArray[i][j] == '?' :
                    newweightedArray[i][j]= '?'
        
    #비중이 곱해진 행렬을 스케일링 -> 의미없음 
    
    zscoreArray= [[0]*(how_many_champs_in_this_lane*how_many_properties_for_line+1) for row in range(how_many_champs_in_this_lane+1)]   
    for i in range (0, how_many_champs_in_this_lane+1) :
        for j in range(0, how_many_champs_in_this_lane*how_many_properties_for_line+1)  :
            
            #가로줄 이름 넣음 
            #승률, 솔로킬, 씨에스, 포탑, 딜, 킬관여 
            if i == 0  and j != 0 and j<how_many_champs_in_this_lane:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'   
            elif i == 0  and j>= how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*2-1:
               
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-how_many_champs_in_this_lane]][0]+'솔로킬'
            elif i == 0  and j>= 2*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*3-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-2*how_many_champs_in_this_lane]][0]+'씨에스'
            elif i == 0  and j>= 3*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*4-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-3*how_many_champs_in_this_lane]][0]+'포탑'
            elif i == 0  and j>= 4*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*5-1:
               
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-4*how_many_champs_in_this_lane]][0]+'딜'
            elif i == 0  and j>= 5*how_many_champs_in_this_lane  and j<=how_many_champs_in_this_lane*6-1:
                
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j-5*how_many_champs_in_this_lane]][0]+'킬관여'
            
            
            #세로줄 이름 넣음 
            elif j == 0 and i!= 0 and i<how_many_champs_in_this_lane :
                zscoreArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                
                #위아래 가렌
            elif i==0 and j ==0 and j<how_many_champs_in_this_lane and i<how_many_champs_in_this_lane:
                zscoreArray[i][j+1] = champ_data[champs_in_this_lane[j]][0]+'승률'
                zscoreArray[i+1][j] = champ_data[champs_in_this_lane[i]][0]
                zscoreArray[i][j] = '챔프이름'
                
            elif i>0 and j>0 :
                if weightedArray[i][j] != '?' and standard_deviation_of_each_line_for_weightedArray[j-1] != 0:
                    zscoreArray[i][j] = (float(weightedArray[i][j]) - average_of_each_line_for_weightedArray[j-1]) / standard_deviation_of_each_line_for_weightedArray[j-1]
                    if j==3 :
                        print(weightedArray[i][j])
                        print(average_of_each_line_for_weightedArray[j-1])
                        print(standard_deviation_of_each_line_for_weightedArray[j-1])
                if weightedArray[i][j] == '?' :
                    zscoreArray[i][j] = '?'
    '''
         
                     
                
         
    
                
                
    return wekaArray2

