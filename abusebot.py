# -*- coding: utf-8 -*- 

import random
import linecache

eol='\n'
buffsize = 1024

with open('./.qqbot-tmp/plugins/AbuseBot/dict.txt', 'rb') as handle:
    linenum = 0
    buffer = handle.read(4096)
    while buffer:
        linenum += buffer.count(eol)
        buffer = handle.read(buffsize)

		
def onQQMessage(bot, contact, member, content):
    #isMe?
    if bot.isMe(contact, member) or (contact.ctype != 'buddy' and member.qq == bot.conf.qq):
        time.sleep(0.1)
        return

    name = str(member)
    name = name.replace('成员','')
    name = name.replace('"','')

    #辱骂
    with open('./.qqbot-tmp/plugins/AbuseBot/list.json','r') as namelist:
        target = namelist.read(16)
        if name in target:
            randline = random.randint(1,linenum)
            reply = linecache.getline(r'dict.txt', randline)
            bot.SendTo(contact,'@'+name+' '+reply.replace("\n", ""))

    #debug
    if content == 'debug':
        bot.SendTo(contact,'bot='+str(bot)+' contact='+str(contact)+' member='+str(member)+' content='+str(content))
    if content == '?member':
        print(member)
        bot.SendTo(contact,str(member))
