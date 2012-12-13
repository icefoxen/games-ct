/* controlInterface.cpp

   
   Simon Heath
   18/2/2006
*/


#include "controlInterface.h"

void ControlInterface::clear()
{
   for( int x = 0; x < COMMAND_COUNT; x++ )
   {
      activeCommands[x] = false;
   }
}
