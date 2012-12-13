# Quaternions
# They may or may not let me rotate stuff around my own axis,
# instead of OpenGL's
# Or whatever.
# Either way, time for a mathematical leap of faith.
# If it doesn't work, I'll just devour Mjolnir's soul.
#
# OpenGL likes degrees, so everything's given in degrees.
# But we use sin and cos and shit, so we turn it into radians
# internally.
#
# Euler	
# glRotatef( angleX, 1, 0, 0)
# glRotatef( angleY, 0, 1, 0)
# glRotatef( angleZ, 0, 0, 1)
# // translate

# Quaternion	
# // convert Euler to quaternion
# // convert quaternion to axis angle
# glRotate(theta, ax, ay, az)
# // translate

## Q54. How do I convert a quaternion to a rotation matrix?
## --------------------------------------------------------

##   Assuming that a quaternion has been created in the form:

##     Q = |X Y Z W|

##   Then the quaternion can then be converted into a 4x4 rotation
##   matrix using the following expression:


##         |       2     2                                |
##         | 1 - 2Y  - 2Z    2XY - 2ZW      2XZ + 2YW     |
##         |                                              |
##         |                       2     2                |
##     M = | 2XY + 2ZW       1 - 2X  - 2Z   2YZ - 2XW     |
##         |                                              |
##         |                                      2     2 |
##         | 2XZ - 2YW       2YZ + 2XW      1 - 2X  - 2Y  |
##         |                                              |


##   If a 4x4 matrix is required, then the bottom row and right-most column
##   may be added.

##   The matrix may be generated using the following expression:

##     ----------------

##     xx      = X * X;
##     xy      = X * Y;
##     xz      = X * Z;
##     xw      = X * W;

##     yy      = Y * Y;
##     yz      = Y * Z;
##     yw      = Y * W;

##     zz      = Z * Z;
##     zw      = Z * W;

##     mat[0]  = 1 - 2 * ( yy + zz );
##     mat[1]  =     2 * ( xy - zw );
##     mat[2]  =     2 * ( xz + yw );

##     mat[4]  =     2 * ( xy + zw );
##     mat[5]  = 1 - 2 * ( xx + zz );
##     mat[6]  =     2 * ( yz - xw );

##     mat[8]  =     2 * ( xz - yw );
##     mat[9]  =     2 * ( yz + xw );
##     mat[10] = 1 - 2 * ( xx + yy );

##     mat[3]  = mat[7] = mat[11 = mat[12] = mat[13] = mat[14] = 0;
##     mat[15] = 1;

##     ----------------

## Create a quaternion that turns a vector to face the same way as
## another vector.
##         Quaternion getRotationTo(const Vector3& dest) const
##         {
##             // Based on Stan Melax's article in Game Programming Gems
##             Quaternion q;
##             // Copy, since cannot modify local
##             Vector3 v0 = *this;
##             Vector3 v1 = dest;
##             v0.normalise();
##             v1.normalise();
##             Vector3 c = v0.crossProduct(v1);
##             // NB if the crossProduct approaches zero, we get unstable because 
##     ANY axis will do
##             // when v0 == -v1
##             Real d = v0.dotProduct(v1);
##             // If dot == 1, vectors are the same
##             if (d >= 1.0f)
##             {
##                 return Quaternion::IDENTITY;
##             }
##             Real s = Math::Sqrt( (1+d)*2 );
##             assert (s != 0 && "Divide by zero!");
##             Real invs = 1 / s;
##             q.x = c.x * invs;
##             q.y = c.y * invs;
##             q.z = c.z * invs;
##             q.w = s * 0.5;
##             return q;
##         }




from math import *
from Vector3D import *


def d2r( x ):
    return x * pi / 180.0

class Quaternion:
    w = 0.0
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__( s, w=1.0, x=0.0, y=0.0, z=0.0 ):
        s.w = w
        s.x = x
        s.y = y
        s.z = z

    def normalize( s ):
        magnitude = sqrt( (s.w * s.w) + (s.x * s.x) +
                          (s.y * s.y) + (s.z * s.z) )
        s.w = s.w / magnitude
        s.x = s.x / magnitude
        s.y = s.y / magnitude
        s.z = s.z / magnitude


    def mult( s, q ):
        nw = (s.w * q.w) - (s.x * q.x) - (s.y * q.y) - (s.z * q.z)
        nx = (s.w * q.x) + (s.x * q.w) + (s.y * q.z) - (s.z * q.y)
        ny = (s.w * q.y) - (s.x * q.z) + (s.y * q.w) + (s.z * q.x)
        nz = (s.w * q.z) + (s.x * q.y) - (s.y * q.x) + (s.z * q.w)
        return Quaternion( nw, nx, ny, nz )
          

    def fromAxis( s, fangle, x, y, z ):
        x = d2r( x )
        y = d2r( y )
        z = d2r( z )
        
        s.w = cos( fangle / 2 )
        sf = sin( fangle / 2 )
        s.x = x * sf
        s.y = y * sf
        s.z = z * sf

    def toAxis( s ):
        scale = sqrt( (s.x * s.x) + (s.y * s.y) + (s.z * s.z) )
        if scale == 0:
            return (0, Vector3D( 1.0, 1.0, 1.0 ))
        v = Vector3D()
        v.x = s.x * scale
        v.y = s.y * scale
        v.z = s.z * scale
        # This occasionally gives us a domain error.
        # s.w cannot be > 1.  Not even 1.0000000000001.
        try:
            if s.w > 1.0:
                s.w = 1.0
            angle = 2 * acos( s.w )
        except:
            print "ERROR ON s.w = %f" % s.w
        return (angle * 180/pi, v)

    def conjugate( s ):
        return Quaternion( s.w, -s.x, -s.y, -s.z )

    def toMatrix( s ):
        matrix = [Vector3D(), Vector3D(), Vector3D()]
                  
        xx = s.x * s.x
        xy = s.x * s.y
        xz = s.x * s.z
        xw = s.x * s.w
        
        yy = s.y * s.y
        yz = s.y * s.z
        yw = s.y * s.w
        
        zz = s.z * s.z
        zw = s.z * s.w

        # Wow, good math leads to efficiency.
        # Hmm...
        matrix[0].x  = 1 - 2 * ( yy + zz )
        matrix[1].x  =     2 * ( xy - zw )
        matrix[2].x  =     2 * ( xz + yw )
        
        matrix[0].y  =     2 * ( xy + zw )
        matrix[1].y  = 1 - 2 * ( xx + zz )
        matrix[2].y  =     2 * ( yz - xw )

        matrix[0].z  =     2 * ( xz - yw )
        matrix[1].z  =     2 * ( yz + xw )
        matrix[2].z  = 1 - 2 * ( xx + yy )

##         matrix[0].x  = 1 - 2 * ( yy + zz )
##         matrix[0].y  =     2 * ( xy - zw )
##         matrix[0].z  =     2 * ( xz + yw )
        
##         matrix[1].x  =     2 * ( xy + zw )
##         matrix[1].y  = 1 - 2 * ( xx + zz )
##         matrix[1].z  =     2 * ( yz - xw )

##         matrix[2].x  =     2 * ( xz - yw )
##         matrix[2].y  =     2 * ( yz + xw )
##         matrix[2].z  = 1 - 2 * ( xx + yy )
        

        
        return matrix

    def __repr__( s ):
        return "<Q %f, (%f, %f, %f)>" % (s.w, s.x, s.y, s.z)


# This algorithm does not work!  Find another!
def euler2Quaternion( x, y, z ):
    x = x * pi / 180.0
    y = y * pi / 180.0
    z = z * pi / 180.0
    Qx = Quaternion( cos( x / 2 ), sin( x / 2 ), 0, 0 )
    Qy = Quaternion( cos( y / 2 ), 0, sin( y / 2 ), 0 )
    Qz = Quaternion( cos( z / 2 ), 0, 0, sin( z / 2 ) )
    return Qx.mult( Qy ).mult( Qz )
