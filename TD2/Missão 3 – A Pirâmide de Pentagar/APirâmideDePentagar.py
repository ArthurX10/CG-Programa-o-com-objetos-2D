from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

"""
uso de gl_polygon e gl_triangles
visão frontal, lateral e superior
base plano XY, e o apice no plano Z
"""

modo_camera = 1

def pegar_tecla(tecla, x, y):
    global modo_camera

    if tecla == b'1':
        modo_camera = 1
    elif tecla == b'2':
        modo_camera = 2
    elif tecla == b'3':
        modo_camera = 3
    glutPostRedisplay()


def configurar_camera():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if modo_camera == 1:
        gluLookAt(
            0, 0, 6,
            0, 0, 0,
            0, 1, 0)

    elif modo_camera == 2:
        gluLookAt(
            0, 6, 0,
            0, 0, 0,
            0, 0, -1)

    elif modo_camera == 3:
        gluLookAt(
            6, 0, 0,
            0, 0, 0,
            0, 1, 0)


def pentagono():
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.7, 0.2)
    glVertex2f(0.4, -0.7)
    glVertex2f(-0.4, -0.7)
    glVertex2f(-0.7, 0.2)
    glEnd()
   
def triangulos():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(0.0, 0.8, 0.0)
    glVertex3f(0.7, 0.2, 0.0)
    glVertex3f(0.0, 0, 1.0)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex3f(0.7, 0.2, 0)
    glVertex3f(0.4, -0.7, 0)
    glVertex3f(0, 0, 1)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 1)
    glVertex3f(0.4, -0.7, 0)
    glVertex3f(-0.4, -0.7,0)
    glVertex3f(0, 0, 1.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 0)
    glVertex3f(-0.4, -0.7, 0)
    glVertex3f(-0.7, 0.2, 0)
    glVertex3f(0, 0, 1)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex3f(-0.7, 0.2, 0)
    glVertex3f(0.0, 0.8, 0.0)
    glVertex3f(0, 0, 1)
    glEnd()
    glFlush()


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    configurar_camera()
    pentagono()
    triangulos()
    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"A Piramide de Pentagar")
init()
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
glutMainLoop()