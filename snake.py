import pygame
from pygame.locals import *
import random

# constantes
WINDOWS_SIZE = (600, 600)  # tamanho da tela
WINDOWS_NAME = 'Snake'  # nome da tela
PIXEZ_SIZE = 10

# cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (250, 255, 255)
AZUL_ESCURO = (27, 48, 242)
AZUL_CLARO = (97, 167, 237)
ROXO = (163, 27, 242)
LARANJA = (242, 117, 27)
AMARELO = (217, 242, 27)

# cores que a cobrinha pode ser
CORES_COBRINHA = [VERMELHO, BRANCO, AZUL_ESCURO, AZUL_CLARO, ROXO, LARANJA, AMARELO]

# icone
programIcon = pygame.image.load('icon.jpg')


def DefinirCor(cores):
    index = random.randint(0, len(cores) - 1)
    return index


def Colisao(pos1, pos2):
    return pos1 == pos2


def ColisaoParede(posicao):
    if 0 <= posicao[0] < WINDOWS_SIZE[0] and 0 <= posicao[1] < WINDOWS_SIZE[1]:
        return False
    else:
        return True


def GerarLocalMaca():
    x = random.randint(0, WINDOWS_SIZE[0])
    y = random.randint(0, WINDOWS_SIZE[1])
    return x // PIXEZ_SIZE * PIXEZ_SIZE, y // PIXEZ_SIZE * PIXEZ_SIZE


def Resart():
    global pontos
    global snake_pos
    global apple_pos
    global snake_direction
    global CORES_COBRINHA
    index_cor_cobrinha = DefinirCor(CORES_COBRINHA)
    snake_surface.fill(CORES_COBRINHA[index_cor_cobrinha])
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    pontos = 0
    apple_pos = GerarLocalMaca()


pygame.init()
tela = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption(WINDOWS_NAME)
pygame.display.set_icon(programIcon)

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEZ_SIZE, PIXEZ_SIZE))
index_cor_cobrinha = DefinirCor(CORES_COBRINHA)
snake_surface.fill(CORES_COBRINHA[index_cor_cobrinha])
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEZ_SIZE, PIXEZ_SIZE))
apple_surface.fill(VERMELHO)
apple_pos = GerarLocalMaca()

pontos = 0

while True:
    pygame.time.Clock().tick(25)

    tela.fill(VERDE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    for i in range(len(snake_pos) - 1, 0, -1):
        if Colisao(snake_pos[0], snake_pos[i]):
            Resart()

        snake_pos[i] = snake_pos[i - 1]

    if ColisaoParede(snake_pos[0]):
        Resart()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEZ_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEZ_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEZ_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEZ_SIZE, snake_pos[0][1])

    tela.blit(apple_surface, apple_pos)

    if Colisao(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        pontos += 10
        apple_pos = GerarLocalMaca()

    for pos in snake_pos:
        tela.blit(snake_surface, pos)

    pygame.display.set_caption('Show Text')

    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(f'Pontos: {pontos}', True, PRETO, VERDE)

    textRect = text.get_rect()

    textRect.center = (WINDOWS_SIZE[0] // 2, WINDOWS_SIZE[1] // 2)

    tela.blit(text, textRect)

    pygame.display.update()
