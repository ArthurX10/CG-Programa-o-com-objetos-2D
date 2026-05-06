import OpenGL.GL as gl 
import OpenGL.GLUT as glut 


def display():
    glut.glutSwapBuffers()

    
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_TRIANGLES)

    #Triangulo A 
    gl.glColor3f(1.0,0.0,0.0)
    gl.glVertex2f(-0.8, 0.8)
    gl.glVertex2f(-0.8, 0.2)
    gl.glVertex2f(-0.2, 0.2)

    #Triangulo B
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex2f(0.8,0.8)
    gl.glVertex2f(0.2, 0.2)
    gl.glVertex2f(0.8, 0.2)


    #Triangulo C
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex2f(0.0, -0.2)
    gl.glVertex2f(-0.7, -0.7)
    gl.glVertex2f(0.7, -0.7)

    gl.glEnd()

    #Desenhar o Plano cartesiano eixo X e y 

    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(1.0, 1.0, 1.0)
    gl.glVertex3f(-1.0, 0.0, 0.0)
    gl.glVertex3f(1.0, 0.0, 0.0)
    gl.glVertex3f(0.0, -1.0, 0.0)   
    gl.glVertex3f(0.0, 1.0, 0.0)

    gl.glEnd()


    glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord('Eixo X'))
    
    gl.glFlush()
    

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutCreateWindow(b'Painel de Formas')
glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
