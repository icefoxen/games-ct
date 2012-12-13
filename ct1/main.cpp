/* main.cpp
 * Main file of Charble Twinsty.
 * Setup, shutdown, that good stuff.
 *
 * Simon Heath
 * 15/2/2006
 */

#include <irrlicht.h>

using namespace std;

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

#include <iostream>


#include "ct.h"
#include "input.h"
#include "config.h"
#include "spaceobj.h"


IrrlichtDevice* irrdev;
KeyboardController* event;
ILogger* logger;
bool keepOnTruckin = true;

void mainloop()
{

   IVideoDriver *driver = irrdev->getVideoDriver();
   ISceneManager *smgr = irrdev->getSceneManager();
   IGUIEnvironment *guienv = irrdev->getGUIEnvironment();

   // Add text
   //guienv->addStaticText( L"Hello world!  Charble Twinsty.",
   //	 rect<int>( 50, 50, 300, 70 ), true );

   // Add camera at ... [facing ...] 
   ICameraSceneNode* camera = smgr->addCameraSceneNode();


   SpaceObj* s = new SpaceObj( "testobj.xml", irrdev );
   s->setNewControlInterface( event->getControl() );
   //s->moveTo( vector3df( 0, 10, 0 ) );
   //s->setVectorTo( vector3df( 0, 1, 0 ) );

   SpaceObj* o = new SpaceObj( "testobj.xml", irrdev );
   o->moveTo( vector3df( 0, 10, 0 ) );


   camera->setTarget( vector3df( 0, 10, 0 ) );
   /* Run the mainloop. */
   while( /* keepOnTruckin && */ irrdev->run() )
   {
      // Set the camera to face the model
      //
      s->doCommands();
      s->doCalc( 1000 );
      o->doCalc( 1000 );

      // 1st SColor arg is alpha...
      driver->beginScene( true, true, SColor( 0, 0, 0, 0 ) );
      smgr->drawAll();
      guienv->drawAll();
      driver->endScene();
   }

   delete s;

}

void dieNonHorribly()
{
   cout << "Died horribly!" << endl;
   irrdev->drop();
   exit( 0 );
}

void dieHorribly()
{
   cout << "Died horribly!" << endl;
   dieNonHorribly();
}



int main()
{
   
   // Init
   event = new KeyboardController();
   ControlInterface* objint = new ControlInterface();
   event->setControl( objint );
   

   // EDT_SOFTWARE works too .
   // driver, screensize, bitdepth, fullscreen?, stencilbuffer?, vsync?,
   // eventreciever
  E_DRIVER_TYPE ogl = EDT_OPENGL;
  E_DRIVER_TYPE soft = EDT_SOFTWARE;
  irrdev = createDevice( ogl, dimension2d<s32>( 800, 600 ), 16,
			 false, true, false, event );

  logger = irrdev->getLogger();

  irrdev->setWindowCaption( L"Charble Twinsty" );


  Config* c = new Config( "testfile.xml" );
  delete c;

  mainloop();

  delete objint;


  // Clean up
//  irrdev->drop();
//  delete objint;
//  delete event;

  return 0;

}
