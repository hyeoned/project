import tkinter
import tkinter.messagebox

window=tkinter.Tk()
window.geometry("1000x1000")

imagek=tkinter.PhotoImage(file='시작전.png')
imageaa=tkinter.PhotoImage(file='체크.png')

labelk=tkinter.Label(window, image=imagek)

labelaa=tkinter.Label(window, image=imageaa)
labelbb=tkinter.Label(window, image=imageaa)
labelcc=tkinter.Label(window, image=imageaa)
labeldd=tkinter.Label(window, image=imageaa)
labelee=tkinter.Label(window, image=imageaa)

labelaa_click = False
labelbb_click = False
labelcc_click = False
labeldd_click = False
labelee_click = False

    

def clickMouse(event) :
    global labelaa_click, labelbb_click, labelcc_click, labeldd_click, labelee_click

    if 295 < event.x < 315 and 430 < event.y < 460:
        labelaa.place(x=934,y=528)
        labelaa_click= True
    elif 375 < event.x < 410 and 325 < event.y < 335:
        labelbb.place(x=934,y=428)
        labelbb_click= True
    elif 150 < event.x < 168 and 370 < event.y < 380:
        labelcc.place(x=934,y=628)
        labelcc_click= True
    elif 250 < event.x < 285 and 480 < event.y < 495:
        labeldd.place(x=934,y=328)
        labeldd_click= True
    elif 402 < event.x < 415 and 230 < event.y < 265:
        labelee.place(x=934,y=228)
        labelee_click= True
    if labelaa_click and labelbb_click and labelcc_click and labeldd_click and labelee_click==True:
        MsgBox = tkinter.messagebox.askquestion("숨은그림찾기", "성공하셨습니다! 게임을 종료하시겠습니까?")
    if MsgBox == "yes":
        window.destroy()
    else:
        tkinter.messagebox.showinfo("숨은그림찾기","게임을 다시 시작하려면 게임 창을 닫고 다시 실행해주세요.")
        


window.bind("<Button>", clickMouse)

image1=tkinter.PhotoImage(file='그림.png')

imagea=tkinter.PhotoImage(file='빗.png')
imageb=tkinter.PhotoImage(file='안경.png')
imagec=tkinter.PhotoImage(file='연필.png')
imaged=tkinter.PhotoImage(file='휴대폰.png')
imagee=tkinter.PhotoImage(file='모자.png')

labela=tkinter.Label(window, image=imagea)
labelb=tkinter.Label(window, image=imageb)
labelc=tkinter.Label(window, image=imagec)
labeld=tkinter.Label(window, image=imaged)
labele=tkinter.Label(window, image=imagee)

labela.place(x=800,y=200)
labelb.place(x=800,y=300)
labelc.place(x=800,y=400)
labeld.place(x=800,y=500)
labele.place(x=800,y=600)

labelI=tkinter.Label(text='숨어있는 그림')
labelI.place(x=810,y=160)



label=tkinter.Label(window, image=image1)
labelk.place(x=250,y=30)
# label.pack()

#타이머
def start_timer():
    countdown(120)  # 120초 타이머 시작
    start_btn.config(state='disable')# 타이머 시작 후 버튼 비활성화
    label.place(x=250,y=30)

def countdown(seconds):
    if seconds > 0:
        timer.config(text=f"남은 시간: {seconds}초")
        timer.after(1000, countdown, seconds-1)  # 1초마다 countdown 함수 호출
    else:
        timer.config(text="게임 종료")
        tkinter.messagebox.showinfo("숨은그림찾기","게임에 실패하셨습니다. 게임을 다시 시작하려면 게임 창을 닫고 다시 실행해주세요.")


# 타이머 텍스트를 표시할 라벨 위젯 생성
timer = tkinter.Label(window, text="")
timer.place(x=800,y=50)


# 타이머 시작 버튼 생성
start_btn = tkinter.Button(window, text="게임 시작", command=start_timer)
start_btn.place(x=810,y=100)



window.mainloop()