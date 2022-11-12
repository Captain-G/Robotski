# edit vector files using https://www.photopea.com/
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 650))

pygame.display.set_caption("Robotski")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")

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

left_arm_half_img = pygame.image.load("left_arm_half.png")
left_arm_half_x = 190
left_arm_half_y = 155

right_arm_half_img = pygame.image.load("right_arm_half.png")
right_arm_half_x = 440
right_arm_half_y = 155

left_hand_down_img = pygame.image.load("left_hand_down.png")
left_hand_down_x = 285
left_hand_down_y = 135

right_hand_down_img = pygame.image.load("right_hand_down.png")
right_hand_down_x = 440
right_hand_down_y = 135

left_hand_raised_img = pygame.image.load("left_hand_raised.png")
left_hand_raised_x = 130
left_hand_raised_y = 155

right_hand_raised_img = pygame.image.load("right_hand_raised.png")
right_hand_raised_x = 440
right_hand_raised_y = 155

left_arm_folded_img = pygame.image.load("left_arm_folded.png")
left_arm_folded_x = 110
left_arm_folded_y = 150

right_arm_folded_img = pygame.image.load("right_arm_folded.png")
right_arm_folded_x = 445
right_arm_folded_y = 150

clap_left_img = pygame.image.load("clap_left.png")
clap_left_x = 300
clap_left_y = 165

clap_right_img = pygame.image.load("clap_right.png")
clap_right_x = 390
clap_right_y = 162

clap_text_img = pygame.image.load("clap_text.png")
clap_text_x = 350
clap_text_y = 315

head_left = False
head_right = False
head_forward = True

left_hand_down = True
left_hand_half = False
left_hand_raised = False
left_hand_folded = False

right_hand_down = True
right_hand_half = False
right_hand_raised = False
right_hand_folded = False

clapping = False


def robotBody(x, y):
    screen.blit(robot_img, (x, y))


def robotHead(x, y):
    screen.blit(head_img, (x, y))


def headRight(x, y):
    screen.blit(right_img, (x, y))


def headLeft(x, y):
    screen.blit(left_img, (x, y))


def leftArmHalf(x, y):
    screen.blit(left_arm_half_img, (x, y))


def rightArmHalf(x, y):
    screen.blit(right_arm_half_img, (x, y))


def leftHandDown(x, y):
    screen.blit(left_hand_down_img, (x, y))


def rightHandDown(x, y):
    screen.blit(right_hand_down_img, (x, y))


def leftHandRaised(x, y):
    screen.blit(left_hand_raised_img, (x, y))


def rightHandRaised(x, y):
    screen.blit(right_hand_raised_img, (x, y))


def leftArmFolded(x, y):
    screen.blit(left_arm_folded_img, (x, y))


def rightArmFolded(x, y):
    screen.blit(right_arm_folded_img, (x, y))


def clap(l_x, l_y, r_x, r_y, t_x, t_y):
    screen.blit(clap_left_img, (l_x, l_y))
    screen.blit(clap_right_img, (r_x, r_y))
    screen.blit(clap_text_img, (t_x, t_y))
    # clap_sound = mixer.Sound("clap.wav")
    # clap_sound.play()


state = "forward"
running = True
while running:
    screen.blit(background, (0, 0))
    robotBody(robot_x, robot_y)
    # pygame.draw.line(screen, (0, 0, 0), (80, 0), (80, 650), width=2)
    # pygame.draw.line(screen, (0, 0, 0), (0, 50), (80, 50), width=2)
    # pygame.draw.line(screen, (0, 0, 0), (0, 110), (80, 110), width=2)
    # pygame.draw.line(screen, (0, 0, 0), (0, 170), (80, 170), width=2)

    # leftHandDown(left_hand_down_x, left_hand_down_y)
    # leftArmHalf(left_arm_half_x, left_arm_half_y)
    # leftHandRaised(left_hand_raised_x, left_hand_raised_y)

    # rightHandDown(right_hand_down_x, right_hand_down_y)
    # rightArmHalf(right_arm_half_x, right_arm_half_y)
    # rightHandRaised(right_hand_raised_x, right_hand_raised_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_left = True
                head_right = False
                head_forward = False
            elif event.key == pygame.K_RIGHT:
                head_right = True
                head_left = False
                head_forward = False
            elif event.key == pygame.K_UP:
                head_forward = True
                head_left = False
                head_right = False
            if event.key == pygame.K_KP1:
                left_hand_down = True
                left_hand_half = False
                left_hand_raised = False
                left_hand_folded = False
            elif event.key == pygame.K_KP4:
                left_hand_down = False
                left_hand_half = True
                left_hand_raised = False
                left_hand_folded = False
            elif event.key == pygame.K_KP7:
                left_hand_down = False
                left_hand_half = False
                left_hand_raised = True
                left_hand_folded = False
            elif event.key == pygame.K_KP3:
                right_hand_down = True
                right_hand_half = False
                right_hand_raised = False
                right_hand_folded = False
            elif event.key == pygame.K_KP6:
                right_hand_down = False
                right_hand_half = True
                right_hand_raised = False
                right_hand_folded = False
            elif event.key == pygame.K_KP9:
                right_hand_down = False
                right_hand_half = False
                right_hand_raised = True
                right_hand_folded = False
            elif event.key == pygame.K_KP0:
                right_hand_down = True
                right_hand_half = False
                right_hand_raised = False
                right_hand_folded = False
                left_hand_down = True
                left_hand_half = False
                left_hand_raised = False
                left_hand_folded = False
                clapping = False
            elif event.key == pygame.K_KP2:
                right_hand_down = False
                right_hand_half = False
                right_hand_raised = False
                right_hand_folded = False
                left_hand_down = False
                left_hand_half = False
                left_hand_raised = False
                left_hand_folded = False
                clapping = True
            elif event.key == pygame.K_KP8:
                right_hand_down = False
                right_hand_half = False
                right_hand_raised = False
                right_hand_folded = True
                left_hand_down = False
                left_hand_half = False
                left_hand_raised = False
                left_hand_folded = True
                clapping = False

    if head_left:
        headLeft(left_x, left_y)
    elif head_right:
        headRight(right_x, right_y)
    elif head_forward:
        robotHead(head_x, head_y)

    if left_hand_down:
        leftHandDown(left_hand_down_x, left_hand_down_y)
    elif left_hand_half:
        leftArmHalf(left_arm_half_x, left_arm_half_y)
    elif left_hand_raised:
        leftHandRaised(left_hand_raised_x, left_hand_raised_y)
    elif left_hand_folded:
        leftArmFolded(left_arm_folded_x, left_arm_folded_y)
    elif clapping:
        clap(clap_left_x, clap_left_y, clap_right_x, clap_right_y, clap_text_x, clap_text_y)

    if right_hand_down:
        rightHandDown(right_hand_down_x, right_hand_down_y)
    elif right_hand_half:
        rightArmHalf(right_arm_half_x, right_arm_half_y)
    elif right_hand_raised:
        rightHandRaised(right_hand_raised_x, right_hand_raised_y)
    elif right_hand_folded:
        rightArmFolded(right_arm_folded_x, right_arm_folded_y)
    elif clapping:
        clap(clap_left_x, clap_left_y, clap_right_x, clap_right_y, clap_text_x, clap_text_y)

    pygame.display.update()
