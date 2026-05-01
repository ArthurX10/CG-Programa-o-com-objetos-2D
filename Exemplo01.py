import OpenGL.GL as gl  # importa as funções de renderização OpenGL
import OpenGL.GLUT as glut  # importa o GLUT para criar janela e gerenciar eventos


def display():
  glut.glutSwapBuffers()  # troca os buffers quando estiver usando renderização dupla
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # limpa o buffer de cor da janela

  gl.glShadeModel(gl.GL_FLAT)  # define sombreamento plano (cor uniforme por face)
  gl.glBegin(gl.GL_QUADS)  # começa a desenhar um quadrilátero

  gl.glColor3f(-0.5, 1.0, 0.0)  # define a cor do primeiro vértice do quadrado esquerdo
  gl.glVertex3f(-0.9, 0.5, 0.0)  # define o vértice superior esquerdo

  gl.glColor3f(1.0, 0.0, 0.0)  # define a cor do segundo vértice
  gl.glVertex3f(-0.9, -0.5, 0.0)  # define o vértice inferior esquerdo

  gl.glColor3f(0.0, 0.0, 0.0)  # define a cor do terceiro vértice
  gl.glVertex3f(-0.1, -0.5, 0.0)  # define o vértice inferior direito

  gl.glColor3f(0.0, 0.0, 1.0)  # define a cor do quarto vértice
  gl.glVertex3f(-0.1, 0.5, 0.0)  # define o vértice superior direito

  gl.glEnd()  # termina o primeiro quadrilátero

  gl.glShadeModel(gl.GL_SMOOTH)  # define sombreamento suave (cores interpoladas)
  gl.glBegin(gl.GL_QUADS)  # começa o desenho do segundo quadrilátero

  gl.glColor3f(1.0, 0.0, 0.0)  # define a cor do primeiro vértice do segundo quadrado
  gl.glVertex3f(0.1, -0.5, 0.0)  # define o vértice inferior esquerdo

  gl.glColor3f(0.0, 1.0, 0.0)  # define a cor do segundo vértice
  gl.glVertex3f(0.1, 0.5, 0.0)  # define o vértice superior esquerdo

  gl.glColor3f(0.0, 0.0, 1.0)  # define a cor do terceiro vértice
  gl.glVertex3f(0.9, -0.5, 0.0)  # define o vértice inferior direito

  gl.glColor3f(0.0, 0.0, 1.0)  # define a cor do quarto vértice
  gl.glVertex3f(0.9, 0.5, 0.0)  # define o vértice superior direito

  gl.glEnd()  # termina o segundo quadrilátero
  gl.glFlush()  # garante que os comandos OpenGL sejam processados imediatamente


glut.glutInit()  # inicializa o GLUT
glut.glutInitDisplayMode(0)  # define o modo de exibição da janela
glut.glutCreateWindow(b'Exemplo02: Joao Arthur!')  # cria a janela com o título especificado
glut.glutReshapeWindow(800,600)  # ajusta o tamanho da janela para 800x600 pixels
glut.glutDisplayFunc(display)  # registra a função de desenho
glut.glutMainLoop()  # entra no loop principal de eventos do GLUT
