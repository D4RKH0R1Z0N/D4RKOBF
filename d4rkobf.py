import os
from sys import version_info, platform, exit
import zlib
import time
import base64
import marshal
import py_compile

if platform == "win32":
    clear = "cls"
else:
    clear = "clear"

if version_info[0]==2:
    _input = "raw_input('%s')"
elif version_info[0]==3:
    _input = "input('%s')"
else:
    exit("\n [!] Python Version Error! Please Try Upgrading!")

zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))

def banner():
    print('\n ╔═════════════════════════════════╗\n ║             D4RKOBF             ║\n ║                                 ║\n ║  Made by D4RKH0R1Z0N            ║\n ║  https://github.com/D4RKH0R1Z0N ║\n ╚═════════════════════════════════╝\n')

def menu():
    print(" [1] Encode Zlib,Base16\n [2] Encode Zlib,Base32\n [3] Encode Zlib,Base64\n [4] Encode Marshal,Zlib,B16\n [5] Encode Marshal,Zlib,B32\n [6] Encode Marshal,Zlib,B64\n [0] Exit\n")

class FileSize:
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [*] Encoded File Size : %s\n" % self.datas(dts))

def program():
    os.system(clear)
    def Encode(option,data,output):
        loop = int(eval(_input % " [*] Encode Count : "))
        if option == 1:
            xx = "b16(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
        elif option == 2:
            xx = "b32(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
        elif option == 3:
            xx = "b64(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
        elif option == 4:
            xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
        elif option == 5:
            xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
        elif option == 6:
            xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
        else:
            print("\n [!] Invalid Option!")
            time.sleep(0.8)
            program()
        
        for x in range(loop):
            try:
                data = "exec((_)(%s))" % repr(eval(xx))
            except TypeError as s:
                exit(" [!] TypeError : " + str(s))
        with open(output, 'w') as f:
            f.write(heading + data)
            f.close()

    def MainMenu():
        try:
            os.system(clear)
            banner()
            menu()
            try:
                option = int(eval(_input % " [*] Option : "))
            except ValueError:
                print("\n [!] Invalid Option !")
                time.sleep(0.8)
                program()
            if option > -1 and option <= 6:
                if option == 0:
                    exit("\n [!] Exitting...")
                os.system(clear)
                banner()
            else:
                print('\n [!] Invalid Option!')
                time.sleep(0.8)
                program()
            try:
                file = eval(_input % " [*] File Name : ")
                data = open(file).read()
            except IOError:
                print("\n [!] File not Found!")
                time.sleep(0.8)
                program()
            
            output = file.lower().replace('.py', '') + '_D4RKOBF.py'
            Encode(option, data, output)
            print("\n [*] Successfully Obfuscated %s" % file)
            print(" [*] File Saved As %s" % output)
            FileSize(output)
        except KeyboardInterrupt:
            time.sleep(0.8)
            exit()

    if __name__ == "__main__":
        MainMenu()

program()
