from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

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
    gluPerspective(30, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    if modo_camera == 1:
        gluLookAt(
            0.0, 0.0, 6.0,  
            0.0, 0.0, 0.0,  
            0.0, 1.0, 0.0     
        )

    elif modo_camera == 2:
        gluLookAt(
            6.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 1.0, 0.0
        )
    elif modo_camera == 3:
        gluLookAt(
            0.0, 6.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, -1.0
        )

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configurar_camera()
    if modo_camera == 1:
        glColor3f(1.0, 0.0, 0.0)
    elif modo_camera == 2:
        glColor3f(0.0, 1.0, 0.0)
    elif modo_camera == 3:
        glColor3f(0.0, 0.0, 1.0)

    # Cone 3D
    glutWireCone(0.7, 1.5, 20, 20)
    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Torre de Vortice 3D")
init()
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
glutMainLoop()