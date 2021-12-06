# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
from tkinter import filedialog
import time
import psutil
import os
import math
from PIL import Image, ImageTk

path = "C:\KimuSoft\KuBukkit"

btn_color = "#B0D597"
frame_color = "#BCE0B3"
background_color = "#99AC94"

search_placeholder = "서버 검색"

btn1_size = [200, 50]
btn2_size = [170, 50]
btn3_size = [160, 50]

btn1_y = 12.5
btn2_y = -25
f2_y = 80

top_frame_y = 40

btn2_margin = 15

is_down = False


# 프레임 설정
def frame_setting():
    # 왼쪽
    frame1.place(width=20, relheight=1, anchor=N)
    frame1.configure(bg=frame_color)
    frame1.configure(bd="0")

    # 위쪽
    frame2.place(relwidth=1, height=f2_y, anchor=W)
    frame2.configure(bg=frame_color)
    frame2.configure(bd="0")

    # 아래쪽
    frame3.place(relwidth=1, height=20, rely=1, anchor=SW)
    frame3.configure(bg=frame_color)
    frame3.configure(bd="0")

    # 오른쪽
    frame4.place(width=10, relheight=1, relx=1, anchor=NE)
    frame4.configure(bg=frame_color)
    frame4.configure(bd="0")


# 자바 경로 설정 함수
def java():
    win.java_path = filedialog.askopenfilename(
        initialdir="path",
        title="select Java path",
        filetypes=[("java.exe", "*exe"),
                   ("all files", "*.*")])


def menu_ui(isTrue):
    if isTrue:
        ram_x = 50
        menu_y_center = f2_y / 4
        menu_lab1.place(x=ram_x, y=menu_y_center - 15 - 30, width=55, height=30)
        menu_spinbox.place(x=ram_x, y=menu_y_center - 15, height=30)
        menu_lab2.place(x=160, y=menu_y_center - 15, width=30, height=30)
        menu_btn_1.place(x=160 + 30 + btn2_margin, y=menu_y_center - 20, width=75, height=40)

    elif not isTrue:
        menu_lab1.place_forget()
        menu_spinbox.place_forget()
        menu_lab2.place_forget()
        menu_btn_1.place_forget()


# 메뉴 클릭 후 실행되는 함수
def menu():
    global f2_y
    global is_down
    global top_frame_y

    if not is_down:
        # 배경화면이 아래로 덮힘
        while True:
            time.sleep(0.001)
            f2_y += 10
            top_frame_y += 5
            frame2.place(relwidth=1, height=f2_y, anchor=W)
            top_frame.place(x=10, y=top_frame_y)

            win.update()
            if f2_y == 250:
                is_down = True
                menu_ui(True)
                break

    elif is_down:
        menu_ui(False)
        # 배경화면이 아래로 덮힘
        while True:
            time.sleep(0.001)
            f2_y -= 10
            top_frame_y -= 5
            frame2.place(relwidth=1, height=f2_y, anchor=W)
            top_frame.place(x=10, y=top_frame_y)

            win.update()
            if f2_y == 80:
                is_down = False
                break


win = Tk()

win.geometry("1024x576")
win.title("Minecraft bukkit")
win.option_add("*Foreground", "white")
win.configure(bg=background_color, bd=0)
win.option_add("*Font", "NotoSansKR-Medium 18")
win.option_add("*relief", "flat")
win.resizable(False, False)

# -----------------------------------------------------

container = Frame(win)
container.config()
canvas = Canvas(container)
canvas.config(bg="#A9C0A3")

bukkit_scrollbar = Scrollbar(container, orient="horizontal", command=canvas.xview)

scrollable_frame = Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

canvas.create_window((0, 0), win=scrollable_frame, anchor=NW)
canvas.configure(xscrollcommand=bukkit_scrollbar.set)
canvas.config(highlightthickness=0, width=965, height=350)
canvas.pack(side=TOP, fill=BOTH, expand=True)

container.place(relx=0.024, rely=0.52, anchor=W)
bukkit_scrollbar.pack(side=BOTTOM, fill=X)

bukkits = 0

bukkit_value = IntVar()

# 자동 버킷 변수 선언
for i in range(1, 29):
    globals()['bukkit_{}'.format(i)] = Radiobutton(scrollable_frame)
    globals()['bukkit_{}'.format(i)].config(font=("NotoSansKR-Medium", 14), width=15, height=2)
    globals()['bukkit_{}'.format(i)].config(text='bukkit_{}'.format(i), variable=bukkit_value, value=i, indicatoron=0)

    globals()['bukkit_image_{}'.format(i)] = PhotoImage(file="testimage.png")
    globals()['bukkit_image_label_{}'.format(i)] = Label(globals()['bukkit_{}'.format(i)], image=globals()['bukkit_image_{}'.format(i)])
    globals()['bukkit_image_label_{}'.format(i)].pack()

    bukkits = i

f = 0

for i in range(1, math.ceil(bukkits / 3) + 1):

    for j in range(1, 4):
        try:
            globals()['bukkit_{}'.format(j + f)].grid(row=j, column=i, sticky=E)

        except:
            print(j + f, "번 버킷 없음")

    f += 3


frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)
frame3 = tkinter.Frame(win)
frame4 = tkinter.Frame(win)

frame_setting()

# 상단 프레임
top_frame = Frame(win)
top_frame.place(x=10, y=top_frame_y, width=1004, height=75)
top_frame.configure(bg=background_color)

# 메뉴 버튼
btn1 = Button(top_frame)
btn1.config(text="메뉴")
btn1.configure(bg=btn_color)
btn1.configure(bd=0)
btn1.place(x=15, y=btn1_y, width=btn1_size[0], height=btn1_size[1])
btn1.config(command=menu)

# 폴더 버튼
btn2 = Button(top_frame)
btn2.config(text="폴더")
btn2.configure(bg=btn_color)
btn2.configure(highlightcolor="black")
btn2.configure(bd=0)
btn2.place(x=235, y=btn1_y, width=btn1_size[0], height=btn1_size[1])
btn2.config(command=lambda: os.startfile(path))

# 서버 검색창
ent = Entry(top_frame)
ent.insert(0, search_placeholder)  # 초기 문장 인서트
ent.configure(font=("NotoSansKR-Medium", 14))
ent.configure(bg="#7A7A7A")
ent.configure(bd=0)
ent.place(x=470, y=btn1_y + 10, width=515, height=30, anchor=NW)


# '찾을 서버를 입력' 삭제 함수
def clear(event):
    if ent.get() == search_placeholder:
        ent.delete(0, len(ent.get()))


ent.bind("<Button-1>", clear)  # clear 함수 사용

CREATING_SERVER = 12
SERVER_dict = dict()
for SERVER_BUTTONS in range(0, CREATING_SERVER, 1):
    SERVER_dict[f'slot_{SERVER_BUTTONS}'] = 1

# -----------------------------------------------------

# 램 설정
menu_lab1 = Label(win)
menu_lab1.configure(font=("NotoSansKR-Medium", 14))
menu_lab1.config(text="RAM", bg=background_color)

# 램 mb
menu_spinbox = Spinbox(win)
menu_spinbox.insert(0, "2048")
menu_spinbox.config(from_=512, to=int(round(psutil.virtual_memory().total / (1024.0 ** 2))))
menu_spinbox.config(width=6, increment=512, justify="right", bg=background_color)

# 램 mb 뒤 단위
menu_lab2 = Label(win)
menu_lab2.configure(font=("NotoSansKR-Medium", 16))
menu_lab2.config(text="MB", bg=frame_color)

# 자바 인식
menu_btn_1 = Button(win)
menu_btn_1.config(text="자바")
menu_btn_1['bg'] = background_color
menu_btn_1.configure(bd=0)
menu_btn_1.config(command=lambda: java())

menu_lab1.place_forget()
menu_spinbox.place_forget()
menu_lab2.place_forget()
menu_btn_1.place_forget()

# -----------------------------------------------------

# 서버 구동 버튼
btn_1 = Button(win)
btn_1.config(text="서버 구동")
btn_1['bg'] = btn_color
btn_1.configure(bd=0)
btn_1.place(x=25, y=btn2_y, rely=1, width=btn2_size[0], height=btn2_size[1], anchor=SW)
# btn_1.config(command=)

# 서버 설정 버튼
btn_2 = Button(win)
btn_2.config(text="서버 설정")
btn_2['bg'] = btn_color
btn_2.configure(bd=0)
btn_2.place(x=25 + btn2_size[0] + btn2_margin, y=btn2_y, rely=1, width=btn2_size[0], height=btn2_size[1], anchor=SW)
# btn_2.config(command=)

# 플러그인 관리 버튼
btn_3 = Button(win)
btn_3.config(text="플러그인 관리")
btn_3['bg'] = btn_color
btn_3.configure(bd=0)
btn_3.place(x=25 + (btn2_size[0] + btn2_margin) * 2, y=btn2_y, rely=1, width=btn2_size[0], height=btn2_size[1],
            anchor=SW)
# btn_3.config(command=)

# 서버 추가 버튼
btn_4 = Button(win)
btn_4.config(text="서버 추가")
btn_4['bg'] = btn_color
btn_4.configure(bd=0)
btn_4.place(x=620, y=btn2_y, rely=1, width=btn3_size[0], height=btn3_size[1], anchor=SW)
# btn_4.config(command=)

# 서버 삭제 버튼
btn_5 = Button(win)
btn_5.config(text="서버 삭제")
btn_5['bg'] = btn_color
btn_5.configure(bd=0)
btn_5.place(x=620 + btn3_size[0] + btn2_margin, y=btn2_y, rely=1, width=btn3_size[0], height=btn3_size[1], anchor=SW)
# btn_5.config(command=)

win.mainloop()
