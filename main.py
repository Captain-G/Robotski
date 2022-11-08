# edit vector files using https://www.photopea.com/
import pygame

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

head_left = False
head_right = False
head_forward = True

left_hand_down = True
left_hand_half = False
left_hand_raised = False

right_hand_down = True
right_hand_half = False
right_hand_raised = False


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


state = "forward"
running = True
while running:
    screen.blit(background, (0, 0))
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
            elif event.key == pygame.K_KP4:
                left_hand_down = False
                left_hand_half = True
                left_hand_raised = False
            elif event.key == pygame.K_KP7:
                left_hand_down = False
                left_hand_half = False
                left_hand_raised = True

            if event.key == pygame.K_KP3:
                right_hand_down = True
                right_hand_half = False
                right_hand_raised = False
            elif event.key == pygame.K_KP6:
                right_hand_down = False
                right_hand_half = True
                right_hand_raised = False
            elif event.key == pygame.K_KP9:
                right_hand_down = False
                right_hand_half = False
                right_hand_raised = True

            if event.key == pygame.K_KP0:
                right_hand_down = True
                right_hand_half = False
                right_hand_raised = False
                left_hand_down = True
                left_hand_half = False
                left_hand_raised = False

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

    if right_hand_down:
        rightHandDown(right_hand_down_x, right_hand_down_y)
    elif right_hand_half:
        rightArmHalf(right_arm_half_x, right_arm_half_y)
    elif right_hand_raised:
        rightHandRaised(right_hand_raised_x, right_hand_raised_y)

    robotBody(robot_x, robot_y)

    # screen.blit(left_arrow_img, (left_arrow_x, left_arrow_y))
    # screen.blit(right_arrow_img, (right_arrow_x, right_arrow_y))
    # screen.blit(front_arrow_img, (front_arrow_x, front_arrow_y))

    pygame.display.update()
