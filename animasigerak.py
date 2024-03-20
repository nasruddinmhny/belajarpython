import pygame

#inisialisasi awal
pygame.init()

#membuat surface
window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x,window_y))

#variabel
isRun = True

lebar = 20
panjang = 20

x = 250
y = 250

#kecepatannya
speed = 10 

while isRun:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Keluar aplikasi')
            isRun = False

    #key 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 :
        x-= speed

    if keys[pygame.K_RIGHT] and x < window_x-lebar:
        x+=speed

    if keys[pygame.K_DOWN] and y < window_y - panjang:
        y+= speed

    if keys[pygame.K_UP] and y > 0:
        y-=speed

    
    #buatkan aset(background)
    window.fill((255,255,255))
    #pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))
    #pygame.draw.circle(window, (255, 120, 0), [x, y], lebar, panjang)
    #pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]])



    #update perubahan window
    pygame.display.update()

pygame.quit()