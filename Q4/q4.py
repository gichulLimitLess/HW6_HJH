#Question 4

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import csv

def main():
    #한글 깨짐 문제를 해결하기 위해 넣었던 구문..(애플 고딕을 사용할 것임)
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False

    indicies = [i for i in range (0,30,1)]

    datafile = open('subway_using_perTime.csv', 'r', encoding='utf-8')
    data = csv.reader(datafile)
    #row[3]: 역 명칭 / row[10]: 7시~8시              / row[12]: 8시~9시  
    #                row[10]: 승차    row[11]: 하차    row[12]: 승차     row[13]: 하차

    #2줄을 건너뛰어야 우리가 원하는 데이터가 나온다
    next(data)
    next(data)

    bar_titles = ['출근시간 최대 승차역 30개', '출근시간 최대 하차역 30개', '출근시간 최대 승하차역 30개']
    dic_riding = {}
    dic_quit = {}
    dic_ridingNquit = {}

    #우선 딕셔너리의 각 키에 해당하는 값을 모두 0으로 초기화한다
    for row1 in data:
        dic_riding[row1[3]]=0
        dic_quit[row1[3]]=0
        dic_ridingNquit[row1[3]]=0
    
    #file pointer를 다시 초기로 돌려서 다시 row를 뒤질 수 있도록 만든다
    datafile.seek(0)
    next(data)
    next(data)
    
    #0으로 초기화 했으면 더할 수 있으므로, 연산을 수행한다
    for row in data:
        dic_riding[row[3]]=dic_riding[row[3]] + int(row[10]) + int(row[12])
        dic_quit[row[3]]=dic_quit[row[3]] + int(row[11]) + int(row[13])
        dic_ridingNquit[row[3]]=dic_ridingNquit[row[3]] + int(row[10]) + int(row[11]) + int(row[12]) + int(row[13])
    
    #위에서 다 수행했으면, 각 dictionary에 적절한 정보들이 들어갔을 것이다.
    #이제 이를 value값을 기준으로 정렬하면 데이터 set은 끝난다
    sorted_riding = dict(sorted(dic_riding.items(), key=lambda x:x[1], reverse=True))
    sorted_quit = dict(sorted(dic_quit.items(), key=lambda x:x[1], reverse=True))
    sorted_ridingNquit = dict(sorted(dic_ridingNquit.items(), key=lambda x:x[1], reverse=True))

    #각 내림차순으로 정렬된 딕셔너리에서 상위 30개씩 뽑아낸다
    sorted_riding_30_name = list(sorted_riding.keys())[:30]
    sorted_riding_30_values = list(sorted_riding.values())[:30]
    sorted_quit_30_name = list(sorted_quit.keys())[:30]
    sorted_quit_30_values = list(sorted_quit.values())[:30]
    sorted_ridingNquit_30_name = list(sorted_ridingNquit.keys())[:30]
    sorted_ridingNquit_30_values = list(sorted_ridingNquit.values())[:30]



    #보기 편하게 하기 위해 숫자의 단위를 줄인다
    labels_1 = []
    for values in sorted_riding_30_values:
        labels_1.append(values/10000)
    
    labels_2 = []
    for values2 in sorted_quit_30_values:
        labels_2.append(values2/10000)
    
    labels_3 = []
    for values3 in sorted_ridingNquit_30_values:
        labels_3.append(values3/10000)

    #그래프 그리기 시작하는 영역
    fig = plt.figure(figsize=(8,12))

    #GridSpec을 이용하여 레이아웃을 지정한다
    gs = GridSpec(3, 1, figure=fig, height_ratios=[1,1,1])

    #레이아웃에다가 subplot들을 그린다 (좌표값 이용)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])
    
    #subplot별로 그래프 그리기
    ax1.set_title(bar_titles[0] + ' (x축: 역명)')
    ax1.set_ylabel('승차객 수 (단위: 만 명)')
    ax1.bar(sorted_riding_30_name, labels_1, alpha=0.5, color='red')
    ax1.set_xticks(indicies, sorted_riding_30_name, rotation=90)

    #subplot별로 그래프 그리기
    ax2.set_title(bar_titles[1] + ' (x축: 역명)')
    ax2.set_ylabel('하차객 수 (단위: 만 명)')
    ax2.bar(sorted_quit_30_name, labels_2, alpha=0.5, color='green')
    ax2.set_xticks(indicies, sorted_quit_30_name, rotation=90)

    #subplot별로 그래프 그리기
    ax3.set_title(bar_titles[2] + ' (x축: 역명)')
    ax3.set_ylabel('승하차객 수 (단위: 만 명)')
    ax3.bar(sorted_ridingNquit_30_name, labels_3, alpha=0.5, color='blue')
    ax3.set_xticks(indicies, sorted_ridingNquit_30_name, rotation=90)

    plt.tight_layout()
    plt.show()
        
if __name__=="__main__":
    main()