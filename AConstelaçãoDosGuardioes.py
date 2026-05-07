import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

import random
import math


modo_noturno = False
cor_fundo = [0.05, 0.05, 0.15]
constelacao = []


class Estrela:

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(50, 750)
        self.y = y if y is not None else random.randint(50, 550)
        self.raio = random.randint(8, 20)
        self.cor = gerar_cor()
    def modo_noturno(self, ativo):

        if ativo:
            self.cor = [1.0, 1.0, 0.7]
        else:
            self.cor = gerar_cor()


def gerar_cor():

    return [
        random.random(),
        random.random(),
        random.random()
    ]


def desenhar_circulo(x, y, raio):

    segmentos = 50

    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(x, y)

    for i in range(segmentos + 1):
        angulo = 2 * math.pi * i / segmentos
        px = x + math.cos(angulo) * raio
        py = y + math.sin(angulo) * raio

        gl.glVertex2f(px, py)

    gl.glEnd()


def desenhar_constelacao():

    # linhas
    gl.glColor3f(0.7, 0.7, 0.7)

    gl.glLineWidth(2)

    gl.glBegin(gl.GL_LINES)

    for i in range(len(constelacao) - 1):

        gl.glVertex2f(constelacao[i].x, constelacao[i].y)

        gl.glVertex2f(constelacao[i + 1].x, constelacao[i + 1].y)

    gl.glEnd()

    # estrelas
    for estrela in constelacao:

        gl.glColor3f(*estrela.cor)

        desenhar_circulo(
            estrela.x,
            estrela.y,
            estrela.raio
        )


def reiniciar_constelacao():

    global constelacao
    constelacao = [Estrela() for _ in range(7)]

    if modo_noturno:
        for estrela in constelacao:
            estrela.modo_noturno(True)


def teclado(tecla, x, y):

    global modo_noturno
    global cor_fundo

    tecla = tecla.decode("utf-8").lower()

    
    if tecla == 'n':
        nova_estrela = Estrela()
        if modo_noturno:
            nova_estrela.modo_noturno(True)
        constelacao.append(nova_estrela)

    elif tecla == 'x':
        if constelacao:
            indice = random.randrange(len(constelacao))
            constelacao.pop(indice)


    elif tecla == 'r':
        reiniciar_constelacao()
    
    elif tecla == 't':
        modo_noturno = not modo_noturno
        if modo_noturno:
            cor_fundo = [0.0, 0.0, 0.0]
        else:
            cor_fundo = [0.05, 0.05, 0.15]
        for estrela in constelacao:
            estrela.modo_noturno(modo_noturno)


    elif tecla == chr(27):
        glut.glutLeaveMainLoop()
    glut.glutPostRedisplay()



def display():

    gl.glClearColor(*cor_fundo, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    desenhar_constelacao()
    glut.glutSwapBuffers()


def init():

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0, 800, 0, 600)
    gl.glMatrixMode(gl.GL_MODELVIEW)


def main():

    print("\n CONSTELAÇÃO DOS GUARDIÕES \n")

    print("N - Nova estrela")
    print("X - Remover estrela")
    print("R - Reiniciar constelação")
    print("T - Alternar modo noturno")
    print("ESC - Sair")

    reiniciar_constelacao()

    glut.glutInit()

    glut.glutInitDisplayMode(
        glut.GLUT_DOUBLE | glut.GLUT_RGB
    )
    glut.glutInitWindowSize(800, 600)
    glut.glutCreateWindow(b"Constelacao dos Guardioes")

    init()
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(teclado)
    glut.glutMainLoop()


if __name__ == "__main__":
    main()