# 通过密码的哈希算法产生的数列进行运算从而达到加密的效果
import hashlib

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

theMD5_of_Peterlits = \
    b'\xa2\x44\xd2\xc5\x45\x70\x7d\x00\x84\x13\x82\x2a\xa3\x74\xcf\xab'
theFiles_flag = 0

print ('''    ------------------------------------------------------------
    Hello, this Programma is used to Encrypt the File(Retain the
    Original File), which only need the Address and Password. 
    ------------------------------------------------------------''')

theAddress = input("\nPlease Enter the Address of the File:")
thePassword = input("Please Enter the Password:")
theOriginalFile = open(theAddress,'rb')
theFile = open(theAddress + ".enced",'wb+')

theMD5 = hashlib.md5(thePassword.encode())
theMD5_bytes = theMD5.digest()
theMD5_bytes = Mix_Two_Bytes(theMD5_bytes,theMD5_of_Peterlits)

if The_Number_Of_Bit_Of_1(theMD5_bytes.hex()) <= 32:
    theMD5_bytes = Negate_of_Bytes (theMD5_bytes)

print ("\nThe MD5 of the Password is " + theMD5_bytes.hex() +".")
print ("Now It is Going to Work:\n")

while True:
    OneAdd = Mix_Two_Bytes(theOriginalFile.read(16),theMD5_bytes)
    if OneAdd==b'':
        break
    theFile.write(OneAdd)

theOriginalFile.close()
theFile.close()
print ("Overed. The Encrypted Files is next to the Original File.")
