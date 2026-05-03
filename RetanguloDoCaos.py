import OpenGL.GL as gl
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random 

espaco_pressionado = False
numero1 = 1
numero2 = 0
numero3 = 0

def pegar_tecla(key, x, y):
    global espaco_pressionado
    global numero1
    global numero2
    global numero3

    if key == b' ':
        espaco_pressionado = True
        numero1 = random.randint(0, 100) / 100
        numero2 = random.randint(0, 100) / 100
        numero3 = random.randint(0, 100) / 100
    print(numero1, numero2, numero3)

    
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
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    #glColor3f(red, green, blue);
    
    
    #Função para definir o vertice do retângulo, no plano cartesiano
    
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
glut.glutReshapeWindow(800,600)  # ajusta o tamanho da janela para 800x600 pixels

glut.glutKeyboardFunc(pegar_tecla)  # registra a função de teclado
glut.glutDisplayFunc(display)  # registra a função de desenho
glut.glutMainLoop()  
