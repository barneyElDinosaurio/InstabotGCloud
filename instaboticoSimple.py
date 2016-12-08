#!/usr/bin/env python
import sys, os
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time

#Pidiendo datos a usuario
varUser = raw_input("mete el user name: ")
varPass = raw_input("aqui el password: ")
tags_array = list()

num = raw_input("Aqui va el numero de tags a agregar:")
print 'Aqui vienen los tags: '
for i in range(int(num)):
	#pidiendo tags por separado
    n = raw_input("tag :")
    tags_array.append(n)
print 'ARRAY: ',tags_array

#Bot en auto_mod
bot = InstaBot(varUser, varPass,
               
               tag_list = tags_array
               )
bot.auto_mod()