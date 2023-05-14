#Question1

import csv
import matplotlib.pyplot as plt
import numpy
from matplotlib.gridspec import GridSpec

def for_loop_all(data, avg):
    for row in data:
        if(row[2] != ''):
            avg.append(float(row[2]))

def making_diff_data(all, avg, diff):
    i = 0
    for all_info in all:
        diff.append(avg[i] - all_info) 
        i = i+1


def main():
    #한글 깨짐 문제를 해결하기 위해 넣었던 구문..(애플 고딕을 사용할 것임)
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False

    month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    major_ticks = [i for i in range (-5, 31, 5)]
    minor_ticks = [i for i in range (-5, 31, 1)]
    major_ticks_diff = [i for i in range (-3, 10, 3)]
    minor_ticks_diff = [i for i in range (-3, 10, 1)]

    #csv 파일을 오픈하여 file descriptor에 저장 (인코딩 방식은 EUC-KR)
    f1 = open('whole_monthAvg.csv', 'r', encoding='EUC-KR')
    f2 = open('seoul_monthAvg.csv', 'r', encoding='EUC-KR')
    f3 = open('busan_monthAvg.csv', 'r', encoding='EUC-KR')
    f4 = open('dajeon_monthAvg.csv', 'r', encoding='EUC-KR')
    f5 = open('jeju_monthAvg.csv', 'r', encoding='EUC-KR')

    #data를 가지고 온다
    data = csv.reader(f1)
    data2 = csv.reader(f2)
    data3 = csv.reader(f3)
    data4 = csv.reader(f4)
    data5 = csv.reader(f5)

    #다음 줄로 데이터를 옮긴다
    next(data)
    next(data2)
    next(data3)
    next(data4)
    next(data5)

    #데이터를 저장할 리스트르 정의한다
    whole_mAvg = []
    seoul_monthAvg = []
    busan_monthAvg = []
    daejon_monthAvg = []
    jeju_monthAvg = []

    #리스트에 대표 데이터들 저장
    for_loop_all(data, whole_mAvg)
    for_loop_all(data2, seoul_monthAvg)
    for_loop_all(data3, busan_monthAvg)
    for_loop_all(data4, daejon_monthAvg)
    for_loop_all(data5, jeju_monthAvg)

    seoul_all_diff=[]
    busan_all_diff=[]
    daejon_all_diff=[]
    jeju_all_diff=[]

    #(해당지역-전국기온) 데이터 만들기
    making_diff_data(whole_mAvg, seoul_monthAvg, seoul_all_diff)
    making_diff_data(whole_mAvg, busan_monthAvg, busan_all_diff)
    making_diff_data(whole_mAvg, daejon_monthAvg, daejon_all_diff)
    making_diff_data(whole_mAvg, jeju_monthAvg, jeju_all_diff)

    fig = plt.figure(figsize=(10,6))

    #GridSpec을 이용하여 레이아웃을 지정한다
    gs = GridSpec(3, 2, figure=fig, width_ratios=[1, 1], height_ratios=[2, 1, 1])

    #레이아웃에다가 subplot들을 그린다 (좌표값 이용)
    ax1 = fig.add_subplot(gs[0, 0:])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[2, 0])
    ax5 = fig.add_subplot(gs[2, 1])

    #subplot별로 그래프 그리기
    ax1.plot(month_list, whole_mAvg, 'black', label='all')
    ax1.plot(month_list, seoul_monthAvg, 'or', label='seoul')
    ax1.plot(month_list, busan_monthAvg, 'og', label='busan')
    ax1.plot(month_list, daejon_monthAvg, 'ob', label='daejon')
    ax1.plot(month_list, jeju_monthAvg, 'om', label='jeju')
    ax1.legend(loc='best', ncol=2)
    ax1.set_title('Average Temperature Datas of 2022')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Temperature(°C)')
    ax1.set_xticks(month_list)
    ax1.set_yticks(major_ticks)
    ax1.set_yticks(minor_ticks, minor=True)

    ax2.plot(month_list, seoul_all_diff, 'red', marker='o')
    ax2.set_title('Average Difference (Seoul-All)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Temperature(°C)')
    ax2.set_xticks(month_list)
    ax2.set_yticks(major_ticks_diff)
    ax2.set_yticks(minor_ticks_diff, minor=True)
    ax2.text(4,6, 'Mean of Data: {0:.1f}'.format(numpy.mean(seoul_all_diff)))

    ax3.plot(month_list, busan_all_diff, 'green', marker='o')
    ax3.set_title('Average Difference (Busan-All)')
    ax3.set_xlabel('Month')
    ax3.set_ylabel('Temperature(°C)')
    ax3.set_xticks(month_list)
    ax3.set_yticks(major_ticks_diff)
    ax3.set_yticks(minor_ticks_diff, minor=True)
    ax3.text(4,6, 'Mean of Data: {0:.1f}'.format(numpy.mean(busan_all_diff)))

    ax4.plot(month_list, daejon_all_diff, 'blue', marker='o')
    ax4.set_title('Average Difference (Daejon-All)')
    ax4.set_xlabel('Month')
    ax4.set_ylabel('Temperature(°C)')
    ax4.set_xticks(month_list)
    ax4.set_yticks(major_ticks_diff)
    ax4.set_yticks(minor_ticks_diff, minor=True)
    ax4.text(4,6, 'Mean of Data: {0:.1f}'.format(numpy.mean(daejon_all_diff)))

    ax5.plot(month_list, jeju_all_diff, 'magenta', marker='o')
    ax5.set_title('Average Difference (Jeju-All)')
    ax5.set_xlabel('Month')
    ax5.set_ylabel('Temperature(°C)')
    ax5.set_xticks(month_list)
    ax5.set_yticks(major_ticks_diff)
    ax5.set_yticks(minor_ticks_diff, minor=True)
    ax5.text(4,6, 'Mean of Data: {0:.1f}'.format(numpy.mean(jeju_all_diff)))

    plt.tight_layout()
    plt.show()

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

if __name__ == '__main__':
    main()