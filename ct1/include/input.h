/* input.h
   Input stuff.

   Simon Heath
   17/2/2006
*/


#ifndef _INPUT_H
#define _INPUT_H

#include <irrlicht.h>

#include "controlInterface.h"


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

// Whoo, this actually works.
// However, it still lags with key-repeat.
// Whyso?
// Maybe instead of clearing the ControlInterface with each frame,
// we clear it on key-up?  That could work...
//
// We don't seem to be able to hold multiple keys, either.  Hmm.
class KeyboardController : public IEventReceiver
{

  private:
   ControlInterface* control;

   char fwdThrustKey;
   char backThrustKey;
   char leftThrustKey;
   char rightThrustKey;
   char upThrustKey;
   char downThrustKey;
  
   char fwdRollKey;
   char backRollKey;
   char leftRollKey;
   char rightRollKey;
   char leftTwistKey;
   char rightTwistKey;

   char fireKey;
   char quitKey;

   virtual void loadKeyMap();

  public:
   KeyboardController();
   virtual bool OnEvent( SEvent e );
   virtual void setControl( ControlInterface* t );
   virtual ControlInterface* getControl();

};


#endif // _INPUT_H
