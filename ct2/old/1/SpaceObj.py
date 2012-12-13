# SpaceObj.py
# An object in space!


from OpenGL.GL import *
from OpenGL.GLU import *

from TextureLoader import *
from Quaternion import *
from Vector3D import *


class SpaceObj:
    # I use () to say "an object's gonna be here".
    # Units are meters.
    # Position
    pos = ()
    # Facing quaternion
    facing = ()
    # Movement vector
    heading = ()

    # Physical properties
    mass = 0.0
    hits = 0
    radius = 0.0

    _boundingSphereRadius = 0.0
    _boundingSphereLoc = Vector3D()

    # Hm, how do I get a display list of a quadric?
    # Same as anything else?  No.  Hm.
    # How are we going to store these models, anyway?
    # Ah, we won't.  Excellent!
    #_displayList = ()
    
    # Dunno how textures will work yet.
    _texture = ()


    def __init__( s ):
        s.pos = Vector3D()
        s.facing = Quaternion()
        s.heading = Vector3D()

        s.hits = 1
        s.mass = 1
        s.radius = 1.0


    # t is in milliseconds.  heading is the vector in meters per second.
    def calc( s, t ):
        dist = s.clone()
        dist.mulNumber( t / 1000.0 )
        s.pos.addVector( dist )

        #s._boundingSphereRadius = s.heading.magnitude() / 2.0
        #s._boundingSphereLoc = 
        
        if s.hits == 0:
            s.die()

    def die( s ):
        return

    # Do damage relative to mass and speed...
    def impact( s ):
        return


    # Our collision detection routine is a bit funky
    # First, we make a big bounding sphere, as wide as the heading
    # vector's length, and make sure nothing collides with that.
    # Then, if something does, we sweep the bounding sphere along the
    # length of the heading vector, checking every 1 radius to see if
    # anything's gotten hit.
    # Oriented bounding boxes might be better, but I don't care to
    # write 'em right now.
    def isColliding( s, obj, time ):
        
        
        return false


    def draw( s ):
        quad = gluNewQuadric()
        gluQuadricNormals( quad, GLU_SMOOTH )
        gluQuadricTexture( quad, GL_FALSE )
        

        glTranslate( s.pos.x, s.pos.y, s.pos.z )
        glColor3f( 0.0, 1.0, 0.0 )
        gluCylinder( quad, s.radius, 0, s.radius, 32, 32 )
        gluQuadricOrientation( quad, GLU_INSIDE )
        #size = s.radius - 0.01
        #gluCylinder( quad, size, 0, size, 32, 32 )

        # glRotatef( )
        # glBindTexture( )
        

    def moveTo( s, v ):
        s.pos = v

    def moveToXYZ( s, x, y, z ):
        s.pos.x = x
        s.pos.y = y
        s.pos.z = z

    def accelerate( s, v ):
        s.heading.addVector( v )

    def rotateQ( s, q ):
        s.facing.mult( q )

    def setFacingToQ( s, q ):
        s.facing = q
