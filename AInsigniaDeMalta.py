import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random


cor = [1.0, 0.0, 0.0]


def gerar_cor():
   return [random.random(), random.random(), random.random()]


def retangulo(x1, y1, x2, y2):

    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x1, y2)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x2, y1)

    gl.glEnd()


def triangulo(x1, y1, x2, y2, x3, y3):

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x3, y3)
    gl.glEnd()


def desenharVasco():

    gl.glColor3f(*cor)
    retangulo(-0.08, 0.0, 0.08, 0.45)

    triangulo(
        -0.08, 0.45,
         0.08, 0.45,
         0.0, 0.75
    )

    # Braço inferior
    retangulo(-0.08, -0.45, 0.08, 0.0)

    triangulo(
        -0.08, -0.45,
         0.08, -0.45,
         0.0, -0.75
    )

    # Braço esquerdo
    retangulo(-0.45, -0.08, 0.0, 0.08)
    triangulo(
        -0.45, -0.08,
        -0.45, 0.08,
        -0.75, 0.0
    )

    # Braço direito
    retangulo(0.0, -0.08, 0.45, 0.08)

    triangulo(
         0.45, -0.08,
         0.45, 0.08,
         0.75, 0.0
    )


def pegar_tecla(tecla, x, y):

    tecla = tecla.decode("utf-8").lower()

    if tecla == 'c':
        global cor
        cor = gerar_cor()
        glut.glutPostRedisplay()


def display():

    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    desenharVasco()

    glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(800, 800)
glut.glutCreateWindow(b"A Insignia de Malta")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(pegar_tecla)
glut.glutMainLoop()