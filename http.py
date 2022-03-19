# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:39:50 2022

@author: User
"""

import http.client


HOST = input("enter the host's ip")
PORT= input("enter the port")
URL = input("enter the url")

if (PORT == ""):
    PORT = 80
    
try:
    #the http.client module defines classes that implement the client side of HTTP and HTTPS protocols
    connection = http.client.HTTPConnection(HOST, PORT)
    #sending http request , the first parameter is the method, the second is the url
    connection.request('GET' , URL)
    response = connection.getresponse()
    print("The server's response", response.status)
except ConnectionRefusedError:
    print("connection failed")