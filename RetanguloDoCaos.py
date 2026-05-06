import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random 

espaco_pressionado = False
numero1 = 1
numero2 = 0
numero3 = 0 
numeroFundo1 = 0.3
numeroFundo2 = 0.3
numeroFundo3 = 0.3

def cor_random():
    return random.random() 

def pegar_tecla(key, x, y):
    global numero1, numero2, numero3
    global numeroFundo1, numeroFundo2, numeroFundo3

    if key == b' ':
        numero1 = cor_random()
        numero2 = cor_random()
        numero3 = cor_random()
        numeroFundo1 = cor_random()
        numeroFundo2 = cor_random()
        numeroFundo3 = cor_random()   

    
    glut.glutPostRedisplay();


def ler_pontos():
    print("Digite as Dimensôes do Retângulo (Aceito Valores de -1.0 a 1.0)")
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    if largura <= -1.0 or largura >= 1.0 or altura <= -1.0 or altura >= 1.0:
        print("Valores inválidos! Por favor, insira valores entre -1.0 e 1.0.")
        return ler_pontos()

    
    return largura, altura

largura, altura = ler_pontos()

def display():

    gl.glClearColor(numeroFundo1, numeroFundo2, numeroFundo3, 1.0)


    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    
    
    # vértices do retângulo
    gl.glColor3f(numero1, numero2, numero3)
    gl.glVertex2f(-largura, altura)
    gl.glVertex2f(-largura, -altura)
    gl.glVertex2f(largura, -altura)
    gl.glVertex2f(largura, altura)


    gl.glEnd()
    gl.glFlush()


glut.glutInit()  # inicializa o GLUT
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)  # define o modo de exibição da janela
glut.glutCreateWindow(b'Retangulo do Caos')  # cria a janela com o título especificado
glut.glutReshapeWindow(800,800)  # ajusta o tamanho da janela para 800x600 pixels

glut.glutKeyboardFunc(pegar_tecla)  # registra a função de teclado
glut.glutDisplayFunc(display)  # registra a função de desenho
glut.glutMainLoop()  
