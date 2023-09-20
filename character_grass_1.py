from pico2d import *
import math

#math.cos()      # 기본 radian 단위, math.radians(90) -> pi/2 반환
#math.sin()
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if (x < 800 and y == 90):
        x += 5
    elif (x == 800 and y < 600):
        y += 5
    elif (x > 0 and y == 600):
        x -= 5
    else:
        y -= 5
    
    delay(0.01)

    
delay(3)

close_canvas()
