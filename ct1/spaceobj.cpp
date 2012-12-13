
#include <iostream>
#include <irrlicht.h>
#include "spaceobj.h"

using namespace std;
using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

extern ILogger* logger;



SpaceObj::SpaceObj( std::string configfile, IrrlichtDevice* dev )
{
   std::string meshname = "data/meshes/";
   std::string texturename = "data/textures/";

   // Read in config file
   Config* c = new Config( configfile );

   mass = c->getFloat( "mass" );
   meshname += c->getString( "mesh" );
   texturename += c->getString( "texture" );

   delete c;

   // Get stuff
   smgr = dev->getSceneManager();
   IVideoDriver* driver = dev->getVideoDriver();

   // Add scene node
   // Also, this is kinda odd.  smgr->getMesh() returns an IAnimatedMesh.
   // So we need to have an animated mesh.
   // For some reason, they're not related to each other.
   // ...I hate C++ strings and all who create them so, so hard.
   IAnimatedMesh* mesh = smgr->getMesh( meshname.c_str() );
   node = smgr->addAnimatedMeshSceneNode( mesh );

   if( !node )
   {
      // Log error and die
      logger->log( L"Could not load mesh!", 0 );
      dieHorribly();
   }
   // Set texture
   node->setMaterialTexture( 0, driver->getTexture( texturename.c_str() ) );

   // Make collision stuff
   // It's stupid.  Really stupid.
   //ITriangleSelector* s = 0;
   //s = smgr->createTriangleSelector( mesh->getMesh( 0 ), node );
   //node->setTriangleSelector( s );
   //s->drop();
   
   // Link to control interface
   control = new ControlInterface();

   alive = true;

}

// Of ISceneNode class,
// OnPreRender(), OnPostRender( time ), and remove() may be useful.
void SpaceObj::doCommands()
{
   for( int x = 0; x < COMMAND_COUNT; x++ )
   {
      if( control->activeCommands[x] )
      {
	 cout << "Active command: " << x << endl;
      }
   }
   control->clear();
}

void SpaceObj::doCalc( int time )
{
   vector3df f = node->getAbsolutePosition();
   f += movement * (time / 1000.0);
   node->setPosition( f );
}

void SpaceObj::die() 
{
   cout << "Boom!" << endl;
   node->remove();
   alive = false;
}

void SpaceObj::doImpact( SpaceObj impactor ) 
{
   die();
}

void SpaceObj::moveTo( vector3df loc ) 
{
   node->setPosition( loc );
}

void SpaceObj::setVectorTo( vector3df loc ) 
{
   movement = loc;
}

void SpaceObj::setFacingTo( vector3df loc ) 
{
   node->setRotation( loc );
}

vector3df SpaceObj::getLocation() 
{
   return node->getAbsolutePosition();
}

vector3df SpaceObj::getOrientation() 
{
   return node->getRotation();
}

vector3df SpaceObj::getHeading() 
{
   return movement;
}


ControlInterface* SpaceObj::getControlInterface() 
{
   return control;
}

bool SpaceObj::isAlive()
{
   return alive;
}

void SpaceObj::setAlive( bool a )
{
   alive = false;
}

bool SpaceObj::isColliding( SpaceObj* other )
{
   aabbox3d<f32> boundingbox = node->getTransformedBoundingBox();
   aabbox3d<f32> otherbb = other->getNode()->getTransformedBoundingBox();
   return boundingbox.intersectsWithBox( otherbb );
}

// XXX: Be careful not to leak memory here!
void SpaceObj::setControlInterface( ControlInterface* c ) 
{
   control = c;
}

void SpaceObj::setNewControlInterface( ControlInterface* c )
{
   delete control;
   control = c;
}

// Yesno?
void SpaceObj::setNode( IAnimatedMeshSceneNode* n ) 
{
   node = n;
}

IAnimatedMeshSceneNode* SpaceObj::getNode() 
{
   return node;
}

