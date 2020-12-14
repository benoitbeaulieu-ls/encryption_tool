import gnupg
import os
import platform
import subprocess


os_type = (platform.system())

def key_creation():
    key_store=input('Where would you like to store your key?')

    gpg=gnupg.GPG(gnupghome='~')
    gpg.encoding = 'utf-8'
    key_info = gpg.gen_key_input()





if os_type == 'Linux':
    print('Detected Linux Operating System')
    print('#########################################')
    key_creation()



    


