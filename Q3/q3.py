#Question 3

import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

def main():
    #한글 깨짐 문제를 해결하기 위해 넣었던 구문..(애플 고딕을 사용할 것임)
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False

    f = open("jeju_population_total.csv", "r", encoding="utf-8")

    data = csv.reader(f)
    next(data)

    Jeju_info={}
    Jeju_info['2002'] = [0,0]
    Jeju_info['2006'] = [0,0]
    Jeju_info['2010'] = [0,0]
    Jeju_info['2014'] = [0,0]
    Jeju_info['2018'] = [0,0]
    Jeju_info['2022'] = [0,0]

    #row[2]가 남자, row[3]이 여자 Data
    for row in data:
        if row[0] in Jeju_info.keys():
            Jeju_info[row[0]][0] = int(row[2])
            Jeju_info[row[0]][1] = int(row[3])
    
    x_labels = list(Jeju_info.keys())
    x = np.array(range(len(x_labels)))
    
    y_labels_men = []
    y_labels_women = []

    for keys in x_labels:
        y_labels_men.append(int(Jeju_info[keys][0]))
        y_labels_women.append(int(Jeju_info[keys][1]))
    
    plt.figure(figsize = (10,6))

    #각 bar의 width를 정한다
    barWidth = 0.3
    plt.bar(x, y_labels_men, alpha=0.4, align='edge', width=barWidth, label="남성")
    x = x+barWidth
    plt.bar(x, y_labels_women, alpha=0.4, align='edge', width=barWidth, label="여성")

    #x,y label 값을 설정하고, show()
    plt.xlabel("Year (단위: 년)")
    plt.ylabel("Value (단위: 명)")
    plt.title("제주도 내 연도별 남녀 인구 분포")
    plt.xticks(np.arange(barWidth, 6, 1), x_labels)

    plt.legend()
    plt.show()

    f.close()
            
    
if __name__ == '__main__':
    main()