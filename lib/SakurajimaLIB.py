#hash:used to get MD5 list
#os:used to get the size of file (to show the bar)
#threading:used to show the bar
import os
import threading
import math

theMD5_of_Peterlits = \
    b'\xa2\x44\xd2\xc5\x45\x70\x7d\x00\x84\x13\x82\x2a\xa3\x74\xcf\xab'
file_flag = [0]

def The_Number_Of_Bit_Of_1 (StringOf16):
    theDict = {"0":0,"1":1,"2":1,"3":2,"4":1,"5":2,"6":2,"7":3,\
               "8":1,"9":2,"a":2,"b":3,"c":2,"d":3,"e":3,"f":4}
    theNumber = 0
    for i in StringOf16:
        theNumber += theDict[i]
    return theNumber

def MixTwoByte (Byte1, Byte2):
    return Byte1^Byte2

def Mix_Two_Bytes (Bytes1, Bytes2):
    MixedBytes = []
    for i in range(Bytes1.__len__()):
        MixedBytes.append (MixTwoByte (Bytes1[i], Bytes2[i]))
    return bytes(MixedBytes)

def Negate_of_Bytes (Bytes):
    AimBytes = []
    for Byte in Bytes:
        AimBytes.append (~Byte)
    return bytes(AimBytes)

def Down_To_Next_Int(num):
    return math.ceil(num)-1;

def Bit_Of_Num(num, bit):
    if type(num)==type(float()):
        num=Down_To_Next_Int(num)
    return num//(10**(bit-1))-num//(10**bit)*10

def Write_Bar (long, fillchar='-', times = 1, endchar='\n', bar_long= -1):
    _sum = times*long
    print (fillchar*(_sum), sep='',end='')
    if bar_long >= long:
        print (' '*(bar_long*times-_sum), sep='',end='')
    print (endchar,sep='',end='')

def Bars (flag, _len):
    while True:
        rate = flag[0] / _len * 100
        print("%-12.6f%%|"%rate ,sep='|',end='')
        Write_Bar(Bit_Of_Num(rate,2), '-', 2, '|    |',10)
        Write_Bar(Bit_Of_Num(rate,1), '-', 2, '|\n',10)

