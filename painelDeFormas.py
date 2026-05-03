import OpenGL.GL as gl 
import OpenGL.GLUT as glut
import numpy as np




def display():
    glut.glutSwapBuffers()
    # desenhar 4 formas (quadrado, triangulo, circulo e +1) cores variadas 


    #quadrado 
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    gl.glColor3f(1.0,0.0,0.0)
    gl.glVertex2f(-0.8, 0.8)
    gl.glVertex2f(-0.8, 0.2)
    gl.glVertex2f(-0.2, 0.2)
    gl.glVertex2f(-0.2, 0.8)

    gl.glEnd()
    


    #Triangulo 
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0.0,1.0,0.0)
    gl.glVertex2f(0.2, -0.2)
    gl.glVertex2f(0.2, -0.8)
    gl.glVertex2f(0.8, -0.8)

    gl.glEnd()





    #Circulo 
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glColor3f(0.0,0.0,1.0)

    x = 0.5
    y= 0.5
    raio = 0.3
    segments = 1000

    gl.glVertex2f(x, y)
    for i in range(segments + 1):
        angle = 2 * np.pi * i/segments
        gl.glVertex2f(x + np.cos(angle) * raio,
                      y + np.sin(angle) * raio)
    gl.glEnd()


    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1.0,1.0,0.0)
    gl.glVertex2f(-0.5, -0.1)
    gl.glVertex2f(-0.2, -0.3)
    gl.glVertex2f(-0.5, -0.8)
    gl.glVertex2f(-0.8, -0.3)
    
    gl.glEnd()
    gl.glFlush()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Painel de Formas')
glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(display)
glut.glutMainLoop()