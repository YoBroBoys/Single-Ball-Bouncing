import pygame
pygame.init()

x,y=600,400
window= pygame.display.set_mode((x,y))
pygame.display.set_caption("GAME")

green = (200,255,0)
blk = (200,200,200)
blu = (255,255,0)

clock = pygame.time.Clock()
bx = 300
by = 200
br = 30
bsx = 10
bsy = 10

rx = 300
ry = 200
rsx = 10
rsy = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    bx += bsx
    by += bsy
    if bx - br < 0 or bx + br > x:
        bsx =- bsx
    if by - br < 0 or by + br > y:
        bsy =- bsy
    rx += rsx
    ry += rsy
    if rx < 0 or rx > x-100:
        rsx = - rsx
    if ry < 0 or ry > y-100:
        rsy = - rsy
    window.fill(green)
    pygame.draw.circle(window,blk,(bx,by),br)
    pygame.draw.rect(window,blu,(rx,ry,100,100))
    clock.tick(20)
    pygame.display.update()