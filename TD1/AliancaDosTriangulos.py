import OpenGL.GL as gl
import OpenGL.GLUT as glut


def ler_pontos():
    print("Digite as Dimensões do Triângulo Isósceles (Valores de -1.0 a 1.0)")
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    return base, altura


base, altura = ler_pontos()


def desenhar_triangulo(base, altura, cor,cx = 0.0, cy=0.0):
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(*cor) 
    gl.glVertex2f(cx, cy + altura)
    gl.glVertex2f(cx + base, cy)
    gl.glVertex2f(cx - base, cy)

    gl.glEnd()


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    desenhar_triangulo(base, altura, (1.0, 0.0, 0.0))
    desenhar_triangulo(0.15, 0.20, (0.0, 1.0, 0.0), -0.70, 0.60)
    desenhar_triangulo(0.10, 0.30, (0.0, 0.0, 1.0), 0.70, 0.55)
    desenhar_triangulo(0.20, 0.15, (1.0, 1.0, 0.0), -0.65, -0.75)
    desenhar_triangulo(0.12, 0.25, (0.0, 1.0, 1.0), 0.65, -0.70)
    desenhar_triangulo(0.18, 0.22, (1.0, 0.0, 1.0), 0.0, 0.65)

    glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutCreateWindow(b'Alianca dos Triangulos')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()









