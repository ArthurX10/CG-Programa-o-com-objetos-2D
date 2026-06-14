import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cubo as cubo_mod
import teapot as teapot_mod
import sphere as sphere_mod
import plano as plano_mod
from camera import Camera

WIDTH, HEIGHT = 800, 600

plano_obj  = plano_mod.Plano()
cubo_obj   = cubo_mod.Cubo()
teapot_obj = teapot_mod.Teapot()
sphere_obj = sphere_mod.Sphere(0.5, 32, 32)
camera     = Camera(WIDTH, HEIGHT)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.15, 0.15, 0.15, 1.0])


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.apply()  

    plano_obj.draw()
    cubo_obj.draw()
    sphere_obj.draw(0, 0.5, 0)
    teapot_obj.draw()

    glutSwapBuffers()


def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w / h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Sintese de Imagens")

init()

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(camera.keyboard)
glutMouseFunc(camera.mouse)
glutMotionFunc(camera.motion)
glutMainLoop()