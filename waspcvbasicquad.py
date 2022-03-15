import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cv2
import time
from numpy import *
import acapture
import sys


def getframe():
    # For performance check
    # start = time.time()
    while (1):
        # vidcap = cv2.VideoCapture(0)
        vidcap = acapture.open(0)

        success, image = vidcap.read()
        if success:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.waitKey()

        return image


def getvert():


    img = getframe()
    sizemuliplyer = 1.1
    rows, cols, _ = img.shape
    imgResize = cv2.resize(img, (round(rows / (13*sizemuliplyer)), round(cols / (30*sizemuliplyer))))
    rows, cols, _ = imgResize.shape
    img = imgResize
    glBegin(GL_LINES)
    for i in range(0, rows, round(rows / (24*sizemuliplyer))):
        for j in range(0, cols, round(cols / (30*sizemuliplyer))):

            k = img[i, j]
            unit0 = (k[0] / 255)
            unit1 = (k[1] / 255)
            unit2 = (k[2] / 255)
            quadcentpos = (j, -i, 0)
            color = (unit2, unit1, unit0)

            quadseedpoint = (quadcentpos)
            xseedvertex = quadseedpoint[0]
            yseedvertex = quadseedpoint[1]
            zseedvertex = quadseedpoint[2]
            perspx = 3
            perspy = (-1)

            vert1 = (
                ((xseedvertex - perspx, (yseedvertex - perspy), zseedvertex)))
            vert2 = (
                ((xseedvertex - perspx, (yseedvertex + perspy), zseedvertex)))
            vert3 = (
                ((xseedvertex + perspx, (yseedvertex + perspy), zseedvertex)))
            vert4 = (
                ((xseedvertex + perspx, (yseedvertex - perspy), zseedvertex)))
            vert5 = (
                ((xseedvertex - perspx, (yseedvertex + perspy), -zseedvertex)))
            vert6 = (
                ((xseedvertex - perspx, (yseedvertex - perspy), -zseedvertex)))
            vert7 = (
                ((xseedvertex + perspx, (yseedvertex + perspy), -zseedvertex)))
            vert8 = (
                ((xseedvertex + perspx, (yseedvertex - perspy), -zseedvertex)))

            verticies = (vert1, vert2, vert3, vert4, vert5, vert6, vert7, vert8)

            edges = (
                (0, 1),
                (0, 3),
                (0, 4),
                (2, 1),
                (2, 3),
                (2, 7),
                (6, 3),
                (6, 4),
                (6, 7),
                (5, 1),
                (5, 4),
                (5, 7)
            )
            glColor3f(unit2, unit1, unit0)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(verticies[vertex])


    glEnd()




def main():
    pygame.init()
    fps = 30
    fpsClock = pygame.time.Clock()
    display = (424, 240)
    pygame.display.set_mode(display, OPENGL)
    gluPerspective(90, (display[0] / display[1]), 1, 300)
    glTranslate(-29, 16, -20)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        getvert()
        pygame.display.flip()
        fpsClock.tick(fps)


main()
