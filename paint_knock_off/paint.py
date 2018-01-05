import pygame

pygame.init()
display= pygame.display.set_mode((800,600))
pygame.display.set_caption('paint')
pygame.display.update()
gameexit= False

while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit=True
        if event.type == pygame.KEYUP:
            pass
        if event.type == pygame.KEYDOWN:
            pass
       # print(event)

pygame.quit()
quit()

