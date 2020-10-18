#include "ext_types.h"
static DataTypeInfo rtDataTypeInfoTable [ ] = { { "real_T" , 0 , 8 } , {
"real32_T" , 1 , 4 } , { "int8_T" , 2 , 1 } , { "uint8_T" , 3 , 1 } , {
"int16_T" , 4 , 2 } , { "uint16_T" , 5 , 2 } , { "int32_T" , 6 , 4 } , {
"uint32_T" , 7 , 4 } , { "boolean_T" , 8 , 1 } , { "fcn_call_T" , 9 , 0 } , {
"int_T" , 10 , 4 } , { "pointer_T" , 11 , 8 } , { "action_T" , 12 , 8 } , {
"timer_uint32_pair_T" , 13 , 8 } , { "ChamberPaced" , 14 , 4 } , {
"ChamberSensed" , 15 , 4 } , { "Activity" , 16 , 4 } , { "uint32_T" , 17 , 4
} , { "uint64_T" , 18 , 8 } , { "int64_T" , 19 , 8 } , { "uint64_T" , 20 , 8
} } ; static uint_T rtDataTypeSizes [ ] = { sizeof ( real_T ) , sizeof (
real32_T ) , sizeof ( int8_T ) , sizeof ( uint8_T ) , sizeof ( int16_T ) ,
sizeof ( uint16_T ) , sizeof ( int32_T ) , sizeof ( uint32_T ) , sizeof (
boolean_T ) , sizeof ( fcn_call_T ) , sizeof ( int_T ) , sizeof ( pointer_T )
, sizeof ( action_T ) , 2 * sizeof ( uint32_T ) , sizeof ( ChamberPaced ) ,
sizeof ( ChamberSensed ) , sizeof ( Activity ) , sizeof ( uint32_T ) , sizeof
( uint64_T ) , sizeof ( int64_T ) , sizeof ( uint64_T ) } ; static const
char_T * rtDataTypeNames [ ] = { "real_T" , "real32_T" , "int8_T" , "uint8_T"
, "int16_T" , "uint16_T" , "int32_T" , "uint32_T" , "boolean_T" ,
"fcn_call_T" , "int_T" , "pointer_T" , "action_T" , "timer_uint32_pair_T" ,
"ChamberPaced" , "ChamberSensed" , "Activity" , "uint32_T" , "uint64_T" ,
"int64_T" , "uint64_T" } ; static DataTypeTransition rtBTransitions [ ] = { {
( char_T * ) ( & rtB . o0hmegtn4n ) , 18 , 0 , 2 } , { ( char_T * ) ( & rtB .
o0nlqgyufw ) , 7 , 0 , 5 } , { ( char_T * ) ( & rtB . h3ny4b2egu ) , 15 , 0 ,
1 } , { ( char_T * ) ( & rtB . opb340v0ul ) , 14 , 0 , 1 } , { ( char_T * ) (
& rtB . bfzr1arjyc ) , 16 , 0 , 1 } , { ( char_T * ) ( & rtB . fe5eov4z2i ) ,
8 , 0 , 1 } , { ( char_T * ) ( & rtDW . mlel4p0jzz . LoggedData ) , 11 , 0 ,
1 } , { ( char_T * ) ( & rtDW . c5bkqgcrxz ) , 6 , 0 , 1 } , { ( char_T * ) (
& rtDW . gbjg1dvsj1 ) , 7 , 0 , 4 } , { ( char_T * ) ( & rtDW . chlmxpvaee )
, 3 , 0 , 2 } } ; static DataTypeTransitionTable rtBTransTable = { 10U ,
rtBTransitions } ; static DataTypeTransition rtPTransitions [ ] = { { (
char_T * ) ( & rtP . Constant2_Value ) , 16 , 0 , 1 } , { ( char_T * ) ( &
rtP . Constant_Value ) , 14 , 0 , 1 } , { ( char_T * ) ( & rtP .
Constant1_Value ) , 15 , 0 , 1 } , { ( char_T * ) ( & rtP . Gain_Gain ) , 17
, 0 , 7 } } ; static DataTypeTransitionTable rtPTransTable = { 4U ,
rtPTransitions } ;