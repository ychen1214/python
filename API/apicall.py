#https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests 

#response = requests.get("http://api.open-notify.org/astros.json")
query = {'lat':'45','lon':'180'}
response = requests.get("http://api.open-notify.org/iss-pass.json",params=query)
print(response)




#check for errors
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests

#raise errors
try:
    response = requests.get("http://api.open-notify.org/iss-pass.json",params=query)
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)


#response.content() # Return the raw bytes of the data payload
#response.text() # Return a string representation of teh data payload
print(response.json()) # This method is convenient when the API returns JSON
print(response.headers["date"])

#Username / password auth
#requests.get('https://api.github.com/user',auth=HTTPBasicAuth('username','password'))
#


#access token
#my_headers = {'Authorization': 'Bearer{acess_token}'}
#response = requests.get('http://httpbin.org/headers',headers=my_headers)


#session = requests.Session()
#session.headers.update({'Authorization': 'Bearer{acess_token}'})
#response = session.get('https://httpbin.org/headres')


#redirects infinite loops
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)

#set maximum number of redirects
response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)   

#disable redirects
response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)


#ConnectionError
try:
    response = requests.get('http://api.open-notify.org/astros.json') 
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)

#Timeout Error
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
    # Code here will only run if the request is successful
except requests.Timeout as error:
    print(error)    

#all errors combine
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)    