import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random

cor = [1.0, 0.0, 0.0]

def gerar_cor():
   return [random.random(), random.random(), random.random()]

def desenharInsignia():

    gl.glColor3f(*cor)
    gl.glBegin(gl.GL_QUADS)

    #CRUZ A
    gl.glVertex2f(-0.3, 0.7)
    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.3, 0.7)
    gl.glVertex2f(0.0, 0.5)
    
    #CRUZ B
    gl.glVertex2f(-0.7, 0.3)
    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(-0.7, -0.3)
    gl.glVertex2f(-0.5, 0.0)
   
   #CRUZ C
    gl.glVertex2f(0.3, -0.7)
    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(-0.3, -0.7)
    gl.glVertex2f(0.0, -0.5)

    #CRUZ D
    gl.glVertex2f(0.7, -0.3)
    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.7, 0.3)
    gl.glVertex2f(0.5, 0.0)

    gl.glEnd()
    gl.glFlush()
    

def pegar_tecla(tecla, x, y):
    tecla = tecla.decode("utf-8").lower()

    if tecla == 'c':
        global cor
        cor = gerar_cor()
        glut.glutPostRedisplay()


def display():

    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    desenharInsignia()
    glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(800, 800)
glut.glutCreateWindow(b"A Insignia de Malta")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(pegar_tecla)
glut.glutMainLoop()