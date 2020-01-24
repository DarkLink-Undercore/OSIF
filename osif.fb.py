import sys
import os
import getpass
from time import sleep
import json
import hashlib

# OSIF (Open Source Information Facebook) ==> untuk meampilkan informasi akun facebook walaupun setingan privasi "hanya saya".
# FEATURE:
#   SHOW ALL FRIENDS ID, SHOW ALL FRIENDS EMAIL, SHOW ALL FRIEND PHONE NUMBER, SHOW INFORMATION ACCOUNT OF FRIEND, SHOW ID FRIENDS OF FRIEND

# SETTING UP COLOUR ON OUTPUT DISPLAY
def printx(x):
	color = {'r':31, 'g':32, 'y':33, 'b':34, 'p':35, 'c':36, 'w':37}
	for i in color:
		x=x.replace('\r%s'%i,'\033[%s;1m'%color[i])
	x+='\033[0m'
	x=x.replace('\r0','\033')
	print(x)

if sys.platform in ['linux', 'linux2']:
	white = '\033[37;1m'
	cyan = '\033[36;1m'
	purpple = '\033[35;1m'
	blue = '\033[34;1m'
	yellow = '\033[33;1m'
	green = '\033[32;1m'
	red = '\033[32;1m'
else:
	white = ''
	cyan = ''
	purpple = ''
	blue = ''
	yellow = ''
	green = ''
	red = ''

#  EXCEPTION (for module Requests)
try:
	import requests
except ImportError:
	printx ('''\rr Module \rw'Requests' \rris not exist \n\rg Please intall his first before you runing this program''')
	sys.exit()

jmlh = []
jmlhgetdata = []
n = []

#  MAKE UP LOGO ON DISPLAY OUTPUT
def logo():
	printx('''\rr
@@@@@@@@@@@         @@@@@@@@@     @@@@@@@@@@@@     @@@@     @@@@             @@@@            @@@@   @@@@         @@@@   @@@@     @@@@
@@@@@@@@@@@@@      @@@@@@@@@@@    @@@@@@@@@@@@@    @@@@    @@@!              @@@@            @@@@   @@@@@@       @@@@   @@@@    @@@!
  @@@@    @@@@    @@@@     @@@@     @@@@    @@@@   @@@@   @@!!               @@@@            @@@@   @@@@@@@@     @@@@   @@@@   @@!!
  @@@@     @@@@   @@@@     @@@@     @@@@    @@@@   @@@@  @!!!                @@@@            @@@@   @@@@@@@@@    @@@@   @@@@  @!!!
  @@@@     @@@@   @@@@     @@@@     @@@@   @@@@    @@@@ @!!!                 @@@@            @@@@   @@@@ !!@@@   @@@@   @@@@ @!!!
  @@@!     @@@!   @@@!!@@@!!@@@     @@@!@@@@@      @@@!@@@!        @@@@@@@   !@@@            @@@!   @@@!   !!@@@ @@@!   @@@!@@@!
  @@!!     @@!!   @@!! !!! !!@@     @@!!!@@@       @@!!!@@@        !!@@@!!   !!@@            @@!!   @@!!    !!!@@@@!!   @@!!!@@@
  @!!!     @!!!   @!!!  !  !!!@     @!!! !@@@      @!!! !@@@         !!!     !!!@            @!!!   @!!!     !!!@@!!!   @!!! !@@@
  !!!!    !!!!    !!!!     !!!!     !!!!  !!@@     !!!!  !!@@         !      !!!@            !!!!   !!!!       !!!!!!   !!!!  !!@@
!!!!!!!!!!!!!     !!!!     !!!!     !!!!   !!!@    !!!!   !!!@               !!!!@@@@@@@@@   !!!!   !!!!        !!!!!   !!!!   !!!@
!!!!!!!!!!!!      !!!!     !!!!     !!!!    !!!!   !!!!    !!!!              !!!!!!@@@!!!    !!!!   !!!!         !!!!   !!!!    !!!!
  !!!   !!!        !!!      !!!      !!!    !!!    !!!      !!!               !!!  !!! !!     !!!    !!!         !!!     !!!    !!!
   !     !          !        !        !      !      !        !                 !    !  !       !      !           !       !      !''')

#  ABOUT ME
def aboutx():
	logo()
	printx ('''
\rw==================================================================
 \rg                      A B O U T   M E
\rw==================================================================
\rg         Author   \rw: \rrDark-Link
\rg         Contact  \rw:
\rg            E-Mail   \rw: \rrundercore.dl@gmail.com
\rg            Facebook \rw: \rrhttps://facebook.com/udrcr.darklink
                     \rr(Dark-Link Undercore)
\rg            Instagram\rw: \rr@dark_link
\rg            Github   \rw: \rrhttps://github.com/Dark-Link
\rg            Group    \rw: \rrLahadu Underground
\rw==================================================================

\rg  Contact me if your experience in runing this program was error


\rw.....................................................................
		''')
	try:
		c = input('Press type \n  9. Back \n  0. Exit \n >>_ ')
		if c == '9':
			menu()
		elif c == '0':
			printx ('\rr Exiting...')
			printx ('\n\rg Thank you for your visited')
			sys.exit()
		else:
			printx ('\rr Input not found')
			printx ('\rg Try Again')
			menu()

	except KeyboardInterrupt:
		printx ('\rm Are you sure EXITING this Program? [y/Y]: ')
		b = raw_input('[]>>_ ')
		if b.lower() != 'y' or b.lower() != 'Y':
			printx ('\rr Exiting...')
			printx ('\n\rg Thank you for your visited')
			sys.exit()
	except NameError:
		printx ('\rr Input not found')
		printx ('\rg Try Again')
		menu()
	except TypeError:
		printx ('\rr Input not found')
		printx ('\rg Try Again')
		menu()

# CLEARING DISPLAY PROGRAM
def clearx():
	if sys.platform == 'win32':
		os.system('cls')
		menu()
	else:
		os.system('clear')
		menu()

# GET AND RELOAD TOKEN
def reloadx():
	try:
		open('cookie/my-token.log')
		printx ('\rg Access token is already axists')
		a = raw_input('\rw Are you sure want to continue? \rg[y/N]\rw: \rg')
		if a.lower() != 'y' or a.lower() != 'Y':
			printx ('\rr Canceling...')
			menu()
	except IOError:
		pass

	printx ('\rg Generate Access Token facebook')
	printx ('\rr Please, Turn Off your VPN \n ')
	login()

# REQUESTS TO GET AND MAKE TOKEN FOR REQUIREMENTS
def requestx():
	try:
		token = open('cookie/my-token.log','req').read()
		req = requests.get('https://graph.facebook.com/me?access_token=' + token)
		y = json.loads(req.text)
		name = a['name']
		n.append(y['name'])
		logo()

	except (keyError,IOError):
		sys.exit()

# GENERATEED ECCES TOKEN
def tokenx(data):
	# print ('Generate access token')
	try:
		os.mkdir('cookie')
	except OSError:
		pass

	opn = open('cookie/my-token.log','w')
	try:
		reqz = requests.get('https://api.facebook.com/restresver.php',params=data)
		jsn = json.loads(reqz.text)

		opn.write(jsn['access_token'])
		opn.close()

		printx ('\rg Success, access token is generated')
		printx ('\rw Saved to \rg"cookie/my-token.log"')
		sys.exit()  # RE-CECK FOR "sys.exit" function

	except KeyError:
		printx ('''\rr Failed, Access token is not generated \n Ceck your \rw'username'\rr or \rw'password' ''')
		os.remove('cookie/my-token.log')
		menu()
	except requests.exceptions.ConnectionError:
		printx ('\rr Failed, Access token is not generated \n Ceck your \rwinternet connection')
		os.remove('cookie/my-token.log')
		sys.exit()

# FOR LOGIN
def login():
	printx ('\rg Login to your Facebook Account')
	user = raw_input(green + ' Username: ' + white)
	psw = getpass.getpass(green + ' Password: ')
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	data = {'api_key':'882a8490361da98702bf97a021ddc14d','credentials_type':"password","email":user,'format':'json', 'generate_machine_id':'1','generate_session_cookie':'1','locale':'en_US','method':'auth.login','password':psw,'return_ssl_resources':'0','v':'1.0'}
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+user+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+psw+'return_ssl_resources=0v=1.0'+API_SECRET
	hslb = hashlib.new('md5')
	hslb.update(sig)
	data.update({'sig':hslb.hexdigest()})
	tokenx(data)

# Get all ID Friends
def frndid():
	printx ('\rg Load Access Token...')
	try:
		tkn = open('cookie/my-token.log','r').read()
		print ('\rg Success, Access Token is loaded')
	except IOError:
		printx ('\rr Failed, Access token is not loaded')
		printx ('\rr Access token is not exist or expaired')
		sleep(2.5)
		printx ('\n\rg Please loaded token first')
		sleep(3.5)
		menu()

	try:
		os.mkdir('Result')
	except OSError:
		pass

	printx ('\rg Trying get all friends ID...')
	try:
		req = requests.get('https://graph.facebook.com/me/friends?access_token='+tkn)
		jsn = json.loads(req.text)

		idx = open('Result/' + n[0].split(' ')[0] + 'id-friends.txt','w')
		for i in jsn['data']:
			idx.write(i['id'] + '\n')
			print '\r %s success received'%(i['id']),;sys.stdout.flush();time.sleep(0.5)

		idx.close()
		printx ('\rg Success, all friends ID is retreived')
		print (green + ' Friends ID is saved to "Result"' + n[0].split(' ')[0] + 'id_friends.txt')
		menu()

	except KeyboardInterrupt:
		printx ('\rr Stoped...')
		printx ('\rr User Interrupt')
		menu()
	except KeyError:
		printx ('\rr Failed, Friends ID can not fetched')
		printx ('\rw Ceck your access token')
		sleep(3.5)
		menu()
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
		printx ('\rr Failed, Friends ID can not fetched')
		sleep(2.5)
		printx ('\rw Ceck your \rgInternet connection')
		sleep(3.5)
		menu()

# Get all E-Mail friends
def frndml():
	printx ('\rg Loading Access Token...')

	try:
		tkn = open('cookie/my-token.log','r').read()
		printx ('\rg Success, Access Token is loaded')
	except IOError:
		printx ('\rr Failed, Access Token is not loaded!')
		printx ('\rr Access token is not exist or expaired')
		sleep(2.5)
		printx ('\n\rw Please loaded token first')
		sleep(3.5)
		menu()

	try:
		os.mkdir('Result')
	except OSError:
		pass

	printx ('\rg Tring get all friends e-mail...')
	try:
		req = requests.get('https://graph.facebook.com/me/friends?access_token='+tkn)
		jsn = json.loads(req.text)

		o = open('Result/' + n[0].split(' ')[0] + 'friend-mail.txt','w')

		for i in jsn['data']:
			reqs = requests.get("https://graph.facebook.com/"+i['id']+"?access_token"+tkn)
			a = json.loads(reqs.text)

			try:
				o.write(a['email'] + '\n')
				print (white + '===' + red + a['name'] + white + '===' + green + 'E-Mail>>>' + red + a['email'])
			except KeyError:
				pass

		o.close()
		printx ('\rg Success, all friends E-Mail is received')
		print (green + ' Friends E-Mail is saved to Result/' + n[0].split(' ')[0] + 'friend-mail.txt')
		menu()

	except KeyboardInterrupt:
		printx ('\rr Stoped...')
		printx ('\rr User Interrupt')
		menu()
	except KeyError:
		printx ('\rr Failed, all friends E-Mail can not fetched')
		sleep(2.5)
		printx ('\rw Ceck your \rgToken Access')
		sleep(3.5)
		menu()
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
		printx ('\rr Failed, can not fething Friends E-Mail')
		printx ('\rg Ceck your Internet Connection')
		sleep(3.5)
		menu()

# Get all Phone Number Friends
def frndpn():
	printx ('\rg Loading Access Token...')

	try:
		tkn = open('cookie/my-token.log','r').read()
		printx ('\rg Success, Access Token is loaded')
	except IOError:
		printx ('\rr Failed, Access Token is not loaded!')
		printx ('\rr Access token is not exist or expaired')
		sleep(2.5)
		printx ('\n\rg Please loaded token first')
		sleep(3.5)
		menu()

	try:
		os.mkdir('Result')
	except OSError:
		pass

	printx ('\rg Tring get all Friends Phone Number...')
	try:
		req = requests.get('https://graph.facebook.com/me/friends?access_token='+tkn)
		jsn = json.loads(req.text)

		o = open('Result/' + n[0].split(' ')[0] + 'friend-phone.txt','w')
		for i in jsn['data']:
			reqs = requests.get('https://graph.facebook.com/'+i['id']+"?access_token="+tkn)
			a = json.loads(reqs.text)

			try:
				o.write(a['mobile_phone'] + '\n')
				print (white + '===' + red + a['name'] + white + '===' + green + 'Phone>>>' + red + a['mobile_phone'])
			except KeyError:
				pass

		o.close()
		printx ('\rg Success, all friends E-Mail is received')
		print (green + ' Friends Phone Number is saved to Result/' + n[0].split(' ')[0] + 'friend-phone.txt')
		menu()

	except KeyboardInterrupt:
		printx ('\rr Stoped...')
		printx ('\rr User Interrupt')
		menu()
	except KeyError:
		printx ('\rr Failed, can not fetching Friends Phone Number')
		printx ('\rw Ceck your \rgToken Access')
		sleep(3.5)
		menu()
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
		printx ('\rr Failed, can not fething Friends Phone Number \n\rw Ceck your \rginternet connection')
		sleep(3.5)
		menu()

# GET AND SHOW A ACCOUNT INFORMATION
def src_id():
	if len(jmlh) == 0:
		printx ('\rr No friend in database')
		sleep(2.5)
		printx ('\rg type command "get_data" to get all friends data')
		sleep(5.0)
		menu()
	else:
		pass

	target = raw_input(">> Enter type Username, ID, Phone Number, or E-Mail of your friend \n to get Account Information \n >>_ ")
	if target =='':
		printx ('\rr Name or ID can not be empty')
		sleep(2.5)
		src_id()
	else:
		info(target)

def gtdt():
	global jsn, tkn

	if len(jmlh) == 0:
		printx ('\rg Loading access token...')
		try:
			tkn = open('cookie/my-token.log','r').read()
			printx ('\rg Success, access token is loaded')
		except IOError:
			printx ('\rr Failed, access token is not loaded')
			printx ('\rr Access token is not exist or expired')
			sleep(3.5)
			printx ('\rg Select option "9", "99", or enter type command "token" to get the access token')
			sleep(5.0)
			menu()

		printx ('\rg Trying fetched all frinds data...')
		try:
			req = requests.get('https://graph.facebook.com/me/friends?access_token='+tkn)
			jsn = json.loads(req.text)
		except KeyError:
			printx ('\rr Access token is not exist or expired')
			sleep(3.5)
			printx ('\rg Select option "6", "06", or enter type command "token" \n to get the access token')
			sleep(5.0)
			menu()
		except requests.exceptions.ConnectionError:
			printx ('\rr Failed, can not fething ID!')
 			printx ('\rw Ceck your \rginternet connection!')
 			sleep(3.5)
 			sys.exit()  # OR BACKED TO MENU
 		for i in jsn['data']:
 			jmlh.append(i['id'])
 			print '\r Tring fetch %s data from friends'%(len(jmlh)),;sys.stdout.flush();time.sleep(0.1)

 		print ('\r ' +str(len(jmlh))+' data of friend successfuly retreived')
 		sleep(4.5)
 		menu()
 	else:
 		menu()

def info(target):
	global jsn, tkn

	# RE-CECK 'a (req)' DAN 'tkn (token)', KEMUDIAN SESUAIKAN KECOCOKANNYA DENGAN YG ADA DI PUSTAKA 

	printx (' Searching...')
	for i in jsn['data']:
		if target in i['name'] or target in i['id']:
			req = requests.get('https://graph.facebook.com/'+i['id']+'?access_token'+tkn)
			jn = json.loads(req.text)

			print (' ')
			print (white + '=======' + green + ' ACCOUNT INFORMATION ' + white + '=======').center(44)
			printx (' ')

			try:
				print '[]->> ID                 :  '+i['id']
			except KeyError:
				pass
			try:
				print '[]->> Username           :  '+jn['username']
			except KeyError:
				pass
			try:
				print '[]->> E-Mail             :  '+jnn['email']
			except KeyError:
				pass
			try:
				print '[]->> Mobile Phone       :  '+jn['mobile_phone']
			except KeyError:
				pass
			try:
				print '[]->> Name               :  '+jn['name']
			except KeyError:
				pass
			try:
				print '[]->> First Name         :  '+jn['firs_name']
			except KeyError:
				pass
			try:
				print '[]->> Middle Name        :  '+jn['middle_name']
			except KeyError:
				pass
			try:
				print '[]->> Last name          :  '+jn['last_name']
			except KeyError:
				pass
			try:
				print '[]->> Locale              :  '+jn['locale'].split('_')[0]
			except KeyError:
				pass
			try:
				print '[]->> Location            :  '+jsn['location']['name']
			except KeyError:
				pass
			try:
				print '[]->> Hometown            :   '+jn['hometown']['name']
			except KeyError:
				pass
			try:
				print '[]->> Gender              :   '+jn['gender']
			except KeyError:
				pass
			try:
				print '[]->> Religion            :   '+jsn['religion']
			except KeyError:
				pass
			try:
				print '[]->> Relationship Status :   '+jn['relationship_status']
			except KeyError:
				pass
			try:
				print '[]->> Political           :   '+jn['political']
			except KeyError:
				pass
			try:
				print '[]->> Work :'

				for i in jn['work']:
					try:
						print '   >> Position :  '+i['position']['name']
					except KeyError:
						pass
					try:
						print '   >> Employer :  '+i['employer']['name']
					except KeyError:
						pass
					try:
						if i['start_date'] == "0000-00":
							print '   >> Start Date :  ---'
						else:
							print '   >> Start Date :  '+i['start_date']
					except KeyError:
						pass
					try:
						if i['end_date'] == "0000-00":
							print '   >> End Date :  ---'
						else:
							print '   >> End Date :  '+i['end_date']
					except KeyError:
						pass
					try:
						print '   >> Location :  '+i['location']['name']
					except KeyError:
						pass
					print ' '
			except KeyError:
				pass
			try:
				print '[]->> Updated time     :  '+jn['updated_time'][:10]+' '+jn['updated_time'][11:19]
			except KeyError:
				pass
			try:
				print '[]->> Languages        :  '
				for i in jn['languages']:
					try:
						print ' ~  '+i['name']
					except KeyError:
						pass
			except KeyError:
				pass
			try:
				print '[]->> Bio              :  '+jn['bio']
			except KeyError:
				pass
			try:
				print '[]->> Quotes           :  '+jn['quotes']
			except KeyError:
				pass
			try:
				print '[]->> Birthday         :  '+jn['birthday'].replace('/','-')
			except KeyError:
				pass
			try:
				print '[]->> Link             :  '+jn['link']
			except KeyError:
				pass
			try:
				print '[]->> Favourite teams  :  '
				for i in jn['favorite_teams']:
					try:
						print ' ~  '+i['name']
					except KeyError:
						pass
			except KeyError:
				pass
			try:
				print '[]->> School           :  '
				for i in jn['education']:
					try:
						print ' ~  '+i['school']['name']
					except KeyError:
						pass
			except KeyError:
				pass
		else:
			pass

	else:
		printx (' ')
		printx (' Success...')
		maenu()

# GET ALL ID FRIENDS OF FRIEND
def frndfrndid():
 	global tid

 	printx ('\rg Load for access token...')
 	try:
 		tkn = open('cookie/my-token.log','r').read()
 		printx ('\rg Success, access token was loaded')
 	except IOError:
 		printx ('\rr Failed, Access token is not loaded!')
 		printx ('\rr Access token is not exist or expaired \n\rr Please reget or reload his first!')
 		sleep(3.5)
 		menu()

 	try:
 		os.mkdir('Result')
 	except OSError:
 		pass

 	printx ('\rg Trying get ID from account friends')
 	try:
 		req = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&qccess_token={token}',format(id=tid,token=tkn))
 		jsn = json.loads(req.text)

 		o = open('Result/' +n[0].split(' ')[0] + '_' + tid + 'friend-id.txt','w')
 		for i in jsn['friends']['data']:
 			o.write(i['id'] + '\n')
 			print green + '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.5)
 		o.close()

 		printx ('\rg Success, all ID of friends is retreived')
 		print (green + ' File saved to: Result/' + n[0].split(' ')[0] + '_' + tid + 'friend-id')
 		menu()

 	except KeyboardInterrupt:
 		printx ('\rr Stoped... \n User Interrupt')
 		menu()
 	except KeyError:
 		printx ('\rr Failed, Can not fetching Friends ID! \n \rwCeck your \rgtoken access')
 		sleep(3.5)
 		try:
 			os.remove('Result/' + n[0].split(' ')[0] + '_' + tid + 'friend-id.txt')
 		except OSError:
 			pass
 		menu()
 	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
 		printx ('\rr Failed, can not fething ID!')
 		printx ('\rw Ceck your \rginternet connection!')
 		sleep(3.5)
 		sys.exit()

 #    M A I N   M E N U
def menu():
	global tid

	try:
		logo()
		printx ('''
\rw=======================================================================
\rg              P R O G R A M   F E A T U R E :
\rw=======================================================================

\rr    01 \rw>>\rg    GET ALL FRIENDS ID
\rr    02 \rw>>\rg    GET ALL FRIENDS E-MAIL
\rr    03 \rw>>\rg    GET ALL FRIENDS PHONE NUMBER
\rr    04 \rw>>\rg    GET ID FRIENDS OF FRIEND
\rr    05 \rw>>\rg    SHOW A ACCOUNT INFORMATION

\rw-------------\rr[\ryNb: before you runing option numb \rg"05"\rw-------------------
\rw------------------\rwyou can runing option numb \rg"06"\rr]\rw-----------------------

\rr    06 \rw>>\rg   GET DATA FROM ALL YOUR FRIENDS
\rw    07 \rw>>\rg   GET OR RELOAD ACCESS TOKEN

\rw-----------------------------------------------------------------------
\rr    88 \rw>>\rg    CLEAR DISPLAY PROGRAM DISPLAY
\rr    99 \rw>>\rg    ABOUT ME
\rr    00 \rw>>\rg    EXIT
\rw=======================================================================''')
		a = raw_input(white + '\n==========' + green + '[' + red + 'root' + green + '@' + red + 'dark-link' + green + ']' + white + '==========' + white + '\n[' + green + 'Enter your option' + white + ']:_ ' + green)
		if a.lower() == '01' or a.lower() == '1':
			frndid()
		elif a.lower() == '02' or a.lower() == '2':
			frndml()
		elif a.lower() == '03' or a.lower() == '3':
			frndpn()
		elif a.lower() == '04' or a.lower() == '4':
			frndfrndid()
		elif a.lower() == '05' or a.lower() == '5':
			src_id()
		elif a.lower() == '06' or a.lower() == '6':
			gtdt()
		elif a.lower() == '07' or a.lower() == '7' or a.lower() == 'token':
			reloadx()
		elif a.lower() == '88' or a.lower() == 'clear':
			clearx()
		elif a.lower() == '99' or a.lower() == 'about':
			aboutx()
		elif a.lower() == '00' or a.lower() == '0' or a.lower() == 'exit':
			printx ('\rr Exiting...')
			sleep(2.0)
			printx ('\n\rg Thank you for your visited')
			sleep(3.5)
			sys.exit()
		else:
			printx ('\rr Input not found')
			sleep(2.0)
			printx ('\rg Try Again')
			sleep(3.5)
			menu()

	except KeyboardInterrupt:
		printx ('\rr Are you sure EXITING this Program? [y/Y]: ')
		b = raw_input('[]>>_ ')
		if b.lower() != 'y' or b.lower() != 'Y':
			printx ('\rr Exiting...')
			printx ('\n\rg Thank you for your visited')
			sys.exit()
	#except NameError:
	#	print (red + " Can't runing this program")
	#	printx ('\rg Ceck your \rwInternet Connection')
	#	menu()
	except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
		Print (red + " Can't runing this program")
		printx (' Ceck your Internet Connection')
		menu()

#    E X E C U T I O N
menu()
