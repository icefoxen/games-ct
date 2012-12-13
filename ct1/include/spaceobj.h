/* spaceobj.h
   This is the basic space object.
   It can move around, have inertia and mass, collide, be
   drawn, and eat things.

   ...I'm not 100% sure about the eating things part...

   ...and I just realized that this is an MVC design.  This the Model,
   the SceneNode is the View, and the the ControlInterface is the
   controller.
   Amazing how that stuff happens by accident...

   ....hrm.  How does this integrate with the scene manager, precisely?
   Hangs onto a pointer to the smgr, most probably...
   Or more likely takes a pointer and adds itself to it, but doesn't
   keep a hold of it.

   Simon Heath
   17/2/2006
*/

#ifndef _SPACEOBJ_H
#define _SPACEOBJ_H

#include <iostream> 
#include <irrlicht.h>

using namespace std;
using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

#include "ct.h"
#include "controlInterface.h"
#include "config.h"


class SpaceObj
{
  private:
   float mass;
   vector3df movement;
   IAnimatedMeshSceneNode* node;
   ControlInterface* control;
   ISceneManager* smgr;
   u32 lastUpdate;
   bool alive;
   
  public:
   SpaceObj( std::string configfile,
	     IrrlichtDevice* dev );
   // Checks the control interface, does all it says, clears it.
   // ...time.  Hmm.  Maybe just globals.
   virtual void doCommands();
   virtual void doCalc( int time );
   virtual void die();
   virtual void doImpact( SpaceObj impactor );

   virtual void moveTo( vector3df loc );
   virtual void setVectorTo( vector3df loc );
   virtual void setFacingTo( vector3df loc );
   //virtual void onPostRender( u32 time );
   virtual bool isAlive();
   virtual void setAlive( bool t );
   virtual vector3df getLocation();
   virtual vector3df getOrientation();
   virtual vector3df getHeading();


   virtual ControlInterface* getControlInterface();
   virtual void setControlInterface( ControlInterface* c );
   virtual void setNewControlInterface( ControlInterface* c );

   virtual bool isColliding( SpaceObj* other );

   // Yesno?
   virtual void setNode( IAnimatedMeshSceneNode* n );
   virtual IAnimatedMeshSceneNode* getNode();
};



#endif // _SPACEOBJ_H
