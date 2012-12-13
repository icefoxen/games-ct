# MeshLoader.py
# Um...yeah.

from OpenGL.GL import *
from OpenGL.GLU import *


def getCube( size ):
    displayList = glGenLists( 1 )
    glNewList( displayList, GL_COMPILE )
    glBegin( GL_QUADS )

    glNormal3f( 0.0, 0.0, 1.0 )

    glColor3f( 1.0, 0.0, 0.0 )
    glVertex3f( 0.0, 0.0, 0.0 )
    glVertex3f( 0.0, size, 0.0 )
    glVertex3f( size, size, 0.0 )
    glVertex3f( size, 0.0, 0.0 )

    glColor3f( 0.0, 1.0, 0.0 )
    glVertex3f( 0.0, 0.0, -size )
    glVertex3f( size, 0.0, -size )
    glVertex3f( size, size, -size )
    glVertex3f( 0.0, size, -size )

    glEnd()
    glEndList()

    return displayList

def drawCube( size ):
    glBegin( GL_QUADS )

    glNormal3f( 0.0, 0.0, 1.0 )

    glColor3f( 1.0, 0.0, 0.0 )
    glVertex3f( 0.0, 0.0, 0.0 )
    glVertex3f( 0.0, size, 0.0 )
    glVertex3f( size, size, 0.0 )
    glVertex3f( size, 0.0, 0.0 )

    glColor3f( 0.0, 1.0, 0.0 )
    glVertex3f( 0.0, 0.0, -size )
    glVertex3f( size, 0.0, -size )
    glVertex3f( size, size, -size )
    glVertex3f( 0.0, size, -size )

    glEnd()
    

def getReferenceObject( size ):
    displayList = glGenLists( 3 )
    q = gluNewQuadric()
    gluQuadricNormals( q, GLU_SMOOTH )
    gluQuadricTexture( q, GL_TRUE )
    
    glNewList( displayList, GL_COMPILE )
    
    glEnable( GL_BLEND )
    glDisable( GL_DEPTH_TEST )

    glColor4f( 1.0, 0.0, 0.0, 0.1 )
    gluDisk( q, 0, size, 32, 32 )
    glRotatef( 90.0, 1.0, 0.0, 0.0 )

    glColor4f( 0.0, 0.0, 1.0, 0.1 )
    gluDisk( q, 0, size, 32, 32 )
    glRotatef( 90.0, 0.0, 1.0, 0.0 )

    glColor4f( 0.0, 1.0, 0.0, 0.1 )
    gluDisk( q, 0, size, 32, 32 )

    glDisable( GL_BLEND )
    glEnable( GL_DEPTH_TEST )
    
    glEndList()
    
    return displayList


def drawReferenceObject( size ):
    q = gluNewQuadric()
    gluQuadricNormals( q, GLU_SMOOTH )
    gluQuadricTexture( q, GL_TRUE )
    
    #glEnable( GL_BLEND )
    #glDisable( GL_DEPTH_TEST )

    glColor4f( 0.5, 0.0, 0.0, 0.1 )
    gluDisk( q, 0, size, 32, 32 )
    glRotatef( 90.0, 1.0, 0.0, 0.0 )

    glColor4f( 0.0, 0.0, 0.5, 0.1 )
    gluDisk( q, 0, size, 32, 32 )
    glRotatef( 90.0, 0.0, 1.0, 0.0 )

    glColor4f( 0.0, 0.5, 0.0, 0.1 )
    gluDisk( q, 0, size, 32, 32 )

    #glDisable( GL_BLEND )
    #glEnable( GL_DEPTH_TEST )
