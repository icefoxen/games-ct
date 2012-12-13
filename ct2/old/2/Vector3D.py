# Vectors!
# In three dimensions!

from math import *

class Vector3D:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__( s, x=0.0, y=0.0, z=0.0 ):
        s.set( x, y, z )

    def clone( s ):
        return Vector3D( s.x, s.y, s.z )

    def __repr__( s ):
        return "<%f, %f, %f>" % (s.x, s.y, s.z)

    # Moves a (position) vector absolutely
    def set( s, x, y, z ):
        s.x = x
        s.y = y
        s.z = z

    # Moves a (position) vector relative to itself
    def addNumber( s, d ):
        s.x += d
        s.y += d
        s.z += d

    # Increases the magnitude of the vector
    def mulNumber( s, d ):
        s.x *= d
        s.y *= d
        s.z *= d

    def addVector( s, v ):
        s.x += v.x
        s.y += v.y
        s.z += v.z

    def invert( s ):
        s.x *= -1.0
        s.y *= -1.0
        s.z *= -1.0

    def magnitude( s ):
        return sqrt( (s.x * s.x) + (s.y * s.y) + (s.z * s.z) )

    
    def normalize( s ):
        magnitude = sqrt( (s.x * s.x) +
                          (s.y * s.y) + (s.z * s.z) )
        if magnitude == 0.0:
            print "MAG: " + str( magnitude )
            magnitude = 1.0
        s.x = s.x / magnitude
        s.y = s.y / magnitude
        s.z = s.z / magnitude
