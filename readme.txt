학번 : 201911291
이름 : 허준호
학과 : 컴퓨터공학부
사용 운영체제 : MacOS

Visual Studio Code와 Terminal(iterm2)을 이용하여 실습했습니다!

[유의사항]
이번 과제에 한글 깨짐 방지를 위해서 제가 제출한 파일의 각 문제 .py 파일마다 추가된 구문은 아래와 같습니다!
plt.rcParams['font.family'] = 'AppleGothic'

해당 구문은 MacOS에 기본으로 내장되어 있는 'AppleGothic' 서체를 가져와 한글 깨짐을 방지합니다.
그러나, 이 구문은 Windows 환경에서는 동작하지 않을 수 있습니다.
따라서, Windows에서 실행 시 한글이 깨져 보이신다면 위 구문을 아래처럼 수정하시면 될 것 같습니다!

plt.rcParams['font.family'] = 'Malign Gothic'
(위 구문은 교수님께서 이캠퍼스 공지사항에 올리신 샘플 코드의 일부와 같은 구문입니다! MacOS에서는 위 구문이 동작하지 않아서 다른 대안을 사용하게 되었습니다.)