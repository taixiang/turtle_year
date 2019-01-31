import turtle as t

x = -200
y = 100


def txt():
    t1 = (x, y)
    t2 = (x + 12, y - 12)
    penSize = 5
    t.screensize(400, 400, "#fff")
    t.pensize(penSize)
    t.pencolor("#ff0000")
    t.speed(10)
    t.hideturtle()
    # 点、
    t.up()
    t.goto(t1)
    t.down()  # 移动，画线
    t.goto(t2)

    # 横 -
    x1 = x - 18
    y1 = y - 22
    t3 = (x1, y1)
    t4 = (x1 + 60, y1)
    t.up()
    t.goto(t3)
    t.down()
    t.goto(t4)

    # 点、、
    x2 = x1 + 16
    y2 = y1 - 10
    t5 = (x2, y2)
    t6 = (x2 + 8, y2 - 16)
    t7 = (x2 + 26, y2)
    t8 = (x2 + 18, y2 - 18)
    t.up()
    t.goto(t5)
    t.down()
    t.goto(t6)
    t.up()
    t.goto(t7)
    t.down()
    t.goto(t8)

    # 长横-
    x3 = x1 - 15
    y3 = y2 - 24
    t9 = (x3, y3)
    t10 = (x3 + 90, y3)
    t.up()
    t.goto(t9)
    t.down()
    t.goto(t10)

    # 横 -
    x4 = x3 + 10
    y4 = y3 - 22
    t11 = (x4, y4)
    t12 = (x4 + 70, y4)
    t.up()
    t.goto(t11)
    t.down()
    t.goto(t12)

    # 竖 |
    x5 = x + 12
    y5 = y3
    t13 = (x5, y5)
    t14 = (x5, y5 - 90)
    t.up()
    t.goto(t13)
    t.down()
    t.goto(t14)

    # 勾
    x6 = x5
    y6 = y5 - 90
    t15 = (x6 - 12, y6 + 10)
    t.goto(t15)

    # 点、、
    x7 = x6 - 12
    y7 = y5 - 40
    t16 = (x7, y7)
    t17 = (x7 - 8, y7 - 20)
    t.up()
    t.goto(t16)
    t.down()
    t.goto(t17)
    t18 = (x7 + 24, y7 - 5)
    t19 = (x7 + 30, y7 - 16)
    t.up()
    t.goto(t18)
    t.down()
    t.goto(t19)

    # 撇
    x8 = x + 100
    y8 = y - 10
    t20 = (x8, y8)
    t21 = (x8 - 32, y8 - 20)
    t.up()
    t.goto(t20)
    t.down()
    t.goto(t21)

    # 撇
    t22 = (x8 - 40, y8 - 135)
    t.goto(t22)

    # 横
    x9 = x3 + 100
    y9 = y3 - 8
    t23 = (x9, y9)
    t24 = (x9 + 50, y9)
    t.up()
    t.goto(t23)
    t.down()
    t.goto(t24)

    # 竖
    x10 = x9 + 24
    y10 = y9
    t25 = (x10, y10)
    t26 = (x10, y10 - 80)
    t.up()
    t.goto(t25)
    t.down()
    t.goto(t26)
    nian()
    kuai()
    le()
    t.done()


# 年
def nian():
    # 撇
    x1 = x + 180
    y1 = y - 10
    t1 = (x1, y1)
    t2 = (x1 - 18, y1 - 28)
    t.up()
    t.goto(t1)
    t.down()
    t.goto(t2)

    # 横
    x2 = x1 - 8
    y2 = y - 25
    t3 = (x2, y2)
    t4 = (x2 + 60, y2)
    t.up()
    t.goto(t3)
    t.down()
    t.goto(t4)

    # 横
    x3 = x2 - 8
    y3 = y - 65
    t5 = (x3, y3)
    t6 = (x3 + 65, y3)
    t.up()
    t.goto(t5)
    t.down()
    t.goto(t6)

    # 小竖
    x4 = x3
    y4 = y3 - 25
    t7 = (x4, y4)
    t.up()
    t.goto(t5)
    t.down()
    t.goto(t7)

    # 长横
    x5 = x4 - 10
    y5 = y4
    t8 = (x5, y5)
    t9 = (x5 + 85, y5)
    t.up()
    t.goto(t8)
    t.down()
    t.goto(t9)

    # 长竖
    x6 = x2 + 25
    y6 = y2
    t10 = (x6, y6)
    t11 = (x6, y6 - 120)
    t.up()
    t.goto(t10)
    t.down()
    t.goto(t11)


# 快
def kuai():
    # 点
    x1 = x + 280
    y1 = y - 65
    t1 = (x1, y1)
    t2 = (x1 - 6, y1 - 25)
    t.up()
    t.goto(t1)
    t.down()
    t.goto(t2)

    # 竖
    x2 = x1 + 10
    y2 = y - 15
    t3 = (x2, y2)
    t4 = (x2, y2 - 130)
    t.up()
    t.goto(t3)
    t.down()
    t.goto(t4)

    # 点
    x3 = x2 + 10
    y3 = y1 - 8
    t5 = (x3, y3)
    t6 = (x3 + 6, y3 - 10)
    t.up()
    t.goto(t5)
    t.down()
    t.goto(t6)

    # 横
    x4 = x3 + 25
    y4 = y - 60
    t7 = (x4, y4)
    t8 = (x4 + 60, y4)
    t9 = (x4 + 60, y4 - 28)
    t.up()
    t.goto(t7)
    t.down()
    t.goto(t8)
    t.goto(t9)

    # 长横
    x5 = x4 - 10
    y5 = y4 - 28
    t10 = (x5, y5)
    t11 = (x5 + 90, y5)
    t.up()
    t.goto(t10)
    t.down()
    t.goto(t11)

    # 撇
    x6 = x4 + 30
    y6 = y2 - 5
    t12 = (x6, y6)
    t13 = (x6 - 18, y6 - 125)
    t.up()
    t.goto(t12)
    t.down()
    t.goto(t13)

    # 捺
    x7 = x6 + 8
    y7 = y5 - 20
    t14 = (x7, y7)
    t15 = (x7 + 12, y7 - 38)
    t.up()
    t.goto(t14)
    t.down()
    t.goto(t15)


# 乐
def le():
    # 撇
    x1 = x + 510
    y1 = y - 20
    t1 = (x1, y1)
    t2 = (x1 - 65, y1 - 20)
    t3 = (x1 - 68, y1 - 60)
    t4 = (x1 + 10, y1 - 60)
    t.up()
    t.goto(t1)
    t.down()
    t.goto(t2)
    t.goto(t3)
    t.goto(t4)

    # 竖
    x2 = x1 - 30
    y2 = y1 - 35
    t5 = (x2, y2)
    t6 = (x2, y2 - 92)
    t7 = (x2 - 12, y2 - 85)
    t.up()
    t.goto(t5)
    t.down()
    t.goto(t6)
    t.goto(t7)

    # 点、、
    x3 = x2 - 20
    y3 = y2 - 50
    t8 = (x3, y3)
    t9 = (x3 - 8, y3 - 20)
    t.up()
    t.goto(t8)
    t.down()
    t.goto(t9)
    t10 = (x3 + 40, y3 - 5)
    t11 = (x3 + 46, y3 - 16)
    t.up()
    t.goto(t10)
    t.down()
    t.goto(t11)


# 新年快乐
def xin():
    t.title('dalao 带带我')  # 设置标题栏文字
    # t.hideturtle()  # 隐藏箭头
    t.getscreen().bgcolor('#f0f0f0')  # 背景色
    t.color('#c1e6c6', 'red')  # 设置画线颜色、填充颜色，可以直接写 green，也可以用 #c1e6c6
    t.pensize(2)  # 笔的大小
    t.speed(1)  # 图形绘制的速度,1~10
    t.up()  # 移动，不画线
    t.goto(0, -150)

    t.down()  # 移动，画线
    # t.begin_fill()  # 开始填充
    # t.goto(0, -150)
    t.goto(-175.12, -8.59)
    t.left(140)
    pos = []
    for i in range(19):
        t.right(10)
        t.forward(20)
        pos.append((-t.pos()[0], t.pos()[1]))
    for item in pos[::-1]:
        t.goto(item)
    t.goto(175.12, -8.59)
    t.goto(0, -150)
    t.left(50)
    t.end_fill()  # 结束填充，显示填充效果

    t.done()


# xin()
txt()
