import OpenGL.GL as gl
import OpenGL.GLUT as glut


 # def pegar_tecla(key, x, y):
    #if key == b' ':

def ler_pontos():
    print("Digite as Dimensôes do Retângulo (Aceito Valores de -1.0 a 1.0)")
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    return largura, altura

largura, altura = ler_pontos()

def display():
    
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    #glColor3f(red, green, blue);
    #gl.glColor3f(1,0, 0.0, 0.0)
    
    #Função para definir o vertice do retângulo, no plano cartesiano
    
    # vértices do retângulo
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
glut.glutDisplayFunc(display)  # registra a função de desenho
glut.glutMainLoop()  
