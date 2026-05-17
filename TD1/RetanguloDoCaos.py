import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random 

espaco_pressionado = False
cor_retangulo = [1, 1, 0]
cor_fundo = [1, 1, 1]


def gerar_cor():
    return [random.random(), random.random(), random.random()]

def pegar_tecla(key, x, y):

    if key == b' ':
        global cor_retangulo 
        global cor_fundo
        cor_retangulo = gerar_cor()
        cor_fundo = gerar_cor()

    
    glut.glutPostRedisplay()


def ler_pontos():
    print("Digite as Dimensôes do Retângulo (Aceito Valores de 0.0r a 1.0)")
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    if largura <= 0 or largura > 1.0 or altura <= 0 or altura > 1.0:
        print("Valores inválidos! Por favor, insira valores entre 0.0 e 1.0.")
        return ler_pontos()

    
    return largura, altura

largura, altura = ler_pontos()

def display():

    gl.glClearColor(*cor_fundo, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    
    # vértices do retângulo
    gl.glColor3f(*cor_retangulo)
    gl.glVertex2f(-largura/2, altura/2)
    gl.glVertex2f(-largura/2, -altura/2)
    gl.glVertex2f(largura/2, -altura/2)
    gl.glVertex2f(largura/2, altura/2)


    gl.glEnd()
    gl.glFlush()


glut.glutInit() 
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB) 
glut.glutCreateWindow(b'Retangulo do Caos') 
glut.glutReshapeWindow(800,800) 
glut.glutKeyboardFunc(pegar_tecla) 
glut.glutDisplayFunc(display)
glut.glutMainLoop()  
