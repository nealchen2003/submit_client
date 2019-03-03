#!/usr/bin/python3
#coding=utf-8
#For Linux

import sys;
import getpass;
import urllib.request, requests;
from lxml import etree;

username='';
dest=None;

#To login destination
def login():
  global username;
  global localname;
  global dest;
  global urldst;
  urldst='';
  for url in ['https://internal.fzyzoi.tk', 'https://fzyzoi.tk']:
    try:
      urllib.request.urlopen(url, None, 3);
      urldst=url;
      break;
    except:
      print(url+' unable to connect.');
  if(urldst==''):
    print('Connection not available.');
    sys.exit(1);
  urldst=urldst+'/OnlineJudge';
  print('Login '+urldst);
  dest=requests.session();
  while True:
    username=input('User name: ');
    form={
      'username': username,
      'password': getpass.getpass('Password: ')
    };
    result=eval(dest.post(urldst+'/user.php', form).text, {'false': False, 'true': True});
    success=result['res'];
    if result['res']: break;
    print(result['msg']);
  print('Login Succeeded.');

#To submit code
def submit_code():
  if(dest==None): login();
  problem_id=input('Problem ID: ');
  localname=input("Local name: ");
  fstream=open(localname, "rb");
  form={
    'pid': problem_id,
    'compiler': 'G++',
    'code': fstream.read(),
    'submit': '提交'
  };
  result=dest.post(urldst+'/submit.php', data=form);
  print(result.text);

#main
while True:
  print('current user: '+username);
  cmd=input('q - Quit\nc - submit Code\n');
  if cmd=='q': break;
  if cmd=='c': submit_code();

# vim: set filetype=python expandtab ts=2 sts=2 sw=2 :
