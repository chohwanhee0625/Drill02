from pico2d import *
import math

#math.cos()      # 기본 radian 단위, math.radians(90) -> pi/2 반환
#math.sin()
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

alp = -90


while (True):
    x = ((1 + math.cos(math.radians(alp))) * 100) + 400
    y = ((1 + math.sin(math.radians(alp))) * 100) + 90
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    alp += 30
    
    delay(0.01)

    
delay(3)

close_canvas()
