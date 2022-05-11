import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))

def banner(): # Program Banner
    print('\n   ╔══════════════════════╗\n   ║    D4RKOBF           ║\n   ║ Author : D4RKH0R1Z0N ║\n   ╚══════════════════════╝\n')

def menu(): # Program Menu
    print("[1] Encode with Marshal,Zlib,B16\n[2] Encode with Marshal,Zlib,B32\n[3] Encode with Marshal,Zlib,B64\n")

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [*] Encoded File Size : %s\n" % self.datas(dts))
# FileSize('rec.py')

def Encode(option,data,output):
    loop = int(eval(_input % " [*] Encode Count : "))
    if option == 1:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 2:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 3:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(heading + data)
        f.close()

# Main Menu
def MainMenu():
    try:
        os.system('cls') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " [*] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n Thanks For Using this Tool")
            os.system('cls') # os.system('cls')
            banner()
        else:
            sys.exit('\n Invalid Option !')
        try:
            file = eval(_input % " [*] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        
        output = file.lower().replace('.py', '') + '_D4RKOBF.py'
        Encode(option,data,output)
        print("\n [*] Successfully Encrypted %s" % file)
        print(" [*] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
