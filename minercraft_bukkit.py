from tkinter import *
import tkinter
from tkinter import filedialog

import matplotlib.pyplot as plt

win = Tk()

win.geometry("1024x576")
win.title("Minecraft bukkit")
win.option_add("*Foreground", "white")
win.configure(bg="#99AC94", bd=0)
win.option_add("*Font", "NotoSansKR-Medium 18")
win.option_add("*relief", "flat")
win.resizable(False, False)

# 메뉴 버튼
btn1 = Button(win)
btn1.config(text="메뉴")
btn1.configure(bg="#B0D597")
btn1.configure(bd=0)
btn1.place(x=25, y=50)
btn1.place(width=200, height=50)


# 자바 경로 설정 함수
def java():
    win.java_path = filedialog.askopenfilename(
        initialdir="path",
        title="select Java path",
        filetypes=[("java.exe", "*exe"),
                   ("all files", "*.*")])


# 메뉴 클릭 후 실행되는 함수
def menu():
    frame = tkinter.Frame(win)


btn1.config(command=java)

# 폴더 버튼
btn2 = Button(win)
btn2.config(text="폴더")
btn2.configure(bg="#B0D597")
btn2.configure(highlightcolor="black")
btn2.configure(bd=0)
btn2.place(x=250, y=50)
btn2.place(width=200, height=50)
Button()

# 서버 검색창
ent = Entry(win)
ent.place(width=1000, height=30)
ent.insert(0, "찾을 서버를 입력")  # 초기 문장 인서트
ent.configure(font=("NotoSansKR-Medium", 14))
ent.configure(bg="#7A7A7A")
ent.configure(bd=0)
ent.place(x=480, y=60, anchor=NW)


# '찾을 서버를 입력' 삭제 함수
def clear(event):
    if ent.get() == "찾을 서버를 입력":
        ent.delete(0, len(ent.get()))


ent.bind("<Button-1>", clear)  # clear 함수 사용

CREATING_SERVER = 12
SERVER_dict = dict()
for SERVER_BUTTONS in range(0, CREATING_SERVER, 1):
    SERVER_dict[f'slot_{SERVER_BUTTONS}'] = 1

# -----------------------------------------------------

# 서버 구동 버튼
btn_1 = Button(win)
btn_1.config(text="서버 구동")
btn_1['bg'] = "#B0D597"
btn_1.place(x=25, rely=1)
btn_1.configure(bd=0)
btn_1.place(y=-25)
btn_1.place(width=170, height=50, anchor=SW)
Button()

# 서버 설정 버튼
btn_2 = Button(win)
btn_2.config(text="서버 설정")
btn_2['bg'] = "#B0D597"
btn_2.configure(bd=0)
btn_2.place(x=210, rely=1)
btn_2.place(y=-25)
btn_2.place(width=170, height=50, anchor=SW)
Button()

# 플러그인 관리 버튼
btn_3 = Button(win)
btn_3.config(text="플러그인 관리")
btn_3['bg'] = "#B0D597"
btn_3.configure(bd=0)
btn_3.place(x=395, rely=1)
btn_3.place(y=-25)
btn_3.place(width=170, height=50, anchor=SW)
Button()

# 서버 추가 버튼
btn_4 = Button(win)
btn_4.config(text="서버 추가")
btn_4['bg'] = "#B0D597"
btn_4.configure(bd=0)
btn_4.place(x=620, rely=1)
btn_4.place(y=-25)
btn_4.place(width=160, height=50, anchor=SW)
Button()

# 서버 삭제 버튼
btn_5 = Button(win)
btn_5.config(text="서버 삭제")
btn_5['bg'] = "#B0D597"
btn_5.configure(bd=0)
btn_5.place(x=795, rely=1)
btn_5.place(y=-25)
btn_5.place(width=160, height=50, anchor=SW)
Button()

# -----------------------------------------------------

# 프레임 설정 위부터 왼쪽, 위쪽, 아래쪽, 오른쪽
frame1 = tkinter.Frame(win)
frame1.place(width=20, relheight=1, anchor=N)
frame1.configure(bg="#BCE0B3")
frame1.configure(bd="0")

frame2 = tkinter.Frame(win)
frame2.place(relwidth=1, height=80, anchor=W)
frame2.configure(bg="#BCE0B3")
frame2.configure(bd="0")

frame2 = tkinter.Frame(win)
frame2.place(relwidth=1, height=20, rely=1, anchor=SW)
frame2.configure(bg="#BCE0B3")
frame2.configure(bd="0")

frame3 = tkinter.Frame(win)
frame3.place(width=10, relheight=1, relx=1, anchor=NE)
frame3.configure(bg="#BCE0B3")
frame3.configure(bd="0")

win.mainloop()
