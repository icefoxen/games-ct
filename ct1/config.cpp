/* config.cpp
   Just in case you have illusions otherwise, this is utterly
   rediculous and a horrid abuse of XML.  But then, the Irrlicht
   XML parser is kinda crappy anyway, so.  We don't even try to
   bother with state or validation or anything, we just want a
   list of name=value pairs.
   And we GET it, too.  Oh yes.

   Simon Heath
   18/2/2006
*/
#include <iostream>
#include <map>
#include <irrlicht.h>

#include "ct.h"
#include "config.h"


using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;


extern ILogger* logger;


Config::Config( std::string cfgfile )
{
   filename = "data/config/" + cfgfile;
   std::cout << "Reading config file: " << filename << std::endl;
   // Segfault.  Putting it mildly, WTF???!!
//   logger->log( ("Reading config file: " + filename).c_str(), 
//		ELL_INFORMATION );
   readFile();
}

Config::~Config()
{
}

int Config::getInt( std::string name )
{
   // XXX: Fix this --shouldn't use atoi()
   return atoi( data[name].c_str() );
}

float Config::getFloat( std::string name )
{
   // XXX: This too
   return atof( data[name].c_str() );
}

char Config::getChar( std::string name )
{
   char c = data[name][0];
   if( c )
      return c;
   else
      return ' ';
}

std::string Config::getString( std::string name )
{
   return data[name];
}

void Config::reRead()
{
   data.clear();
   readFile();
}

void Config::print()
{
   cout << data.size() << endl;
}

// Private

void Config::readFile()
{
   IrrXMLReader* xml = createIrrXMLReader( filename.c_str() );
   if( !xml )
   {
      logger->log( L"Error: Could not open config file for reading!", 
		   ELL_ERROR );
      dieHorribly();
   }

   //std::cout << "Foo!" << std::endl;
   while( xml->read() )
   {
      switch( xml->getNodeType() )
      {
	 case EXN_ELEMENT:
	    //std::cout << "Bar!" << std::endl;
	    //std::cout << xml->getNodeName() << " " << xml->getAttributeValue( "data" ) << std::endl;
	    const char* nodename = xml->getNodeName();
	    const char* nodedata = xml->getAttributeValue( "data" );
	    if( nodename && nodedata ) 
	    {
	       data[nodename] = nodedata;
	    }
	    else
	    {
	       logger->log( L"Malformed config file",
			    ELL_ERROR );
	       dieHorribly();
	    }
	    break;
      }
   }
   delete xml;
}
