
import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

CUBE_POINTS = (
    (0.5, -0.5, -0.5),  (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),  (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),   (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),  (-0.5, 0.5, 0.5)
)

CUBE_COLORS = (
    (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0),
    (1, 0, 1), (1, 1, 1), (0, 0, 1), (0, 1, 1)
)

CUBE_QUAD_VERTS = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
    (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6)
)

CUBE_EDGES = (
    (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7), (5,1), (5,4), (5,7),
)



def drawcube():
	"draw the cube"
	allpoints = list(zip(CUBE_POINTS, CUBE_COLORS))

	glBegin(GL_QUADS)
	for face in CUBE_QUAD_VERTS:
		for vert in face:
			pos, color = allpoints[vert]
			glColor3fv(color)
			glVertex3fv(pos)
	glEnd()

	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_LINES)
	for line in CUBE_EDGES:
		for vert in line:
			pos, color = allpoints[vert]
			glVertex3fv(pos)

	glEnd()

def draw_pie(point_list,color,thick):
	list_top=[]
	list_bottom=[]
	for i in point_list:
		list_top.append((i[0],i[1],thick))
		list_bottom.append((i[0],i[1],-thick))
	glBegin(GL_QUAD_STRIP)
	glColor3fv(color)
	for (i,j) in zip(list_top,list_bottom):
		glVertex3fv(i)
		glVertex3fv(j)
	glVertex3fv(list_top[0])
	glVertex3fv(list_bottom[0])
	glEnd()
	glBegin(GL_POLYGON)
	for i in list_top:
		glVertex3fv(i)
	glEnd()
	glBegin(GL_POLYGON)
	for i in list_bottom:
		glVertex3fv(i)
	glEnd()
	
	glBegin(GL_LINE_LOOP)
	glColor3fv((1.,1.,1.))
	for i in list_top:
		glVertex3fv(i)
	glEnd()
	glBegin(GL_LINE_LOOP)
	for i in list_bottom:
		glVertex3fv(i)
	glEnd()
	glBegin(GL_LINES)
	for (i,j) in zip(list_top,list_bottom):
		glVertex3fv(i)
		glVertex3fv(j)
	glEnd()

def draw_ubi(x,y,a0,a1,rs,re):
	list_top1=[]
	list_top2=[]
	list_bottom1=[]
	list_bottom2=[]
	color=(1, 1, 1)
	for i in range(a0,a1+10,10):
		angle=i*math.pi/180
		r1=rs-(i-a0)/(a1-a0)*(rs-re)
		r2=r1-0.1
		list_top1.append((x+r1*math.cos(angle),y+r1*math.sin(angle),0.1))
		list_top2.append((x+r2*math.cos(angle),y+r2*math.sin(angle),0.1))
		list_bottom1.append((x+r1*math.cos(angle),y+r1*math.sin(angle),-0.1))
		list_bottom2.append((x+r2*math.cos(angle),y+r2*math.sin(angle),-0.1))
	list_top2.reverse()
	list_bottom2.reverse()
	glBegin(GL_QUAD_STRIP)
	glColor3fv(color)
	for (i,j) in zip(list_top1,list_bottom1):
		glVertex3fv(i)
		glVertex3fv(j)	
	for (i,j) in zip(list_top2,list_bottom2):
		glVertex3fv(i)
		glVertex3fv(j)
	glVertex3fv(list_top1[0])
	glVertex3fv(list_bottom1[0])	
	glEnd()	
	
	list_top2.reverse()
	list_bottom2.reverse()
	glBegin(GL_QUAD_STRIP)
	for (i,j) in zip(list_top1,list_top2):
		glVertex3fv(i)
		glVertex3fv(j)
	glEnd()
	glBegin(GL_QUAD_STRIP)
	for (i,j) in zip(list_bottom1,list_bottom2):
		glVertex3fv(i)
		glVertex3fv(j)
	glEnd()
	
	glBegin(GL_LINE_STRIP)
	glColor3fv((0.5,0.5,0.5))
	for i in zip(list_top1):
		glVertex3fv(i)
	glEnd()
	glBegin(GL_LINE_STRIP)
	for i in zip(list_top2):
		glVertex3fv(i)
	glEnd()
	glBegin(GL_LINE_STRIP)
	for i in zip(list_bottom1):
		glVertex3fv(i)
	glEnd()
	glBegin(GL_LINE_STRIP)
	for i in zip(list_bottom2):
		glVertex3fv(i)
	glEnd()  

def main():
	"run the demo"
	pygame.init()
	pygame.display.set_mode((640,480), OPENGL|DOUBLEBUF)
	glEnable(GL_DEPTH_TEST)     

	glMatrixMode(GL_PROJECTION)
	gluPerspective(45.0,640/480.0,0.5,100.0)  
	glTranslatef(0.0, 0.0, -3.0)               

	while 1:
		event = pygame.event.poll()
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			break
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glRotatef(1, 0, 1, 0)                    

#       drawcube()
#		draw_pie([(math.cos(a*math.pi/180),math.sin(a*math.pi/180)) for a in range(0,360,10)],(0.5, 0.4, 0.8),0.1)
		draw_ubi(0,0,-40,380,0.2,0.3)
		draw_ubi(-0.11,-0.11,20,250,0.43,0.43)
		draw_ubi(-0.2,0.05,-20,270,0.5,0.57)
		draw_ubi(-0.1,0.05,-150,30,0.5,0.8)
		draw_ubi(-0.1,0.05,30,140,0.8,0.7)
		pygame.display.flip()
		pygame.time.wait(10)


if __name__ == '__main__': main()
