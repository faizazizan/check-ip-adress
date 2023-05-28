#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Check Any Web IP Adress

import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

# Example usage:
domain = "YOUR WEBSITE DOMAIN URL"
ip_address = get_ip_address(domain)

if ip_address:
    print(f"The IP address of {domain} is {ip_address}.")
else:
    print(f"Failed to retrieve the IP address for {domain}.")


# In[ ]:


## Check My IP Adress

import requests

def get_my_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            ip_address = data["ip"]
            return ip_address
    except requests.exceptions.RequestException:
        return None

# Example usage:
my_ip_address = get_my_ip_address()

if my_ip_address:
    print(f"Your IP address is: {my_ip_address}")
else:
    print("Failed to retrieve your IP address.")


# In[ ]:




