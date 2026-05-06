import OpenGL.GL as gl 
import OpenGL.GLUT as glut

def gerar_coordenadas(x, y, text):
    
    gl.glRasterPos2f(x,y)
    for char in text:
        glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(char))


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
    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)
    gl.glVertex2f(0.0, -1.0)   
    gl.glVertex2f(0.0, 1.0)

    gl.glEnd()

    gl.glRasterPos2f(0.95, 0.05)
    glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord('X'))

    gl.glRasterPos2f(0.05, 0.95)
    glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord('Y'))

    #Coordenadas do Triangulo A
    gerar_coordenadas(-0.83, 0.83, "A(-0.8, 0.8)")
    gerar_coordenadas(-0.8, 0.15, "B(-0.8, 0.2)")
    gerar_coordenadas(-0.2, 0.15, "C(-0.2, 0.2)")

    #Coordenadas do Triangulo B
    gerar_coordenadas(0.8, 0.8, "A(0.8, 0.8)")
    gerar_coordenadas(0.8, 0.15, "B(0.8, 0.15)")
    gerar_coordenadas(0.2, 0.15, "C(0.2, 0.2)")

    #Coordenadas do Triangulo C
    gerar_coordenadas(0.0, -0.2, "A(0.0, -0;2)")
    gerar_coordenadas(-0.7, -0.75, "B(-0.7, -0.7)")
    gerar_coordenadas(0.6, -0.75, "C(0.7, 0.7)")



    

    
    gl.glFlush()
    

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutCreateWindow(b'O Dominio do Espaco')
glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
