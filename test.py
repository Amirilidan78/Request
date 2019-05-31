# importing the requests library 
import requests 

# api-endpoint 
URL = "http://hotspot.vru.ac.ir/status"

# send Request to Url With Data

# post
r = requests.post('http://google.com', 
data = {
    'test':'test',
    })

# get
r = requests.get('http://google.com', 
data = {
    'test':'test',
    })

    