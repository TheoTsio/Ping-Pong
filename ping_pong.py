from pygame import *


window = display.set_mode((700, 500))
window.fill((200, 255, 255))




game = True
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)