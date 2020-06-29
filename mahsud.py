@@ -49,46 +49,23 @@ def jalan(z):
##### LOGO #####
logo = """ -----------------------------•◈•
(  __)\\ ____--------------_------------•◈•
|__(~)    •||•THE - AAHIL -OFFICAL------•◈•
|__\~~) •||•RANA - RAJPUT---------------•◈•
|__(~)    •||•THE - Nisar -OFFICAL------•◈•
|__\~~) •||•Nisar - Mahsud---------------•◈•
|__(-----\  •◈•------BLACK-TIGER--------•◈•
|__~~~\ •◈•-----█-------⑦-------█------•◈•
|__~~~\ •◈•-----█-------⑧-------█------•◈•
|__~~~\ •◈•-----█-------⑥-------█------•◈•
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mRana Aahil
\033[1;96mInstagram \033[1;93m: \033[1;FlowRana
\033[1;96mFacebook  \033[1;93m: \033[1; Aahilrna4072
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://github.com/Therana/zero
\033[1;91m======================================="""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m ============================================================="
print  """\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mRana Aahil
\033[1;96mInstagram \033[1;93m: \033[1;92mFlowRana
\033[1;96mFacebook  \033[1;93m: \033[1;92m Aahilrana4072
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://Github.com/Therana/zero
\033[1;91m======================================="""
print " \x1b[1;93m============================================================="
CorrectUsername = "rana"
CorrectPassword = "rana"
CorrectUsername = "nisar"
CorrectPassword = "nisar"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
