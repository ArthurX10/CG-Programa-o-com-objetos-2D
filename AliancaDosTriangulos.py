import OpenGL.GL as gl
import OpenGL.GLUT as glut 

# triangulo isosceles, com base e altura fornecidas pelo 
# usuário, em seguida, deve desenhar pelo menos 5 triangulos com diferentes tamanhos e em posições em tela, cada triangulo tem que ter uma cor diferente.


def ler_pontos():
    print("Digite as Dimensôes do Triângulo Isósceles (Aceito Valores de -1.0 a 1.0)")
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))

    return base, altura

base, altura = ler_pontos()


def display():
    glut.glutSwapBuffers()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_TRIANGLES)


    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex2f(0.0, altura)
    gl.glVertex2f(base, 0)
    gl.glVertex2f(-base, 0)

    gl.glEnd()
    gl.glFlush()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Alianca dos Triangulos')
glut.glutReshapeWindow(800, 800)
glut.glutDisplayFunc(display)
glut.glutMainLoop() 



