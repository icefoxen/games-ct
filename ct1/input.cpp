/* input.cpp
   Handles all the input stuff.
   We SHOULD be able to do it without SDL...

   We will need a keymap --an array of keys to actions.

   CCameraFPSSceneNode has some good stuff in it.

   ...hokay.  So the input reciever will only hang onto a keyState or
   commandState object.  It will modify this according to the input,
   essentially sending commands to the object.

   ...These objects can be things beyond just ships.  They can be, for
   instance, the runtime system to do things like save or quit.
   These require more/different commandStates, though.
   Hmmmm.  We CAN have multiple EventRecievers, using different ones
   at different times.  Flight mode vs menu mode, etc.
   Not sure we're gonna get that fancy though... but it's something
   to think about.  Really, I COULD just make all the commands modeless;
   keyboard shortcuts instead of menus, etc.


   It will also read in a config file (someday) that tells it what
   keys are bound to what commands.
   Someday we'll also have mouse support.


   Simon Heath
   17/2/2006
*/

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
#include "input.h"
#include "controlInterface.h"


KeyboardController::KeyboardController()
{
   loadKeyMap();
}

bool KeyboardController::OnEvent( SEvent event )
{
   // Um... slight disadvantage to doing it by char value...
   // Can't do things like escape, backspace, etc.
   // Damn Irrlicht.  Need to fix that.
   if( event.EventType == EET_KEY_INPUT_EVENT &&
       !event.KeyInput.PressedDown )
   {
      if( !control )
      {
	 cout << "input.cpp: Controller does not exist!" << endl;
	 dieHorribly();
      }

      char stupidCasts = (char) event.KeyInput.Char;

      // Stupid way of doing it (array map might be better),
      // but it works.
      // Um... or a case?
      if( stupidCasts == fwdThrustKey )
      {
	 control->activeCommands[COMMAND_FWD] = true;
      }
      if( stupidCasts == backThrustKey )
      {
	 control->activeCommands[COMMAND_BACK] = true;
      }
      if( stupidCasts == leftThrustKey )
      {
	 control->activeCommands[COMMAND_LEFT] = true;
      }
      if( stupidCasts == rightThrustKey )
      {
	 control->activeCommands[COMMAND_RIGHT] = true;
      }
      if( stupidCasts == upThrustKey )
      {
	 control->activeCommands[COMMAND_UP] = true;
      }
      if( stupidCasts == downThrustKey )
      {
	 control->activeCommands[COMMAND_DOWN] = true;
      }

      if( stupidCasts == fwdRollKey )
      {
	 control->activeCommands[COMMAND_ROLL_FWD] = true;
      }
      if( stupidCasts == backRollKey )
      {
	 control->activeCommands[COMMAND_ROLL_BACK] = true;
      }
      if( stupidCasts == leftRollKey )
      {
	 control->activeCommands[COMMAND_ROLL_LEFT] = true;
      }
      if( stupidCasts == rightRollKey )
      {
	 control->activeCommands[COMMAND_ROLL_RIGHT] = true;
      }
      if( stupidCasts == leftTwistKey )
      {
	 control->activeCommands[COMMAND_TWIST_LEFT] = true;
      }
      if( stupidCasts == rightTwistKey )
      {
	 control->activeCommands[COMMAND_TWIST_RIGHT] = true;
      }

      return true;
   }
   return false;
/*
   // ...gods only know quite how this reference-stuff works...
   if( thing != 0 && event.EventType == EET_KEY_INPUT_EVENT &&
       !event.KeyInput.PressedDown )
   {
      vector3df posv = thing->getAbsolutePosition();
      vector3df rotv = thing->getRotation();
      // Or we can just set the X, Y and Z directly instead of adding
      // another vector to it.  Nice!
/*      posv += vector3df( 50, 0, 0 ); */
/*
      switch( event.KeyInput.Char )
      {
	 case L'w':
	    posv.Z += 5;
	    break;
	 case L's':
	    posv.Z -= 5;
	    break;
	 case L'a':
	    posv.X -= 5;
	    break;
	 case L'd':
	    posv.X += 5;
	    break;
	 case L'q':
	    posv.Y += 5;
	    break;
	 case L'e':
	    posv.Y -= 5;
	    break;

	 case L'o':
	    rotv.Z += 5;
	    break;
	 case L'l':
	    rotv.Z -= 5;
	    break;
	 case L'k':
	    rotv.X += 5;
	    break;
	 case L';':
	    rotv.X -= 5;
	    break;
	 case L'i':
	    rotv.Y += 5;
	    break;
	 case L'p':
	    rotv.Y -= 5;
	    break;
      }

      thing->setRotation( rotv );
      thing->setPosition( posv );
      cout << "Vector is now " << posv.X << "," << posv.Y << ","
	   << posv.Z << endl;
      return true;
   }
   return false;
*/
}

// You MUSTMUSTMUST call this!
void KeyboardController::setControl( ControlInterface* t )
{
   control = t;
}

ControlInterface* KeyboardController::getControl()
{
   return control;
}

// Private


// Brute force works.
// Except when it mysteriously segfaults.
void KeyboardController::loadKeyMap()
{
   Config* c = new Config( "keymap.xml" );
   fwdThrustKey = c->getChar( "fwdThrust" );
   backThrustKey = c->getChar( "backThrust" );
   leftThrustKey = c->getChar( "leftThrust" );
   rightThrustKey = c->getChar( "rightThrust" );
   upThrustKey = c->getChar( "upThrust" );
   downThrustKey = c->getChar( "downThrust" );

   fwdRollKey = c->getChar( "fwdRoll" );
   backRollKey = c->getChar( "backRoll" );
   leftRollKey = c->getChar( "leftRoll" );
   rightRollKey = c->getChar( "rightRoll" );
   leftTwistKey = c->getChar( "leftTwist" );
   rightTwistKey = c->getChar( "rightTwist" );

   fireKey = c->getChar( "fire" );
   quitKey = c->getChar( "quit" );
   delete c;
}
