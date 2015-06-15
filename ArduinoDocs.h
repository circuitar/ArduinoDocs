/** @file ArduinoDocs.h
 * ArduinoDocs sample library.
 *
 * This is a sample library to show how to use ArduinoDocs.
 *
 * Copyright (c) 2015 Circuitar
 * This software is released under the MIT license. See the attached LICENSE file for details.
*/
#ifndef ARDUINODOCS_h
#define ARDUINODOCS_h

#include <Arduino.h>

/**
 * This is a brief description of the ArduinoDocs class.
 *
 * This is the detailed description of the ArduinoDocs class.
 */
class ArduinoDocs
{
  public:
    /**
     * Constructor.
     *
     * Create an ArduinoDocs (bogus) object.
     */
    ArduinoDocs();

    /**
     * Brief documentation for method 1.
     *
     * Detailed documentation for method 1.
     */
    void method1();
    
    /**
     * Brief documentation for method 2.
     *
     * Detailed documentation for method 2.
     *
     * @param p1  method 2's first parameter.
     * @param p2  method 2's second parameter.
     * @return   return value for method 2.
     */
    int method2(int p1, int p2);
    
  private:
    int member1;
    float member2;
    
    int method3(int p1);
};

#endif
