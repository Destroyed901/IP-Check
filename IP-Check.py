import os
os.system("clear")
import requests, random, datetime, sys, time, argparse, os, json
from colorama import Fore, Back, Style
from termcolor import colored

def ip():
  print('Введите IP.')
  ip = input('—> ')
  response = requests.get('https://ipinfo.io/' + ip + '/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def self_ip():
  response = requests.get('https://ipinfo.io/json')
  r = response.json()
  try:
    try:
      print('[IP] : ' + r['ip'])
    except:
      pass
    try:
      print('[Страна] : ' + r['country'])
    except:
      pass
    try:
      print('[Регион] : ' + r['region'])
    except:
      pass
    try:
      print('[Город] : ' + r['city'])
    except:
      pass
    try:
      print('[Имя устройства] : ' + r['hostname'])
    except:
      pass
    try:
      print('[Местоположение] : ' + r['loc'])
    except:
      pass
    try:
      print('[Провайдер] : ' + r['org'])
    except:
      pass
    try:
      print('[Часовой пояс] : ' + r['timezone'])
    except:
      pass
    try:
      print('[Почтовый индекс] : ' +  r['postal'])
    except:
      pass
  except Exeption as er:
    print(er)
  print('----------')
  main()

def main():
  print('[1] Info about IP')
  print('[2] My IP')
  print('[0] Exit')
  a = input('>>> ')
  if a == '1':
    ip()
  elif a == '2':
    self_ip()
  elif a == '0':
    print('Stopped...')
    
  else:
    print('Error commands!')
    main()

def clear():
  if os.sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")
   
banner = colored("""
 __  .______        ______  __    __   _______   ______  __  ___ 
|  | |   _  \      /      ||  |  |  | |   ____| /      ||  |/  / 
|  | |  |_)  |    |  ,----'|  |__|  | |  |__   |  ,----'|  '  /  
|  | |   ___/     |  |     |   __   | |   __|  |  |     |    <   
|  | |  |         |  `----.|  |  |  | |  |____ |  `----.|  .  \  
|__| | _|          \______||__|  |__| |_______| \______||__|\__\ 
                    channel: https://t.me/eniac_tg
		
""", "green")

print(banner)
main()