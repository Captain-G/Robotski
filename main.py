# edit vector files using https://www.photopea.com/
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 650))

pygame.display.set_caption("Robotski")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

robot_img = pygame.image.load("body.png")
robot_x = 300
robot_y = 100

head_img = pygame.image.load("head.png")
head_x = 355
head_y = 20

right_img = pygame.image.load("right.png")
right_x = 355
right_y = 24

left_img = pygame.image.load("left.png")
left_x = 351
left_y = 28

left_arrow_img = pygame.image.load("leftarrow.png")
left_arrow_x = 22
left_arrow_y = 6.5

right_arrow_img = pygame.image.load("rightarrow.png")
right_arrow_x = 22
right_arrow_y = 65

front_arrow_img = pygame.image.load("frontarrow.png")
front_arrow_x = 22
front_arrow_y = 125

head_left = False
head_right = False
head_forward = True

def robotBody(x, y):
    screen.blit(robot_img, (x, y))


def robotHead(x, y):
    screen.blit(head_img, (x, y))


def headRight(x, y):
    screen.blit(right_img, (x, y))


def headLeft(x, y):
    screen.blit(left_img, (x, y))


state = "forward"
running = True
while running:
    screen.fill((0, 200, 150))
    pygame.draw.line(screen, (0, 0, 0), (80, 0), (80, 650), width=2)
    pygame.draw.line(screen, (0, 0, 0), (0, 50), (80, 50), width=2)
    pygame.draw.line(screen, (0, 0, 0), (0, 110), (80, 110), width=2)
    pygame.draw.line(screen, (0, 0, 0), (0, 170), (80, 170), width=2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_left = True
                head_right = False
                head_forward = False
            if event.key == pygame.K_RIGHT:
                head_right = True
                head_left = False
                head_forward = False
            elif event.key == pygame.K_UP:
                head_forward = True
                head_left = False
                head_right = False

    if head_left:
        headLeft(left_x, left_y)
    elif head_right:
        headRight(right_x, right_y)
    elif head_forward:
        robotHead(head_x, head_y)
    robotBody(robot_x, robot_y)

    screen.blit(left_arrow_img, (left_arrow_x, left_arrow_y))
    screen.blit(right_arrow_img, (right_arrow_x, right_arrow_y))
    screen.blit(front_arrow_img, (front_arrow_x, front_arrow_y))
    pygame.display.update()
