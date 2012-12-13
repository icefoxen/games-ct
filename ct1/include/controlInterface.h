/* commandState.h
   This is basically an array of potential commands "move", "fire", etc
   It will get hung onto both by each active object (ship), and the object that
   commands it --keyboard, AI, and so on.
   
   It is essentially the basic interface to a ship.

   Simon Heath
   17/2/2006
*/


#ifndef _COMMANDSTATE_H
#define _COMMANDSTATE_H

#include <irrlicht.h>

using namespace std;
using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

#include "config.h"




enum COMMAND {
   COMMAND_FWD,
   COMMAND_BACK,
   COMMAND_LEFT,
   COMMAND_RIGHT,
   COMMAND_UP,
   COMMAND_DOWN,

   COMMAND_ROLL_FWD,
   COMMAND_ROLL_BACK,
   COMMAND_ROLL_LEFT,
   COMMAND_ROLL_RIGHT,
   COMMAND_TWIST_LEFT,
   COMMAND_TWIST_RIGHT,

   COMMAND_FIRE,
   COMMAND_QUIT,

   COMMAND_COUNT,
};


class ControlInterface
{
  public:
   bool activeCommands[COMMAND_COUNT];
   void clear();
};



#endif // _COMMANDSTATE_H
