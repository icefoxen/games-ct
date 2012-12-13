# CharbleTwinsty.py
# The main game file
# Yay!


from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

from Input import *
from Drawing import *
from Quaternion import *
from Vector3D import *
from SpaceObj import *
from Ship import *

import Gui

KM = 1000.0
MAXDISTANCE = 1 * KM


# Recall, this gets called every time the OpenGL window gets focus
def initGL( width, height ):
    if height == 0:
        raise Exception( "Height == 0!" )
    
    glViewport( 0, 0, width, height )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    # Make sure the clipping planes are appropriate!
    # Note if min and max distance are too far apart, there
    # could be problems with depth buffer resolution --often 16 bit int.
    gluPerspective( 45, 1.0 * width / height, 1.0, MAXDISTANCE )

    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    glShadeModel( GL_SMOOTH )
    # Black background
    glClearColor( 0.0, 0.0, 0.0, 0.0 )
    glClearDepth( 1.0 )
    glEnable( GL_DEPTH_TEST )
    glDepthFunc( GL_LEQUAL )
    glHint( GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST )

    # Right now we just a default light...
    glLightfv( GL_LIGHT1, GL_AMBIENT, ((0.1, 0.1, 0.1, 0.5)) )
    glLightfv( GL_LIGHT1, GL_DIFFUSE, ((1.0, 1.0, 1.0, 1.0)) )
    glLightfv( GL_LIGHT1, GL_POSITION, ((0.0, 0.0, 0.0, 1.0)) )
    glEnable( GL_LIGHT1 )
    #glEnable( GL_LIGHTING )
    
    glEnable( GL_TEXTURE_2D )
    glColor4f( 1.0, 1.0, 1.0, 1.0 )
    glBlendFunc( GL_SRC_ALPHA, GL_ONE )



    #glPolygonMode( GL_FRONT, GL_LINE )
    #glPolygonMode( GL_BACK, GL_POINT )


def focusCameraOn( objpos, orientationq, distancevec ):
    # We grab the object's rotation matrix...
    matrix = orientationq.toMatrix()
    objvectorx = matrix[0]
    objvectory = matrix[1]
    objvectorz = matrix[2]

    cameratop = objvectory.clone()

    # We turn the angle vectors into offset vectors from
    # the object.
    objvectorx.mulNumber( distancevec.x )
    objvectory.mulNumber( distancevec.y )
    objvectorz.mulNumber( distancevec.z )

    # Now we have an offset vector we can add to the object's position
    # vector
    camerapos = objpos.clone()
    camerapos.addVector( objvectorx )
    camerapos.addVector( objvectory )
    camerapos.addVector( objvectorz )


    # It works!
    gluLookAt( camerapos.x, camerapos.y, camerapos.z, \
               #objvectorx.x, objvectory.y, objvectorz.z,
               objpos.x, objpos.y, objpos.z, \
               cameratop.x, cameratop.y, cameratop.z )



def drawStuff( target, things, effects ):
    offsetvec = Vector3D( 0.0, 5.0, -10.0 )
    
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glLoadIdentity()

    focusCameraOn( target.pos, target.facing, offsetvec )
    #focusCameraOn( s.pos, s.facing, offsetvec )
    for x in things:
        x.draw()
    for x in effects:
        x.draw()



# This reads in the pygame events and sets the key state appropriately.
# Returning False means "we should quit now".  Normally returns True.
# Not the most elegant way of doing it, but oh well.
def handleEvents( event ):
    global KEYSPRESSED
    
    if event.type == KEYDOWN:
        if (event.key == KB_LEFT):
            KEYSPRESSED[KEY_LEFT] = True
        elif (event.key == KB_RIGHT):
            KEYSPRESSED[KEY_RIGHT] = True
        elif (event.key == KB_UP):
            KEYSPRESSED[KEY_UP] = True
        elif (event.key == KB_DOWN):
            KEYSPRESSED[KEY_DOWN] = True
        elif (event.key == KB_FWD):
            KEYSPRESSED[KEY_FWD] = True
        elif (event.key == KB_BACK):
            KEYSPRESSED[KEY_BACK] = True

            
        elif (event.key == KB_YAWN):
            KEYSPRESSED[KEY_YAWN] = True
        elif (event.key == KB_YAWP):
            KEYSPRESSED[KEY_YAWP] = True
        elif (event.key == KB_PITCHP):
            KEYSPRESSED[KEY_PITCHP] = True
        elif (event.key == KB_PITCHN):
            KEYSPRESSED[KEY_PITCHN] = True
        elif (event.key == KB_ROLLP):
            KEYSPRESSED[KEY_ROLLP] = True
        elif (event.key == KB_ROLLN):
            KEYSPRESSED[KEY_ROLLN] = True

        elif event.key == K_q:
            return False

    elif event.type == KEYUP:
        if event.key == KB_LEFT:
            KEYSPRESSED[KEY_LEFT] = False
        elif event.key == KB_RIGHT:
            KEYSPRESSED[KEY_RIGHT] = False
        elif event.key == KB_UP:
            KEYSPRESSED[KEY_UP] = False
        elif event.key == KB_DOWN:
            KEYSPRESSED[KEY_DOWN] = False
        elif event.key == KB_FWD:
            KEYSPRESSED[KEY_FWD] = False
        elif event.key == KB_BACK:
            KEYSPRESSED[KEY_BACK] = False

        elif event.key == KB_YAWN:
            KEYSPRESSED[KEY_YAWN] = False
        elif event.key == KB_YAWP:
            KEYSPRESSED[KEY_YAWP] = False
        elif event.key == KB_PITCHP:
            KEYSPRESSED[KEY_PITCHP] = False
        elif event.key == KB_PITCHN:
            KEYSPRESSED[KEY_PITCHN] = False

        elif event.key == KB_ROLLP:
            KEYSPRESSED[KEY_ROLLP] = False
        elif event.key == KB_ROLLN:
            KEYSPRESSED[KEY_ROLLN] = False

    elif event.type == QUIT:
        return False

    return True

# This is what reads in the keystate set by handleEvents() and
# manipulates the world appropriately.
def handlePlayerEvents( target, t ):
    # Input handling!
    # This does not, in fact, cause the object to go in the right
    # direction.  It moves relative to the world, not itself.
    # I think I can fix that though.
    cameralocinc = 0.05
    if KEYSPRESSED[KEY_LEFT]:
        target.pos.x -= cameralocinc
        print target.pos
    if KEYSPRESSED[KEY_RIGHT]:
        target.pos.x += cameralocinc
        print target.pos
    if KEYSPRESSED[KEY_UP]:
        target.pos.y += cameralocinc
        print target.pos
    if KEYSPRESSED[KEY_DOWN]:
        target.pos.y -= cameralocinc
        print target.pos
    if KEYSPRESSED[KEY_FWD]:
        #target.pos.z -= cameralocinc
        target.thrust( t )
        print target.pos
    if KEYSPRESSED[KEY_BACK]:
        target.pos.z += cameralocinc
        print target.pos


    def doRotation( vector ):
        #target.facing.normalize()
        rotq = Quaternion()
        rotq.fromAxis( -1.0, vector.x, vector.y, vector.z )
        rotq.normalize()
        target.facing = target.facing.mult( rotq )
        target.facing.normalize()
            
    if KEYSPRESSED[KEY_YAWP]:
        doRotation( Vector3D( 1.0, 0.0, 0.0 ) )
    if KEYSPRESSED[KEY_YAWN]:
        doRotation( Vector3D( -1.0, 0.0, 0.0 ) )
    if KEYSPRESSED[KEY_PITCHP]:
        doRotation( Vector3D( 0.0, 1.0, 0.0 ) )
    if KEYSPRESSED[KEY_PITCHN]:
        doRotation( Vector3D( 0.0, -1.0, 0.0 ) )
    if KEYSPRESSED[KEY_ROLLP]:
        doRotation( Vector3D( 0.0, 0.0, 1.0 ) )
    if KEYSPRESSED[KEY_ROLLN]:
        doRotation( Vector3D( 0.0, 0.0, -1.0 ) )




def mainloop():
    # Objects collide with things
    objects = [ Ship(), SpaceObj() ]
    # Effects don't.
    effects = []

    objects[1].moveToXYZ( 10.0, 0.0, 5.0 )

    # What we're aiming the camera at
    target = objects[0]


    then = pygame.time.get_ticks()
    frames = 0
    while True:
        now = pygame.time.get_ticks()
        dt = now - then
        
        event = pygame.event.poll()
        
        if not handleEvents( event ):
            break

        handlePlayerEvents( target, dt )
        for x in objects:
            x.calc( dt )
        for x in effects:
            x.calc( dt )
        drawStuff( target, objects, effects )
        Gui.drawCompass( target )
        Gui.drawVector( target )
        pygame.display.flip()
        frames += 1
        then = now
    return frames

def main():
    videoFlags = OPENGL | DOUBLEBUF
    screenX = 640
    screenY = 480

    pygame.init()
    pygame.display.set_mode( (screenX, screenY), videoFlags )
    initGL( screenX, screenY )

    frames = 0
    ticks = pygame.time.get_ticks()

    frames = mainloop()

    print "FPS: %d" % ((frames * 1000) / (pygame.time.get_ticks() - ticks))

                   

if __name__ == '__main__':
    main()
