from guizero import App, Text, PushButton,Box
def Display_nums(n):
    output.value += str(n)
def erase():
    output.value = ""
def answer():
    output.value = eval(output.value)
def delete():
    n = ""
    for i in output.value:
        n+=i
    x = n[:-1]
    if len(n) >= 1: 
        output.value = x
    else:
        output.value = output.value
oporators = [" + ", " - ", " * ", " / "]
def pos_neg():
    if any(op in output.value for op in oporators):
        k = output.value.split(" ")
        last = k[-1]
        if last.startswith('-'):
            k[-1] = last[1:]
        else:
            k[-1] = "-" + last
        output.value = " ".join(k)
    elif not any(op in output.value for op in oporators):
        if output.value.startswith('-'):
            output.value = output.value[1:]
        else:
            output.value = "-" + output.value




            


    
app = App(layout="grid", width=500, height=500, title="CaLCULATOR")
screen = Box(app, height=50, width=200, grid=[3,0], border=True)
button1 = PushButton(app, text=1,grid=[0,0], width= 5, height=5, command=Display_nums, args=[1])
button2 = PushButton(app, text=2, grid=[1,0], width= 5, height=5,command=Display_nums,args=[2])
button3 = PushButton(app, text=3, grid=[2,0], width= 5, height=5,command=Display_nums,args=[3])
button4 = PushButton(app, text=4, grid=[0,1], width= 5, height=5,command=Display_nums,args=[4])
button5 = PushButton(app, text=5, grid=[1,1], width= 5, height=5,command=Display_nums,args=[5])
button6 = PushButton(app, text=6, grid=[2,1], width= 5, height=5,command=Display_nums,args=[6])
button7 = PushButton(app, text=7, grid=[0,2], width= 5, height=5,command=Display_nums,args=[7])
button8 = PushButton(app, text=8, grid=[1,2], width= 5, height=5,command=Display_nums,args=[8])
button9 = PushButton(app, text=9, grid=[2,2], width= 5, height=5,command=Display_nums,args=[9])
button0 = PushButton(app, text=0, grid=[1,3], width= 5, height=5,command=Display_nums,args=[0])
switch = PushButton(app, text="+/-", grid=[2,3], width= 5, height=5, command=pos_neg)
Plus = PushButton(app, text="+", grid=[3, 1], width= 5, height=5, command=Display_nums, args=[" + "])
Minus = PushButton(app, text="-", grid=[3, 2], width= 5, height=5, command=Display_nums, args=[" - "])
Times = PushButton(app, text="X", grid=[3, 3], width= 5, height=5, command=Display_nums, args=[" * "])
Divide = PushButton(app, text="%", grid=[4, 1], width= 5, height=5, command=Display_nums, args=[" / "])
Equals = PushButton(app, text="=", grid=[4,2], width= 5, height=5, command=answer)
clear = PushButton(app, text="Clear", grid=[4,3], width= 5, height=5, command=erase)
backspace = PushButton(app, text="Del", grid=[4,0], command=delete)
Decimal = PushButton(app, text= ".", grid=[0,3], width= 5, height=5, command=Display_nums, args=["."])
output = Text(screen, text="")
app.display()
