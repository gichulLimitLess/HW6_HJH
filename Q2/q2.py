#Question2

import random
import csv
import matplotlib.pyplot as plt
import numpy
from matplotlib.gridspec import GridSpec

#1~6 사이의 랜덤 숫자를 만들어, 100번, 1000번, 10000번, 100000번
#시행 결과를 csv 파일로 저장
#시행별 데이터를 읽어와 1~6 숫자에 대해 히스토그램으로 시각화
#주사위 시뮬레이션 결과에 대한 분석결과 설명

def calc_Dice(Dict, count):
    for i in range(0, count):
        result = random.randrange(1,7)
        Dict[result] = Dict[result] + 1

def write_information(f, count, Dict):
    f.write(str(count)+ '\n')
    for i in range(1, 7):
        #맨 마지막 줄을 쓰고 있는 중이라면.. 개행문자 필요 없음
        if count == 100000 and i == 6:
            f.write(str(i) + ',' + str(Dict.get(i)))
            break
        else:
            f.write(str(i) + ',' + str(Dict.get(i)) + '\n')

def make_graph_information(reader, list, count):
    i = 0
    for row in reader:
        if i == 6:
            break
        if row[0] == str(count):
            continue
        else:
            list.append(int(row[1]))
            i = i + 1
            if i == 6 and count == 100000:
                break

def add_value_label(ax, x_list, y_list):
    for i in range(1, len(x_list)+1):
        ax.text(i, y_list[i-1], y_list[i-1], ha="center")


def main():
    #한글 깨짐 문제를 해결하기 위해 넣었던 구문..(애플 고딕을 사용할 것임)
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False

    f = open("dice_result.csv", "w", encoding="utf-8")

    Dice_info={}
    Dice_info[1] = 0
    Dice_info[2] = 0
    Dice_info[3] = 0
    Dice_info[4] = 0
    Dice_info[5] = 0
    Dice_info[6] = 0

    #랜덤 함수 돌리고, .csv 파일 생성
    calc_Dice(Dice_info, 100)
    write_information(f, 100, Dice_info)

    calc_Dice(Dice_info, 1000)
    write_information(f, 1000, Dice_info)

    calc_Dice(Dice_info, 10000)
    write_information(f, 10000, Dice_info)

    calc_Dice(Dice_info, 100000)
    write_information(f, 100000, Dice_info)

    f.close()

    one_to_six=[i for i in range(1,7,1)]
    dice_100=[]
    dice_1000=[]
    dice_10000=[]
    dice_100000=[]

    #적었던 csv 파일 다시 읽기 모드로 open
    f2 = open("dice_result.csv", "r", encoding="utf-8")
    reader = csv.reader(f2)

    make_graph_information(reader, dice_100, 100)
    make_graph_information(reader, dice_1000, 1000)
    make_graph_information(reader, dice_10000, 10000)
    make_graph_information(reader, dice_100000, 100000)

    fig = plt.figure(figsize=(10,6))

    #GridSpec을 이용하여 레이아웃을 지정한다
    gs = GridSpec(2, 2, figure=fig, width_ratios=[1, 1], height_ratios=[1, 1])

    #레이아웃에다가 subplot들을 그린다 (좌표값 이용)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    ax1.set_title('100 times')
    ax1.set_xlabel('Result')
    ax1.set_ylabel('Frequency')
    ax1.bar(one_to_six, dice_100, color='red')
    add_value_label(ax1, one_to_six, dice_100)

    ax2.set_title('1000 times')
    ax2.set_xlabel('Result')
    ax2.set_ylabel('Frequency')
    ax2.bar(one_to_six, dice_1000, color='green')
    add_value_label(ax2, one_to_six, dice_1000)

    ax3.set_title('10000 times')
    ax3.set_xlabel('Result')
    ax3.set_ylabel('Frequency')
    ax3.bar(one_to_six, dice_10000, color='blue')
    add_value_label(ax3, one_to_six, dice_10000)

    ax4.set_title('100000 times')
    ax4.set_xlabel('Result')
    ax4.bar(one_to_six, dice_100000, color='magenta')
    add_value_label(ax4, one_to_six, dice_100000)

    
    plt.tight_layout()
    plt.show()

    f2.close()
    
if __name__ == '__main__':
    main()