/* config.h
   Configuration file framework.
   We do some evil things to the (somewhat crappy) Irrlicht XML
   interface here.

   Simon Heath
   18/2/2006
*/


#ifndef _CONFIG_H
#define _CONFIG_H

/*
enum ConfigType {
   CFG_INT;
   CFG_FLOAT;
   CFG_STRING;

   CFG_COUNT;
};

struct BloodyTaggedUnion {
      ConfigType tag;
      union{ int i; float f; string s } itm;
};
*/

/* ...how do we fit all the different config data in here?
   atoi()?  Ugly...  Might be simplest, though.
   Different maps?  Doable...  Hacky as hell, though.
*/

#include <iostream>
#include <map>
#include <irrlicht.h>

using namespace std;


class Config
{
  public:
   Config( std::string cfgfile );
   ~Config();
   int getInt( std::string name );
   float getFloat( std::string name );
   char getChar( std::string name );
   std::string getString( std::string name );
   void reRead();
   void print();

  private:
   std::string filename;
   map<std::string,std::string> data;
   void readFile();
};


#endif // _CONFIG_H
