from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



"""
Criar um objeto 3d original
Armazenar vértices, faces e cores.
Exibir sob diferentes ângulos de camera.
Vou fazer um Boneco do minecraft. cabeça, tronco, braços e pernas.
"""

faces = [

    [0, 1, 2, 3],
    [4, 5, 6, 7],

    [0, 1, 5, 4],
    [2, 3, 7, 6],

    [0, 3, 7, 4],
    [1, 2, 6, 5]
]


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

def cabeca():
    vertices = [
        (-0.3, 1.3, 1),
        ( 0.3, 1.3, 1),
        ( 0.3, 1.3, 0.5),
        (-0.3, 1.3, 0.5),

        (-0.3, 0.8, 1),
        ( 0.3, 0.8, 1),
        ( 0.3, 0.8, 0.5),
        (-0.3, 0.8, 0.5),
        ]

    glBegin(GL_QUADS)
    glColor3fv([1.0, 0.8, 0.6])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def braço_direito():
    vertices = [
        (-0.3, 0.8, 1),   
        (-0.8, 0.8, 1),   
        (-0.8, 0.4, 1),   
        (-0.3, 0.4, 1), 
        (-0.3, 0.8, 0.5), 
        (-0.8, 0.8, 0.5),
        (-0.8, 0.4, 0.5), 
        (-0.3, 0.4, 0.5), 
    ]

    glBegin(GL_QUADS)
    glColor3fv([0.5, 0.8, 1])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    
def braço_esquerdo():
    vertices = [
        (0.3, 0.8, 1),   
        (0.8, 0.8, 1),   
        (0.8, 0.4, 1),   
        (0.3, 0.4, 1), 
        (0.3, 0.8, 0.5), 
        (0.8, 0.8, 0.5),
        (0.8, 0.4, 0.5), 
        (0.3, 0.4, 0.5), 
    ]
    faces = [
        [0, 1, 2, 3],  
        [4, 5, 6, 7], 
        [0, 1, 5, 4],  
        [2, 3, 7, 6],  
        [0, 3, 7, 4],  
        [1, 2, 6, 5], 
    ]

    glBegin(GL_QUADS)
    glColor3fv([0.5, 0.8, 1])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def mao_direita():
    vertices = [
        (0.3, 0.4, 1),   
        (0.8, 0.4, 1),   
        (0.8, -0.2, 1),   
        (0.3, -0.2, 1), 
        (0.3, 0.4, 0.5), 
        (0.8, 0.4, 0.5),
        (0.8, -0.2, 0.5), 
        (0.3, -0.2, 0.5), 
    ]


    glBegin(GL_QUADS)
    glColor3fv([1, 0.8, 0.6])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def mao_esquerda():
    vertices = [
        (-0.3, 0.4, 1),   
        (-0.8, 0.4, 1),   
        (-0.8, -0.2, 1),   
        (-0.3, -0.2, 1), 
        (-0.3, 0.4, 0.5), 
        (-0.8, 0.4, 0.5),
        (-0.8, -0.2, 0.5), 
        (-0.3, -0.2, 0.5), 
    ]


    glBegin(GL_QUADS)
    glColor3fv([1, 0.8, 0.6])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def tronco():

    vertices = [
        (-0.4, 0.8, 1),
        ( 0.4, 0.8, 1),
        ( 0.4, 0.8, 0.5),
        (-0.4, 0.8, 0.5),

        (-0.4, -0.4, 1),
        ( 0.4, -0.4, 1),
        ( 0.4, -0.4, 0.5),
        (-0.4, -0.4, 0.5),
    ]


    glBegin(GL_POLYGON)
    glColor3fv([0.5, 0.8, 1])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def perna():
    vertices = [
        (-0.4, -0.4, 1),
        ( 0.4, -0.4, 1),
        ( 0.4, -0.4, 0.5),
        (-0.4, -0.4, 0.5),

        (-0.4, -1.4, 1),
        ( 0.4, -1.4, 1),
        ( 0.4, -1.4, 0.5),
        (-0.4, -1.4, 0.5),
    ]

    glBegin(GL_POLYGON)
    glColor3fv([0, 0, 0.3])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def sapato():
    vertices = [
        (-0.4, -1.4, 1),
        ( 0.4, -1.4, 1),
        ( 0.4, -1.4, 0.5),
        (-0.4, -1.4, 0.5),

        (-0.4, -1.6, 1),
        ( 0.4, -1.6, 1),
        ( 0.4, -1.6, 0.5),
        (-0.4, -1.6, 0.5),
    ]
    glBegin(GL_POLYGON)
    glColor3fv([0, 0, 0.5])
    for i, face in enumerate(faces):
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    configurar_camera()
    cabeca()
    tronco()
    braço_direito()
    braço_esquerdo()
    mao_direita()
    mao_esquerda()
    perna()
    sapato()
    glutSwapBuffers()



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)



glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"A Forja das Formas 3D")
init()
glutDisplayFunc(display)
glutKeyboardFunc(pegar_tecla)
glutMainLoop()
