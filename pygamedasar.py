import pygame

#init
pygame.init()

#variabel
isRun = True

#display 
window = pygame.display.set_mode((500,500))

#titik kordinat posisi x dan y
x = 250
y = 250

#objek dengan rect
lebar = 20
panjang = 20 

#speed/kecepatan
speed = 10
while isRun:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Aplikasi Keluar')
            isRun = False

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < 500 - lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < 500 - panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed 

    #membuat wadah dengan background warnah putih
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))
    #melakukan perubahan yang terjadi pada display
    pygame.display.update()
