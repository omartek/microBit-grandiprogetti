from turtle import *

#se non viene indicato appare con sfondo bianco
screen=Screen()
screen.bgcolor('black')


color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
