from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys


modo_camera = 1
angulo = 0

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
    gluPerspective(45,1.0,0.1,100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if modo_camera == 1:

        gluLookAt(
            0, 0, 6,
            0, 0, 0,
            0, 1, 0
        )

    elif modo_camera == 2:

        gluLookAt(
            0, 6, 0,
            0, 0, 0,
            0, 0, 1
        )

    elif modo_camera == 3:

        gluLookAt(
            6, 4, 6,
            0, 0, 0,
            0, 1, 0
        )

def paralelepipedo():

    vertices = [
        [-0.8, -0.5, -0.8],  # 0
        [ 0.8, -0.5, -0.8],  # 1
        [ 0.8,  0.5, -0.8],  # 2
        [-0.8,  0.5, -0.8],  # 3

        [-0.8, -0.5,  0.8],  # 4
        [ 0.8, -0.5,  0.8],  # 5
        [ 0.8,  0.5,  0.8],  # 6
        [-0.8,  0.5,  0.8],  # 7
    ]

    faces = [
        [0, 1, 2, 3],  
        [4, 5, 6, 7], 
        [0, 1, 5, 4],  
        [2, 3, 7, 6],  
        [0, 3, 7, 4],  
        [1, 2, 6, 5], 
    ]

    cores = [

        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
    ]

    glBegin(GL_QUADS)

    for i, face in enumerate(faces):
        glColor3fv(cores[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def display():

    global angulo
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

    configurar_camera()

    if modo_camera == 3:
        glRotatef(angulo, 0, 1, 0 )
        angulo += 0.1

    paralelepipedo()
    glutSwapBuffers()
    glutPostRedisplay()

def init():

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glEnable(GL_DEPTH_TEST)

glutInit(sys.argv)
glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow( b"Bloco de Pedra 3D" )
init()
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
glutMainLoop()