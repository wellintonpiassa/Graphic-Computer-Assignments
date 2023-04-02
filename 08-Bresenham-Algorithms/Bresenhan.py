import pygame
import sys
global window


def plot(x, y):
    window.set_at((x, y), white)


def bresenhan_retas(x1, y1, x2, y2):
    delta_x = x2-x1
    delta_y = y2-y1
    p = 2 * delta_y - delta_x
    p2 = 2 * delta_y
    xy2 = 2*(delta_y-delta_x)
    x = x1
    y = y1
    while x != x2:
        plot(x,y)
        x = x + 1
        if p < 0:
            p = p + p2
        elif p >= 0:
            y = y + 1
            p = p + xy2


def draw_circle(xc, yc, x, y):
    plot(xc+x, yc+y);
    plot(xc-x, yc+y);
    plot(xc+x, yc-y);
    plot(xc-x, yc-y);
    plot(xc+y, yc+x);
    plot(xc-y, yc+x);
    plot(xc+y, yc-x);
    plot(xc-y, yc-x);


def bresenhan_circunferencia(xc, yc, raio):
    x = 0
    y = raio
    draw_circle(xc,yc,x,y)
    d = 3 - 2 * raio
    while y >= x:
        x += 1
        if d > 0:
            y = y - 1
            d = d + 4 * (x-y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(xc,yc,x,y)
            

white = (255, 255, 255) 
pygame.init()  # inicialização
window = pygame.display.set_mode((500, 500))  # cria a janela de exibição
pygame.display.set_caption("Algoritmo de Bresenhan")

bresenhan_retas(20, 50, 150, 150)
bresenhan_circunferencia(300, 200, 100)
pygame.display.update() # refresh da janela para exibir o que foi impresso com set_at

# loop para congelar a janela
# fica aguardando um evento, que no caso é o fechamento da janela no botao X
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # fechar a janela no x
            pygame.quit()
            sys.exit()
