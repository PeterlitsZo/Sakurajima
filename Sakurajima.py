# 通过密码的哈希算法产生的数列进行运算从而达到加密的效果
from lib.SakurajimaLIB import *
import hashlib

print ('''    ------------------------------------------------------------
    Hello, this Programma is used to Encrypt the File(Retain the
    Original File), which only need the Address and Password. 
    ------------------------------------------------------------''')

theAddress = input("\n    Please Enter the Address of the File:")
thePassword = input("    Please Enter the Password:")
theOriginalFile = open(theAddress,'rb')
theFile = open(theAddress + ".enced",'wb+')

theMD5 = hashlib.md5(thePassword.encode())
theMD5_bytes = theMD5.digest()
theMD5_bytes = Mix_Two_Bytes(theMD5_bytes,theMD5_of_Peterlits)

if The_Number_Of_Bit_Of_1(theMD5_bytes.hex()) <= 32:
    theMD5_bytes = Negate_of_Bytes (theMD5_bytes)

print ("\n    The MD5 of the Password is " + theMD5_bytes.hex() +".")
print ("    Now It is Going to Work:\n")

file_len = os.path.getsize(theAddress)
app = QApplication([''])
bar_thread = threading.Thread(target = QtBar,args = (file_flag, file_len, app))
bar_thread.setDaemon(True)
bar_thread.start()

while True:
    file_flag[0]+=16
    OneAdd = Mix_Two_Bytes(theOriginalFile.read(16),theMD5_bytes)
    if OneAdd==b'':
        break
    theFile.write(OneAdd)

theOriginalFile.close()
theFile.close()
print ("    Overed. The Encrypted Files is next to the Original File.")
