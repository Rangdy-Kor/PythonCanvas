import turtle as t  #터틀 그래픽 모듈 불러오기

def loading() :  #로딩 함수 지정
    t.clear()
    t.home()
    t.speed(0)  #로딩 기본 세팅
    t.ht()
    t.up()
    t.seth(90)
    t.fd(100)
    t.bgcolor('black')
    t.color('green')

    t.goto(0, 50)  #로딩 화면
    t.write(f"로딩 중...", False, 'center', ('맑은 고딕', 30, 'bold'))
    t.seth(270)
    t.fd(80)
    t.write(f"Loading...", False, 'center', ('Arial', 20, 'bold'))

loading()

t.title("파이썬 캔버스(Python Canvas) - ver 0.10 +")  #타이틀 변경
from keyboard import *  #keyboard 모듈 불러오기

t.reset()


hide = 0
a = 0


t.shape("classic")  #초기 설정
t.ht()
t.up()
t.lt(90)
t.speed(0)

t.fd(100)  #메인 화면 설정
t.speed(0)
t.bgcolor('bisque')
t.color('white')
t.write("Python Canvas", False, 'center', ('Gabriola', 100, 'bold'))
t.seth(270)
t.fd(80)
t.color('silver')
t.write("ver 0.10 + Alpha", False, 'center', ('NanumSquareRound', 30, 'bold'))
t.home()
t.seth(270)
t.fd(200)
t.color('pink')
t.write("Start to press 'k'...", False, 'center', ('NanumBarunGothic', 30, 'italic'))
while True :  #k와 Esc 감지
    if is_pressed('k') :
        break
    if is_pressed('Esc') :
        t.bye()

loading()  #로딩 화면

from time import *  #time 모듈 불러오기

def blue_screen(time) :  #종료 화면
    t.reset() 
    t.speed(0)
    t.ht()
    t.bgcolor('#2067B2')
    t.color('#FFFFFF')
    t.up()
    t.seth(90)
    t.fd(130)
    t.seth(180)
    t.fd(250)
    t.write(":(", False, 'left', ("맑은 고딕", 100, 'normal'))
    t.seth(270)
    t.fd(40)
    t.write("프로그램을 종료합니다.", False, 'left', ('맑은 고딕', 20, 'normal'))
    t.fd(40)
    t.write("Eixt the program.", False, 'left', ('Arial', 20, 'normal'))
    sleep(time)
    t.bye()

def real_bluescreen() :  #이스터에그 블루스크린
    t.reset() 
    t.speed(0)
    t.ht()
    t.bgcolor('#2067B2')
    t.color('#FFFFFF')
    t.up()
    t.seth(90)
    t.fd(130)
    t.seth(180)
    t.fd(250)
    t.write(":)", False, 'left', ("맑은 고딕", 100, 'normal'))
    t.seth(270)
    t.fd(100)
    t.write('''이스터 에그 보안에 문제가 발생하여 \nㅋㅋㅋ해야 합니다. \n대체 어떻게 찾으신 거죠?''', False, 'left', ('굴림', 20, 'bold'))
    t.fd(110)
    t.write("Easter egg security ran into a problem and \nneeds to lol. \nHow the heck did you find it?", False, 'left', ('Comic Sans MS', 20, 'normal'))
    t.fd(80)
    t.write("Esc를 눌러 리셋하기.", False, 'left', ("맑은 고딕", 20, 'normal'))
    t.fd(30)
    t.write("Reset to press Escape.", False, 'left', ('Arial', 20, 'normal'))
    while True :
        if is_pressed('Escape') :
            break
    t.reset()
    t.bgcolor('white')
    
def move(seth, speed) :  #move 함수 지정
    t.speed(0)
    t.seth(seth)
    t.speed(6)
    t.fd(speed)

def color(color) :
    t.color(color)

def bgcolor(bgcolor) :
    t.bgcolor(bgcolor)

def okp(de, key) :  #okp 함수 지정
    t.onkeypress(de, key)

def w() :
    move(90, 10)

def s() :
    move(270, 10)
    
def a() :
    move(180, 10)

def d() :
    move(0, 10)

def shape_stamp() :  #도형 삽입
    shape_stamp = int(t.numinput('system', '삽입하려는 도형의 번호를 입력하십시오.', 0, minval = 0))
    shape_size = t.numinput('system', '삽입하려는 도형의 반지름, 혹은 한 변의 길이의 절반을 입력하십시오.', 25, minval = 1)
    t.speed(0)
    
    if shape_stamp == 0 :  #원 그리기
        t.circle(shape_size)
    else :  #기타 도형 그리기
        t.up()
        t.seth(90)
        t.fd(shape_size)
        t.seth(180)
        t.fd(shape_size)
        t.seth(270)
        t.down()
        for i in range(0, shape_stamp+1) :
            t.fd(shape_size*2)
            t.lt(360/shape_stamp)
    t.speed(6)
    t.listen()
                
def stamp() :  #도장 찍기
    tc = t.stamp()

def write() :  #글자 삽입
    font = t.textinput("system", "적용할 폰트명를 입력하세요 ----> ")
    text = t.textinput("system", "작성할 글자를 입력하세요 ----> ")
    t.write(text, False, "center", (font,20,"normal"))
    t.listen()

def undo() :  #undo는 4번 해줘야 실행 취소 효과가 있다. 
    t.undo()
    t.undo()
    t.undo()
    t.undo()

def clear() :
    t.clear()
    
def shape() :
    sha = t.textinput('sytstem', '변경할 모양을 입력하세요 \nex)circle, classic, turtle...')
    t.shape(sha)
    t.listen()

def title() :
    title_name = t.textinput('system', '변경할 창의 이름을 입력하세요')
    t.title(title_name)
    t.listen()

def up() :
    t.up()

def down() :
    t.down()

def plus() :  #pensize 늘리기
    global pensize
    if pensize < 100 :  
        pensize += 1
        t.pensize(pensize)

def minus() :  #pensize 줄이기
    global pensize
    if pensize > 1 :
        pensize -=1
        t.pensize(pensize)

def hide() :  #포인터 숨기기
    global hide
    if hide == 0 :
        hide = 1
        t.ht()
    if hide == 1 :
        hide = 0
        t.st()

def home() :  #중앙으로 이동(home)
    t.up()
    t.speed(0)
    t.home()
    t.speed(6)
    t.down()

def helping() :  #도움말(업데이트 필요)
    print('''
                〈파이썬 캔버스 ver 0.10 + 사용 설명서 - 한국어〉

WSAD를 이용해 선을 그을 수 있습니다.

숫자 키를 눌러 색상을 변경 할 수 있습니다. 0번이 검정색입니다.

숫자 키에 쉬프트를 같이 누르면 배경 색상을 변경 할 수 있습니다. 

텍스트 작성은 t를 눌러 사용 할 수 있습니다. 처음에는 font를 입력하는 창이 나오고
그 다음에 문자 작성 창이 나올 것입니다.

e를 눌러 커서의 모양을 바꿀 수 있습니다.

F5를 눌러 창의 이름을 변경 할 수 있습니다.

BackSpace를 눌러 실행 취소 할 수 있습니다(다시 실행은 안 됩니다).

Delete를 눌러 캔버스의 모든 그림을 지울 수 있습니다.

Home을 눌러 커서를 처음 위치로 돌아가게끔 할 수 있습니다.

Enter를 눌러 커서의 도장을 찍을 수 있습니다.

?를 눌러 지금 보고 계시는 사용 설명서를 볼 수 있습니다.

Esc를 눌러 명령어 창을 펼칠 수 있습니다.
명령어 종류는 명령어 창에 Help를 실행하십시오.

위쪽 방향키와 아래쪽 방향키로 펜을 올리고 내릴 수 있습니다.

\(^o^)\ 그럼 좋은 하루 되세요~ /(^o^)/

                                                    - 랭디 -


                〈Python Canvas ver 0.10 + User Guide - Eglish〉
                
You can draw line to WSAD.

You can change the color by pressing the number keys. Number 0 is black.

To change the background color, press the shift key along with a number key. 

You can write text on 't'. First you need to enter the font.
Next, type the text you want to write.

You can set the cursor shape to 'e'.

You can rename the pane by pressing F5.

You can undo it by pressing BackSpace (but not redo).

You can press Delete to erase all the paintings on the canvas.

You can press Home to return the cursor to its initial position.

You can press Enter to stamp the cursor.

Tap ? to view the user guide you are currently viewing.

You can press Esc to expand the command paner.
For command types, launch Help in the Command Pane.

You can raise and lower the pen with the up and down arrow keys.

:) Have a good day~

                                                    Write by Rangdy
    ''')

#아래는 모두 포인터 색상 지정
def color_red() :
    color('red')

def color_orange() :
    color('red')

def color_yellow() :
    color('orange')

def color_green() :
    color('green')

def color_blue() :
    color('blue')

def color_purple() :
    color('purple')

def color_pink() :
    color('pink')

def color_brown() :
    color('brown')

def color_white() :
    color('white')

def color_black() :
    color('black')

#아래는 모두 배경 색상 지정
def bgcolor_red() :
    bgcolor('red')

def bgcolor_orange() :
    bgcolor('orange')

def bgcolor_yellow() :
    bgcolor('yellow')

def bgcolor_green() :
    bgcolor('green')

def bgcolor_blue() :
    bgcolor('blue')

def bgcolor_purple() :
    bgcolor('purple')

def bgcolor_pink() :
    bgcolor('pink')

def bgcolor_brown() :
    bgcolor('brown')

def bgcolor_white() :
    bgcolor('white')

def bgcolor_black() :
    bgcolor('black')
    
def Esc() :  #명령어 창(주요 업데이트)
    command = t.textinput("system", "명령어를 입력하십시오.")  #명령어 입력 받기
    if command == 'Shutdown' :  #프로그램 종료
        blue_screen(2)
    if command == 'AllDelete' :  #모든 것을 삭제(포인터도)
        t.clearscreen()
    if command == 'Reset' :  #리셋--증후군(?)--
        t.reset()
        t.bgcolor('white')
    if command == 'PatchNotes' :  #패치 노트(귀찮아서 버전 업데이트 안 할 거임
        print('''
                        〈파이썬 캔버스 패치 노트 - 한국어〉

알파 버전 - ver 0.0 ~ 0.

ver 0.0
기본적인 기능 추가

ver 0.1
사용 설명서 추가

ver 0.2
Esc 종료 추가

ver 0.3
Esc 창을 명령어 창으로 변경

ver 0.4
패치 노트 추가

ver 0.5
사용 설명서 내용 추가

ver 0.6
색상 변경 기능 추가

ver 0.7
write 버그 수정 시도 - 이제 폰트 변경이 정상 작동시키려 했습니다(실패).

ver  0.8
폰트 변경이 작동 안 하는 버그를 드디어 수정. penup, pendown 및 Home 기능 추가.

ver 0.9
명령어 가이드 창 추가

ver 0.10 +
여러 가지 수정

                    〈Python Canvas Patch Notes - English〉

Alpha Version - ver 0.0 ~ 0.

ver 0.0
Added basic functionality

ver 0.1
Added user documentation

ver 0.2
Added Esc Exit

ver 0.3
Changed Esc paner to Command paner

ver 0.4
Added patch notes

ver 0.5
Updating the user guide

ver 0.6
Added ability to change colors

ver 0.7
Tried to fix writing bug. Font changes now work properly (failed).

ver 0.8
Finally fixed a bug where changing fonts didn't work.
Added penup, pendown, and home functions.

ver 0.9
Added Command Guide

ver 0.10 +
Multiple changes

''')
    if command == 'SetColor' :  #기타 색상 지정
        color = t.textinput("system", "변경할 색상명을 입력하십시오.")
        color(color)
    if command == 'SetBgColor' :  #기타 배경 색상 지정
        bgcolor = t.textinput("system", "변경할 배경의 색상명을 입력하십시오.")
        bgcolor(bgcolor)
    if command == 'pRiNTbLuesCCreeN' :  #이스터에그(쉿!)
        real_bluescreen()
    if command == 'Help' or command == '?' :  #명령어 도움말 창
        print('''
〈파이썬 캔버스: 명령어 종류〉

Shutdown   : 블루 스크린을 띄우며 2초 후 종료합니다.
AllDelete  : 커서를 포함한 모든 것을 캔버스에서 지웁니다.
Reset      : 캔버스에서 도장 및 선, 텍스트를 지우고 커서를 초기 위치로 돌려보냅니다.
PatchNotes : 패치 노트를 출력합니다.
SetColor   : 기본 색상을 포함한 추가적인 색상 설정을 할 수 있습니다(ex: chocolate).
SetBgColor : 기본 색상을 포함한 추가적인 배경 색상 설정을 할 수 있습니다.
Help       : 지금 보고 계시는 명령어 도움말 창을 출력합니다.

〈Python Canvas: Commands Types〉

Shutdown   : Blue screen and shut down after 2 seconds.
AllDelete  :Erases everything from the canvas, including the cursor.
Reset      : Erases stamps, lines, and text from the canvas and returns the cursor to
             its initial position.
PatchNotes : Print the patch notes.
SetColor   : You can set additional color settings beyond the default color(ex: chocolate).
SetBgColor : You can set additional background color settings beyond the default color.
Help(?)    : Prints the Command Guide you are currently viewing.

''')
    t.listen()

t.reset()
t.bgcolor('white')
t.delay(0)  #딜레이 없애줌. 꼭 필요
pensize = 1
t.pensize(pensize)

#아래는 모두 키 지정
okp(w, 'w')
okp(s, 's')
okp(a, 'a')
okp(d, 'd')
okp(shape_stamp, 'b')
okp(stamp, 'Return')  #왜 이건 Return이지?
okp(write, 't')
okp(undo, 'BackSpace')
okp(clear, 'Delete')
okp(shape, 'e')
okp(title, 'F5')
okp(helping, '?')
okp(color_red, '1')
okp(color_orange, '2')
okp(color_yellow, '3')
okp(color_green, '4')
okp(color_blue, '5')
okp(color_purple, '6')
okp(color_pink, '7')
okp(color_brown, '8')
okp(color_white, '9')
okp(color_black, '0')
okp(bgcolor_red, '!')
okp(bgcolor_orange, '@')
okp(bgcolor_yellow, '#')
okp(bgcolor_green, '$')
okp(bgcolor_blue, '%')
okp(bgcolor_purple, '^')
okp(bgcolor_pink, '&')
okp(bgcolor_brown, '*')
okp(bgcolor_white, '(')
okp(bgcolor_black, ')')
okp(up, 'Up')
okp(down, 'Down')
okp(plus, '=')
okp(minus, '-')
okp(hide, 'h')
okp(home, 'Home')
okp(Esc, 'Escape')

t.listen()  #창에 포커스 맞추기
t.done()  #꼭 있어야됨. 아니면 실행하자마자 종료
