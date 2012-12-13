# Gui!
# Gods this is gonna be twisty...

from OpenGL.GL import *
from OpenGL.GLU import *

from Drawing import *
from SpaceObj import *

compassOffset = Vector3D( 2.5, 0.0, -4.80 )
vectorOffset = Vector3D( -2.5, 0.0, -4.80 )

def drawCompass( obj ):
    matrix = obj.facing.toMatrix()

    compassx = matrix[0]
    compassy = matrix[1]
    compassz = matrix[2]

    compassx.mulNumber( compassOffset.x )
    compassy.mulNumber( compassOffset.y )
    compassz.mulNumber( compassOffset.z )

    compasspos = obj.pos.clone()
    compasspos.addVector( compassx )
    compasspos.addVector( compassy )
    compasspos.addVector( compassz )
    
    glPushMatrix()
    glTranslate( compasspos.x, compasspos.y, compasspos.z )
    drawReferenceObject( 0.2 )
    glPopMatrix()




def drawVector( obj ):
    matrix = obj.facing.toMatrix()

    vectorx = matrix[0]
    vectory = matrix[1]
    vectorz = matrix[2]

    vectorx.mulNumber( vectorOffset.x )
    vectory.mulNumber( vectorOffset.y )
    vectorz.mulNumber( vectorOffset.z )

    vectorpos = obj.pos.clone()
    vectorpos.addVector( vectorx )
    vectorpos.addVector( vectory )
    vectorpos.addVector( vectorz )

    glPushMatrix()
    glTranslate( vectorpos.x, vectorpos.y, vectorpos.z )
    
    drawVectorObject( 0.1, obj.heading.x, obj.heading.y, obj.heading.z )

    #theta, vec = obj.facing.toAxis()
    #glRotatef( theta, vec.x, vec.y, vec.z )
    #drawReferenceObject( 0.5 )
    
    glPopMatrix()
