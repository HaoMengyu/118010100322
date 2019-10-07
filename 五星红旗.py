from turtle import*
#画背景
begin_fill()
setup(1600,800,0,0)
color('red','red')
for i in range(2):
    forward(576)
    right(90)
    forward(384)
    right(90)
end_fill()
#绘制主星
penup()
goto(38.4,-76.8)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(115.2)
    right(144)
end_fill()
#第一颗小星星
penup()
goto(172.8,-48)
pendown()
left(60)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(38.4)
    right(144)
end_fill()
#第二颗小星星
penup()
goto(211.2,-80)
pendown
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(38.4)
    right(144)
end_fill()
#第三颗小星星
penup()
goto(211.2,-131.2)
pendown()
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(38.4)
    right(144)
end_fill()
#第四颗小星星
penup()
goto(172.8,-160)
pendown()
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(38.4)
    right(144)
end_fill()
hideturtle()
done()






