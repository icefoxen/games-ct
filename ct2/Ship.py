
# XXX...  I need a compass, a heading vector-line, and some kinda
# external reference point (stars).  A "reset location, heading and vector"
# button would also be nice.
# A gui framework in general would be good, too.  Billboards and such...


from OpenGL.GL import *
from OpenGL.GLU import *

from TextureLoader import *
from Quaternion import *
from Vector3D import *
from SpaceObj import *

class Ship( SpaceObj ):

    irEmissions = 0
    radarEmissions = 0
    lidarEmissions = 0

    radarOn = False
    lidarOn = False

    fuel = 0.0
    fuelBurnRate = 0.0
    
    maxAccel = 0.0
    currentAccel = 1.0
    turnRate = 0.0

    maxEnergy = 0.0
    energyRegen = 0.0
    currentEnergy = 0.0

    def __init__( s ):
        SpaceObj.__init__( s )

    def calc( s, t ):
        SpaceObj.calc( s, t )
        # Acceleration, energy, emissions, visibility...
        
    def canSee( s, obj ):
        return 0

    def canSeeRadar( s, obj ):
        return 0
    
    def canSeeLidar( s, obj ):
        return 0

    def canSeeIR( s, obj ):
        return 0

    def thrust( s, t ):
        facingMatrix = s.facing.toMatrix()
        thrustVector = facingMatrix[2] # Z heading
        # thrustVector SHOULD be normalized already, but...
        thrustVector.normalize()
        
        thrustVector.mulNumber( (s.currentAccel / 1000.0) * t )
        s.accelerate( thrustVector )

    

