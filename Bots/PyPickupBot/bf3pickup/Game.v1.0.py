#!/usr/bin/env python
import socket
import traceback, re
from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr
import random
from random import randint
from threading import Timer
import time
from time import strftime
import datetime

class Access_Lists:
        def isGeneralAccess(self,c,e,msg):
                if self.isSuper(c,e,msg)==True or self.isHigh(c,e,msg)==True:
                        return True
 
        def isHigh(self,c,e,msg):
                ac = open("Access_List_High.txt","r")
                high = ac.read()
                high = high.split("\n")
                ac.close()
                for block in high:
                        if block:
                                if block==e.nick:
                                        return True

        def isHighName(self,nick):
                ac = open("Access_List_High.txt","r")
                high = ac.read()
                high = high.split("\n")
                ac.close()
                for block in high:
                        if block:
                                if block==nick:
                                        return True
                                       
        def isSuper(self,c,e,msg):
                ac = open("Access_List_Super.txt","r")
                super1 = ac.read()
                super1 = super1.split("\n")
                ac.close()
                for block in super1:
                        if block:
                                if block==e.nick:
                                        return True

        def isSuperName(self,nick):
                ac = open("Access_List_Super.txt","r")
                super1 = ac.read()
                super1 = super1.split("\n")
                ac.close()
                for block in super1:
                        if block:
                                if block==nick:
                                        return True
                                       
        def writeHigh(self,c,e,msg):
                if len(msg.split(" "))>=3:
                        ac = open("Access_List_High.txt","a")
                        ac.write("%s\n" % (msg.split(" ")[3]))
                        ac.close()
                        c.notice(e.nick,"User added to High Access List")
       
        def writeSuper(self,c,e,msg):
                if len(msg.split(" "))>=3:
                        ac = open("Access_List_Super.txt","a")
                        ac.write("%s\n" % (msg.split(" ")[3]))
                        ac.close()
                        c.notice(e.nick,"User added to Super Access List")
                        writeHigh(c,e,msg)
       
        def removeHigh(self,c,e,msg):
                if len(msg.split(" "))>=3:
                        highbuffer=""
                        ac = open("Access_List_High.txt","r")
                        high = ac.read()
                        high = high.split("\n")
                        ac.close()
                        for block in high:
                                if block==msg.split(" ")[2]:
                                        c.notice(e.nick,"User removed from High Access List")
                                else:
                                        highbuffer=highbuffer+block+"\n"
                        ac = open("Access_List_High.txt","w")
                        ac.write(highbuffer)
                        ac.close()
                        removeSuper(c,e,msg)
                                               
        def removeSuper(self,c,e,msg):
                if len(msg.split(" "))>=3:
                        superbuffer=""
                        ac = open("Access_List_Super.txt","r")
                        super1 = ac.read()
                        super1 = super1.split("\n")
                        ac.close()
                        for block in super1:
                                if block==msg.split(" ")[2]:
                                        c.notice(e.nick,"User removed from Super Access List")
                                else:
                                        superbuffer=superbuffer+block+"\n"
                        ac = open("Access_List_Super.txt","w")
                        ac.write(superbuffer)
                        ac.close()
       
        def showHigh(self,c,e,msg):
                highbuffer=""
                ac = open("Access_List_High.txt","r")
                high = ac.read()
                high = high.split("\n")
                ac.close()
                for block in high:
                        if block:
                                highbuffer="%s[\x02%s\x02]" % (highbuffer,block)
                c.notice(e.nick,"High Access List Users:")
                if highbuffer == "":
                        c.notice(e.nick,"-")
                else:
                        c.notice(e.nick,highbuffer)
               
        def showSuper(self,c,e,msg):
                superbuffer=""
                ac = open("Access_List_Super.txt","r")
                super1 = ac.read()
                super1 = super1.split("\n")
                ac.close()
                for block in super1:
                        if block:
                                superbuffer="%s[\x02%s\x02]" % (superbuffer,block)
                c.notice(e.nick,"Super Access List Users:")
                if superbuffer == "":
                        c.notice(e.nick,"-")
                else:
                        c.notice(e.nick,superbuffer)
 
        def AccessList(self,c,e,msg):
                syntax="Syntax: \x02ACCESS \x1f[high/super]\x1f \x1f[add/remove/show]\x1f \x1f[user]\x1f\x02"
                if len(msg.split(" "))>=2:
                        if msg.split(" ")[1].lower()=="high":
                                if len(msg.split(" "))>=3:
                                        if msg.split(" ")[2].lower()=="add":
                                                if self.isSuper(c,e,msg)==True:
                                                        self.writeHigh(c,e,msg)
                                                else:
                                                        c.notice(e.nick,"You do not have access to this command")
                                        elif msg.split(" ")[2].lower()=="remove":
                                                if self.isSuper(c,e,msg)==True:
                                                        self.removeHigh(c,e,msg)
                                                else:
                                                        c.notice(e.nick,"You do not have access to this command")
                                        elif msg.split(" ")[2].lower()=="show":
                                                self.showHigh(c,e,msg)
                                        else:
                                                c.notice(e.nick,syntax)
                                else:
                                                c.notice(e.nick,syntax)
                               
                        elif msg.split(" ")[1].lower()=="super":
                                if len(msg.split(" "))>=3:
                                        if msg.split(" ")[2].lower()=="add":
                                                if self.isSuper(c,e,msg)==True:
                                                        self.writeSuper(c,e,msg)
                                                else:
                                                        c.notice(e.nick,"You do not have access to this command")
                                        elif msg.split(" ")[2].lower()=="remove":
                                                if self.isSuper(c,e,msg)==True:
                                                        self.removeSuper(c,e,msg)
                                                else:
                                                        c.notice(e.nick,"You do not have access to this command")
                                        elif msg.split(" ")[2].lower()=="show":
                                                self.showSuper(c,e,msg)
                                        else:
                                                c.notice(e.nick,syntax)
                                else:
                                        c.notice(e.nick,syntax)
                        else:
                                c.notice(e.nick,syntax)
                else:
                        c.notice(e.nick,syntax)

class Game:
        spots = []
        spotsTaken = 0
        servers= {'alpha': 'http://goo.gl/hfx7a', 'bravo' : 'http://goo.gl/qbzG0', 'charlie' : 'http://goo.gl/YQsfg'}
        servernames= {'alpha': 'ZA Pickup Alpha', 'bravo' : 'ZA Pickup Bravo', 'charlie' : 'ZA Pickup Charlie'}
        maps = {'seine' : 'Seine Crossing', 'metro' : 'Operation Metro', 'bazaar' : 'Grand Bazaar', 'tehran' : 'Tehran Highway', 'canals' : 'Noshahr Canals', 'peak' : 'Damavand Peak'}
        modes = {'squad':'Squad Rush 4v4','rush':'Rush 8v8','conquest':'Conquest 8v8'}
        game_mode = "conquest"
        game_on=False
        game_server="ZA BF3 Pick up server"
        game_map="Grand Bazaar"
        game_server_IP="http://goo.gl/hfx7a"
        game_admin=""
        game_attack=""
        game_defence=""
        channel="#battlefield3"
        news=""
	timer=None

        def do_topic(self,c,e):
                if self.game_on==True:
                        c.topic(e.target,"\x02\x0311,1| \x030BATTLEFIELD 3 \x0311|\x030 \x02Status: \x1fGame ON\x1f\x030 | Map: %s | Server: %s ( %s ) | Admin: %s | Mode: %s" % (self.game_map,self.game_server,self.game_server_IP,self.game_admin,self.game_mode))
                else:
                        c.topic(e.target,"'\x02\x0311,1|\x030 BATTLEFIELD 3 \x0311| \x02www.\x02\x030battlefieldza\x02\x0311.co.za \x0314\x95\x0311 www.\x02\x030bfza\x0311\x02.co.za \x02|\x02 \x030\x1fNews\x1f: %s " % (self.news))

        def setNews(self,c,e,news):
                self.news = news
                self.do_topic(c,e)

        def getNews(self):
                ac = open("News.txt","r")
                news = ac.read()
                news = news.split("\n")[0]
                return news
        
        def doNews(self,c,e,msg):
                if len(msg.split(" ")) >=2:
                        n = msg.split(" ")[1:]
                        n = " ".join(n)
                        ac = open("News.txt","w")
                        ac.write(n)
                        self.setNews(c,e,n)
        
        def start(self,c,e,msg):
                if self.game_on==False:
                        self.game_on=True
                        self.game_admin = e.nick
			if len(msg.split(" ")) == 1:
				self.game_mode = self.modes["conquest"]
				self.game_map="Grand Bazaar"
				self.game_server_IP=self.servers["alpha"]
				self.game_server=self.servernames["alpha"]
                        elif len(msg.split(" ")) == 2:
                                if msg.split(" ")[1] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[1].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[1].lower()]
                                elif msg.split(" ")[1] in self.maps:
                                        self.game_map=msg.split(" ")[1].lower()
                                elif msg.split(" ")[1] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[1].lower()]
                                else:
                                        c.notice(e.nick,"Invalid option, starting with defaults (Grand Bazaar, ZA Pickup Alpha, Conquest).")
                                        self.game_mode=self.modes["conquest"]
                                        self.game_map="Grand Bazaar"
                                        self.game_server_IP=self.servers["alpha".lower()]
                                        self.game_server=self.servernames["alpha"]
                        elif len(msg.split(" ")) == 3:
                                servSelected=True
                                mapSelected=True
                                modeSelected=True
                                message="Invalid option, starting with defaults ("
                                if msg.split(" ")[1] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[1].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[1].lower()]
                                elif msg.split(" ")[2] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[2].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[2].lower()]
                                else:
                                        servSelected=False
                                if msg.split(" ")[1] in self.maps:
                                        self.game_map=msg.split(" ")[1].lower()
                                elif msg.split(" ")[2] in self.maps:
                                        self.game_map=msg.split(" ")[2].lower()
                                else:
                                        mapSelected=False
                                if msg.split(" ")[1] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[1].lower()]
                                elif msg.split(" ")[2] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[2].lower()]
                                else:
                                        modeSelected=False
                                if not servSelected:
                                        message = message + "ZA Pickup Alpha, "
                                        self.game_server_IP=self.servers["alpha".lower()]
                                        self.game_server=self.servernames["alpha"]
                                if not mapSelected:
                                        message = message + "Grand Bazaar, "
                                        self.game_map="Grand Bazaar"
                                if not modeSelected:
                                        message = message + "Conquest, "
                                        self.game_mode=self.modes["conquest"]
                                if not servSelected or not mapSelected or not modeSelected:
                                        c.notice(e.nick,message+").")
                        elif len(msg.split(" ")) >= 4:
                                servSelected=True
                                mapSelected=True
                                modeSelected=True
                                message="Invalid option, starting with defaults ("
                                if msg.split(" ")[1] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[1].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[1].lower()]
                                elif msg.split(" ")[2] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[2].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[2].lower()]
                                elif msg.split(" ")[3] in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[3].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[3].lower()]
                                else:
                                        servSelected=False
                                if msg.split(" ")[1] in self.maps:
                                        self.game_map=msg.split(" ")[1].lower()
                                elif msg.split(" ")[2] in self.maps:
                                        self.game_map=msg.split(" ")[2].lower()
                                elif msg.split(" ")[3] in self.maps:
                                        self.game_map=msg.split(" ")[3].lower()
                                else:
                                        mapSelected=False
                                if msg.split(" ")[1] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[1].lower()]
                                elif msg.split(" ")[2] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[2].lower()]
                                elif msg.split(" ")[3] in self.modes:
                                        self.game_mode=self.modes[msg.split(" ")[3].lower()]
                                else:
                                        modeSelected=False
                                if not servSelected:
                                        message = message + "ZA Pickup Alpha, "
                                        self.game_server_IP=self.servers["alpha".lower()]
                                        self.game_server=self.servernames["alpha"]
                                if not mapSelected:
                                        message = message + "Grand Bazaar, "
                                        self.game_map="Grand Bazaar"
                                if not modeSelected:
                                        message = message + "Conquest, "
                                        self.game_mode=self.modes["conquest"]
                                if not servSelected or not mapSelected or not modeSelected:
                                        c.notice(e.nick,message+").")
                        if self.game_mode == self.modes["conquest"]:
                                self.spots = ["",]*16
                                self.game_defence = "\x034US: \x0314( " + " ) ( ".join(self.spots[:8]) + " )"
                                self.game_attack = "\x0312RU: \x0314( " + " ) ( ".join(self.spots[8:]) + " )"
			elif self.game_mode==self.modes["rush"]:
				self.spots = ["",]*16
				self.game_defence = "\x034DEF: \x0314( " + " ) ( ".join(self.spots[:8]) + " )"
				self.game_attack = "\x0312ATT: \x0314( " + " ) ( ".join(self.spots[8:]) + " )"
                        elif self.game_mode==self.modes["squad"]:
                                self.spots = ["",]*8
                                self.game_defence = "\x034DEF: \x0314( " + " ) ( ".join(self.spots[:4]) + " )"
                                self.game_attack = "\x0312ATT: \x0314( " + " ) ( ".join(self.spots[4:]) + " )"
			self.timer = None
                        self.do_topic(c,e)
                else:
                        c.notice(e.nick,"There is already a game")
               
        def stop(self,c,e,msg):
                if self.game_on==True:
                        self.game_on=False
                        self.spots = []
                        self.spotsTaken = 0
                        self.setNews(c,e,self.getNews())
                        if not self.timer == None:
                                self.timer.cancel()
                                self.timer = None
                else:
                        c.notice(e.nick,"There is no game")
               
        def showpool(self,c,e):
                if self.game_on==True:
                        if self.game_mode == self.modes["conquest"]:
                                self.game_defence = "\x034US: \x0314( " + " ) ( ".join(self.spots[:8]) + " )"
                                self.game_attack = "\x0312RU: \x0314( " + " ) ( ".join(self.spots[8:]) + " )"
                                c.privmsg(self.channel,"\x0314[\x02%s/16\x02]\x02Teams:\x02 %s %s" % (str(self.spotsTaken),self.game_defence,self.game_attack))
			elif self.game_mode == self.modes["rush"]:
				self.game_defence = "\x034DEF: \x0314( " + " ) ( ".join(self.spots[:8]) + " )"
				self.game_attack = "\x0312ATT: \x0314( " + " ) ( ".join(self.spots[8:]) + " )"
				c.privmsg(self.channel,"\x0314[\x02%s/16\x02]\x02Teams:\x02 %s %s" %(str(self.spotsTaken),self.game_defence,self.game_attack))
                        elif self.game_mode == self.modes["squad"]:
                                self.game_defence = "\x034DEF: \x0314( " + " ) ( ".join(self.spots[:4]) + " )"
                                self.game_attack = "\x0312ATT: \x0314( " + " ) ( ".join(self.spots[4:]) + " )"
                                c.privmsg(self.channel,"\x0314[\x02%s/8\x02]\x02Teams:\x02 %s %s" % (str(self.spotsTaken),self.game_defence,self.game_attack))
                else:
                        c.notice(e.nick,"There is no game")
                       
        def add(self,c,e,msg):
                if self.game_on==True:
                        if e.nick in self.spots:
                                c.notice(e.nick,"You are already in the pickup")
                        else:
                                added = False
                                a = 0
                                b = 15
                                if self.game_mode in [self.modes["conquest"],self.modes["rush"]]:
                                        a = 0
                                        b = 15
                                        if len(msg.split()) == 2:
                                                team = msg.split()[1]
                                                if team.lower() not in ['us', 'ru','def','att','defence','attack']:
                                                        c.notice(e.nick,"Usage: !add [RU|US] or !add [att|def]")
                                                        return
                                                if (team.lower() in ['us','def','defence']) and ('' in self.spots[:8]):
                                                        a = 0
                                                        b = 7
                                                elif (team.lower() in ['ru','att','attack']) and ('' in self.spots[8:]):
                                                        a = 8
                                                        b = 15
                                                else:
                                                        c.notice(e.nick,"That team is full")
                                                        return
                                elif self.game_mode == self.modes["squad"]:
                                        a = 0
                                        b = 7
                                        if len(msg.split()) == 2:
                                                team = msg.split()[1]
                                                if team.lower() not in ['def','att','defence','attack']:
                                                        c.notice(e.nick,"Usage: !add [att|def]")
                                                        return
                                                if (team.lower() in ['def','defence']) and ('' in self.spots[:4]):
                                                        a = 0
                                                        b = 3
                                                elif (team.lower() in ['att','attack']) and ('' in self.spots[4:]):
                                                        a = 4
                                                        b = 7
                                                else:
                                                        c.notice(e.nick,"That team is full")
                                                        return
				if '' in self.spots:
                                	while not added:
                                        	pos = randint(a, b)
                                        	if self.spots[pos] == "":
                                                	self.spots[pos] = e.nick
                                                	added = True
                                if added:
                                        self.spotsTaken += 1
                                        self.showpool(c,e)
                                        self.begin(c,e)
                else:
                        c.notice(e.nick,"There is no game")
               
        def remove(self,c,e):
                if self.game_on==True:
                        if e.nick in self.spots:
                                self.spots[(self.spots).index(e.nick)] = ""
                                self.spotsTaken = self.spotsTaken - 1
                                self.showpool(c,e)
				if not self.timer == None:
					self.timer.cancel()
					c.privmsg(e.target,"Waiting period timer has been cancelled.")
					self.timer = None
                        else:
                                c.notice(e.nick,"You are not in the pickup")
                else:
                        c.notice(e.nick,"There is no game")

        def forceremove(self,c,e,msg):
                if len(msg.split(" ")) >= 2:
                        if self.game_on==True:
                                player = msg.split(" ")[1]
                                if player in self.spots:
                                        self.spots[(self.spots).index(player)] = ""
                                        self.spotsTaken = self.spotsTaken - 1
                                        self.showpool(c,e)
                                        if not self.timer == None:
                                                self.timer.cancel()
                                                c.privmsg(e.target,"Waiting period timer has been cancelled.")
                                                self.timer = None
                                else:
                                        c.notice(e.nick,"Player is not in the pickup")
                        else:
                                c.notice(e.nick,"There is no game")

        def move(self,c,e,msg):
                if self.game_on==True:
                        if e.nick in self.spots:
                                if self.game_mode in [self.modes["conquest"],self.modes["rush"]]:
                                        if (self.spots.index(e.nick) < 8) and ("" in self.spots[8:]): # in team A and spot open in team B
                                                i = self.spots.index('', 8, 16) # get index of open spot in B
                                                n = self.spots.index(e.nick)
                                                self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                        elif (self.spots.index(e.nick) >= 8) and ("" in self.spots[:8]): # in team B and spot open in team A
                                                i = self.spots.index('', 0, 8) # get index of open spot in A
                                                n = self.spots.index(e.nick)
                                                self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                        else:
                                                c.notice(e.nick,"The other team is full.")
                                elif self.game_mode == self.modes["squad"]:
                                        if (self.spots.index(e.nick) < 4) and ("" in self.spots[4:]): # in team A and spot open in team B
                                                i = self.spots.index('', 4, 8) # get index of open spot in B
                                                n = self.spots.index(e.nick)
                                                self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                        elif (self.spots.index(e.nick) >= 4) and ("" in self.spots[:4]): # in team B and spot open in team A
                                                i = self.spots.index('', 0, 4) # get index of open spot in A
                                                n = self.spots.index(e.nick)
                                                self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                        else:
                                                c.notice(e.nick,"The other team is full.")
                                self.showpool(c,e)
                        else:
                                c.notice(e.nick,"You are not in the pickup")
                else:
                        c.notice(e.nick,"There is no game")

        def forcemove(self,c,e,msg):
                if len(msg.split(" ")) >= 2:
                        if self.game_on==True:
                                player = msg.split(" ")[1]
                                if player in self.spots:
                                        if self.game_mode in [self.modes["conquest"],self.modes["rush"]]:
                                                if (self.spots.index(player) < 8) and ("" in self.spots[8:]):
                                                        i = self.spots.index('', 8, 16)
                                                        n = self.spots.index(player)
                                                        self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                                elif (self.spots.index(player) >= 8) and ("" in self.spots[:8]):
                                                        i = self.spots.index('', 0, 8)
                                                        n = self.spots.index(player)
                                                        self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                                else:
                                                        c.notice(player,"The other team is full.")
                                                self.showpool(c,e)
                                        elif self.game_mode == self.modes["squad"]:
                                                if (self.spots.index(player) < 4) and ("" in self.spots[4:]):
                                                        i = self.spots.index('', 4, 8)
                                                        n = self.spots.index(player)
                                                        self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                                elif (self.spots.index(player) >= 4) and ("" in self.spots[:4]):
                                                        i = self.spots.index('', 0, 4)
                                                        n = self.spots.index(player)
                                                        self.spots[i], self.spots[n] = self.spots[n], self.spots[i] #swap
                                                else:
                                                        c.notice(player,"The other team is full.")
                                                self.showpool(c,e)
                                else:
                                        c.notice(e.nick,"Player is not in the pickup")
                        else:
                                c.notice(e.nick,"There is no game")

        def swap(self,c,e,msg):
                if self.game_on==True:
                        if len(msg.split(" ")) >= 3:
                                player1 = msg.split(" ")[1]
                                player2 = msg.split(" ")[2]
                                if(player1 in self.spots) and (player2 in self.spots):
                                        i1 = self.spots.index(player1)
                                        i2 = self.spots.index(player2)
                                        self.spots[i1], self.spots[i2] = player2, player1
                                        self.showpool(c,e)
                                else:
                                        c.notice(e.nick,"Players are not in the pickup")
                        else:
                               c.notice(e.nick,"You must specify two players")
                else:
                        c.notice(e.nick,"There is no game")
               
        def gameinfo(self,c,e):
                if self.game_on==True:
                        c.privmsg(e.target,"Status: Game On | Map: %s | Server: %s %s | Admin: %s | Mode: %s | Players: %s" % (self.game_map,self.game_server,self.game_server_IP,self.game_admin,self.game_mode,str(self.spotsTaken)))
                else:
                        c.privmsg(e.target,"Status: No Game on, ask an admin to start a game or join TeamSpeak to see if people are around for a game. Type !voip for TS details.")

        def lastgame(self,c,e):
                ac = open("LastGame.txt","r")
                last_map=""
                last_server=""
                last_server_IP=""
                last_admin=""
                last_time=""
		last_mode=""
                game = ac.read()
                game = game.split("\n")
                for block in game:
                        if block:
                                key = block.split(" ")[0]
                                if key == "Map:":
                                        last_map=block.split(" ")[1:]
                                elif key == "Server:":
                                        last_server=block.split(" ")[1:]
                                elif key == "IP:":
                                        last_server_IP=block.split(" ")[1:]
                                elif key == "Admin:":
                                        last_admin=block.split(" ")[1:]
                                elif key == "Date/time:":
                                        last_time=block.split(" ")[1:]
				elif key == "Mode:":
					last_mode=block.split(" ")[1:]
                ac.close()
                c.privmsg(e.target,"Last game: Map: %s | Server: %s %s | Mode: %s | Admin: %s | Date/Time: %s |" % (" ".join(last_map)," ".join(last_server)," ".join(last_server_IP)," ".join(last_mode)," ".join(last_admin)," ".join(last_time)))

        def lastteams(self,c,e):
                ac = open("LastGame.txt","r")
                defence=""
                attack=""
                game = ac.read()
                game = game.split("\n")
                for block in game:
                        if block:
                                key = block.split(" ")[0]
                                if key == "Defence:":
                                        defence=block.split(" ")[1:]
                                        defence=" ".join(defence)
                                elif key == "Attack:":
                                        attack=block.split(" ")[1:]
                                        attack=" ".join(attack)
				elif key == "RU:":
					attack=block.split(" ")[1:]
					attack=" ".join(attack)
				elif key == "US:":
					defence=block.split(" ")[1:]
					defence=" ".join(defence)
                ac.close()
                c.privmsg(e.target,"Last teams: "+defence+" "+attack+"")

        def cmap(self,c,e,msg):
                if len(msg.split(" ")) >= 2:
                        if self.game_on==True:
                                m = msg.split(" ")[1].lower()
                                if m in self.maps.keys():
                                        self.game_map = self.maps[m]
                                        self.do_topic(c,e)
                                else:
                                        c.notice(e.nick,"No such map")
                        else:
                                c.notice(e.nick,"There is no game")
       
        def cserver(self,c,e,msg):
                if len(msg.split(" ")) >= 2:
                        if self.game_on==True:
                                if msg.split(" ")[1].lower() in self.servers.keys():
                                        self.game_server_IP=self.servers[msg.split(" ")[1].lower()]
                                        self.game_server=self.servernames[msg.split(" ")[1].lower()]
                                        self.do_topic(c,e)
                                else:
                                        c.notice(e.nick,"No such server")
                        else:
                                c.notice(e.nick,"There is no game")

        def cadmin(self,c,e,msg):
                if len(msg.split(" ")) >= 2:
                        if self.game_on==True:
                                access = Access_Lists()
                                if (access.isHigh(c,e,msg) == True):
					if(access.isHighName(msg.split(" ")[1])):
	                                        self.game_admin=msg.split(" ")[1]
        	                                self.do_topic(c,e)
					else:
						c.notice(e.nick,msg.split(" ")[1]+" is not an admin.")
                                elif (access.isSuper(c,e,msg) == True):
					if(access.isSuperName(msg.split(" ")[1])):
	                                        self.game_admin=msg.split(" ")[1]
	                                        self.do_topic(c,e)
					else:
						c.notice(e.nick,msg.split(" ")[1]+" is not an admin.")
                        else:
                                c.notice(e.nick,"There is no game")

	def cmode(self,c,e,msg):
		if len(msg.split(" ")) >= 2:
			if self.game_on==True:
                                if msg.split(" ")[1].lower() in self.modes.keys():
                                        if msg.split(" ")[1].lower() in ["conquest","rush"]:
                                                self.game_mode = self.modes[msg.split(" ")[1].lower()]
                                                for i in range(16):
                                                        if i >= len(self.spots):
                                                                self.spots.append("")
                                                self.do_topic(c,e)
                                                c.privmsg(e.target,"The game mode has been changed to "+self.game_mode)
                                                if not self.timer == None and self.spotsTaken < 16:
                                                        self.timer.cancel()
                                                        self.timer = None
                                                        c.privmsg(e.target,"Waiting period timer has been cancelled.")
                                        elif msg.split(" ")[1].lower() == "squad" and self.spotsTaken <= 8:
                                                self.game_mode = self.modes[msg.split(" ")[1].lower()]
                                                spots = ["",]*8
                                                j = 0
                                                for i in range(len(self.spots)):
                                                        if self.spots[i] not in [""]:
                                                                spots[j] = self.spots[i]
                                                                j += 1
                                                self.spots = spots
                                                self.do_topic(c,e)
                                                c.privmsg(e.target,"The game mode has been changed to "+self.game_mode)
                                                self.begin(c,e)
                                        else:
                                                c.notice(e.nick,"You need 8 players or less to change to squad rush mode.")
                                else:
                                        c.notice(e.nick,"Not a valid mode. Choose one of: squad,rush,conquest")

        def shuffle(self,c,e):
                c.privmsg(e.target,"Now shuffling the teams...")
                random.shuffle(self.spots)
                self.showpool(c,e)
                                
        def part(self,c,e):
                nick = nm_to_n(e.source())
                if self.game_on==True:
                        if nick in self.spots:
                                self.spots[(self.spots).index(nm_to_n(e.source()))] = ""
                                self.spotsTaken = self.spotsTaken - 1
                                c.privmsg(self.channel,"\x02"+nick+"\x02 has been removed from the pickup.")
                                self.showpool(c,e)

        def kick(self,c,e,nick):
                if self.game_on==True:
                        if nick in self.spots:
                                self.spots[(self.spots).index(nick)] = ""
                                self.spotsTaken = self.spotsTaken - 1
                                c.privmsg(self.channel,"\x02"+nick+"\x02 has been removed from the pickup.")
                                self.showpool(c,e)
       
        def nick(self,c,e):
                if self.game_on==True:
                        if nm_to_n(e.source()) in self.spots:
                                self.spots[(self.spots).index(nm_to_n(e.source()))] = e.target()
                                if self.game_admin == nm_to_n(e.source()):
                                        self.game_admin == e.target()
                                        self.do_topic(c,e)
                        elif self.game_admin == nm_to_n(e.source()):
                                self.game_admin == e.target()
                                self.do_topic(c,e)


        def saveLastGame(self,server,ip,map,admin,attack,defence,mode):
                time = strftime("%Y-%m-%d %H:%M:%S")
                ac = open("LastGame.txt","w")
		block = ""
		if mode in [self.modes["squad"],self.modes["rush"]]:
                	block = "Server: "+server+"\nIP: "+ip+"\nMap: "+map+"\nMode: "+mode+"\nAdmin: "+admin+"\nDate/time: "+time+"\nAttack: "+attack+"\nDefence: "+defence
		else:
			block = "Server: "+server+"\nIP: "+ip+"\nMap: "+map+"\nMode: "+mode+"\nAdmin: "+admin+"\nDate/time: "+time+"\nRU: "+attack+"\nUS: "+defence
                ac.write("%s" % (block))
                ac.close()

        def showRules(self,c,e):
                c.notice(e.nick,"To view the full list of rules visit: http://goo.gl/P5dqN")
                c.notice(e.nick,"Type !weapons to see disallowed weapons")

        def showWeapons(self,c,e):
                c.notice(e.nick,"\x02Disallowed weapons, add-ons and equipment:\x02")
                c.notice(e.nick,"Weapons: L85A2 / G18 Pistol")
		c.notice(e.nick,"Add-ons: M320 Explosive/Buck / GP-30 Explosive/Buck / M26 Mass/Dart / Tactical light including pistols / IRNV including vehicles / 12G Frag")
		c.notice(e.nick,"Equipment: MAV")
       
	def begin(self,c,e):
		if self.game_mode in [self.modes["conquest"],self.modes["rush"]] and self.spotsTaken==16:
			c.privmsg(e.target,"The game will begin in 60 seconds. Changes to the game can still be made.")
			self.timer = Timer(60.0,self.doBegin,[c,e])
			self.timer.start()
		elif self.game_mode == self.modes["squad"] and self.spotsTaken == 8:
			c.privmsg(e.target,"The game will begin in 60 seconds. Changes to the game can still be made.")
			self.timer = Timer(60.0,self.doBegin,[c,e])
			self.timer.start()

        def doBegin(self,c,e):
		c.privmsg(e.target,"\x034The player pool is full. Please make your way to the server and join the relevant Teamspeak Channels.")
                c.privmsg(e.target,"\x034Players will be notified with the current game information (Server URL and Password)")
                c.privmsg(self.channel,self.game_defence)
                c.privmsg(self.channel,self.game_attack)
                for block in self.spots:
                        if block:
                                c.privmsg(block,"Please join the following server: %s ( %s ) with password: gamezone" % (self.game_server,self.game_server_IP))
                                c.privmsg(block,"Teamspeak 3 Server: dwarf.mweb.co.za:9987 - Channel: #Bf3 - Password: bf3")
                c.privmsg(self.game_admin,"The teams for your pickup are as follows:")
                c.privmsg(self.game_admin,self.game_defence)
                c.privmsg(self.game_admin,self.game_attack)
                self.spotsTaken = 0
                self.game_on=False
                self.setNews(c,e,self.getNews())
                self.saveLastGame(self.game_server,self.game_server_IP,self.game_map,self.game_admin,self.game_attack,self.game_defence,self.game_mode)
		self.saveStats()
                self.spots = []
		
	def saveStats(self):
		file = open('stats.txt','r')
		fileArr = file.read()
		file.close()
		fileArr = fileArr.split("\n")
		newFileArr = []
		totalPickups = 1
		for line in fileArr:
			if line not in [""]:
				if len(line.split(":")) > 1:
					totalPickups = totalPickups + int(line.split(":")[1])
				elif len(line.split(" ")) > 1:
					args = line.split(" ")
					name = args[0]
					stat = int(args[1])
					if name in self.spots:
						self.spots.remove(name)
						stat +=1
					newFileArr.append((name,stat))
		for player in self.spots:
			if player:
				newFileArr.append((player,1))
		file = open('stats.txt','w')
		file.write("%s\n" % ("total:" + (str(totalPickups))))
		for i in newFileArr:
			file.write("%s\n" %(i[0] + " " + str(i[1])))
		file.close()

	def doTotal(self,c,e):
                file = open("stats.txt",'r')
                lines = file.read()
                lines = lines.split("\n")
                for line in lines:
                        if len(line.split(":")) > 1:
                                c.privmsg(e.target,"A total of "+line.split(":")[1]+" pickups have been played.")

	def doStats(self,c,e,msg):
		file = open("stats.txt",'r')
		players = file.read()
		file.close()
		players = players.split("\n")
		if len(msg.split(" ")) > 1:
			for player in players:
				if len(player.split(" ")) > 1:
					if player.split(" ")[0] == msg.split(" ")[1]:
						c.privmsg(e.target,msg.split(" ")[1]+" has played "+player.split(" ")[1]+" pickups.")
		else:
			for player in players:
				if len(player.split(" ")) > 1:
					if player.split(" ")[0] == e.nick:
						c.privmsg(e.target,"You have played "+player.split(" ")[1]+" pickups.")

        def ts(self,c,e):
                c.notice(e.nick,"MWEB Teamspeak Server: dwarf.mweb.co.za:9987 - Channel: #Bf3 - Password: bf3")

        def showMaps(self,c,e):
                c.notice(e.nick,"Current maps: "+", ".join(self.maps.values()))

        def listservers(self,c,e,msg):
                serverlist=""
                for key in self.servers.keys():
                        serverlist = serverlist + key +" ( "+self.servers[key]+" ), "
                c.notice(e.nick,"Current servers: "+serverlist)

class Protection:
        unick = ""
        uident = ""
        uaddress = ""
        uchannels = ""
        ubanned = {}
        uready = False
        cmd = ""
        target = ""
        nick = ""
        reason = ""
 
        def do_Commands(self,c,e):
                if self.cmd in ['whois','wi']:
                        self.whois(c,e)
                elif self.cmd in ['ban','b']:
                        self.ban(c,e)
                elif self.cmd in ['kick','k']:
                        self.kick(c,e)
                elif self.cmd in ['kb','kickban']:
                        self.ban(c,e)
                        self.kick(c,e)
                elif self.cmd in ['unb','unban','remb','removeban','remban','ub']:
                        self.unban(c,e)
                elif self.cmd in ['aop']:
                        self.aop(c,e)
                elif self.cmd in ['deaop']:
                        self.deaop(c,e)
                elif self.cmd in ['hop']:
                        self.hop(c,e)
                elif self.cmd in ['dehop']:
                        self.dehop(c,e)
                elif self.cmd in ['vop']:
                        self.vop(c,e)
                elif self.cmd in ['devop']:
                        self.devop(c,e)
                               
       
        def get_Commands(self,c,e,msg):
                self.cmd = msg.split(" ")[0]
                self.target = e.target
                if len(msg.split(" "))>1:
                        self.nick = msg.split(" ")[1]
                        nick = []
                        nick.append(msg.split(" ")[1])
                        message = msg.split(" ")
                        del message [:2]
                        self.reason = " ".join(message)
                        c.whois(nick)
                        c.whowas(self.nick)
 
        def whois(self,c,e):
                c.privmsg(self.target,"Nick: %s | Ident: %s | Address: %s" % (self.unick,self.uident,self.uaddress))
               
        def whowas(self,c,e):
                c.privmsg(self.target,"Nick: %s | Ident: %s | Address: %s" % (self.unick,self.uident,self.uaddress))
       
        def getUser(self,c,e):
                self.unick=e.arguments()[0]
                self.uident=e.arguments()[1]
                self.uaddress=e.arguments()[2]
               
        def unban(self,c,e):
                if self.nick in self.ubanned.keys():
                        c.mode(self.target,self.ubanned[self.nick])
               
        def ban(self,c,e):
                 c.mode(self.target,"+bbb %s!*@* *!%s@* *!*@%s" % (self.unick,self.uident,self.uaddress))
                 self.ubanned[self.unick] = ("-bbb %s!*@* *!%s@* *!*@%s" % (self.unick,self.uident,self.uaddress))
       
        def kick(self,c,e):
                c.kick(self.target,self.unick,self.reason)
       
        def aop(self,c,e):
                c.mode(self.target,"+o %s" % (self.unick))
                access = Access_Lists()
                access.writeSuper(self,c,e,"access add super "+e.nick)
               
        def deaop(self,c,e):
                c.mode(self.target,"-o %s" % (self.unick))
                access = Access_Lists()
                access.removeSuper(self,c,e,"access remove super "+e.nick)
               
        def vop(self,c,e):
                c.mode(self.target,"+v %s" % (self.unick))
       
        def devop(self,c,e):
                c.mode(self.target,"-v %s" % (self.unick))
                 
        def dehop(self,c,e):
                c.mode(self.target,"-h %s" % (self.unick))
                access = Access_Lists()
                access.removeHigh(self,c,e,"access add high "+e.nick)


class Command_Message:
                def __init__(self, e, msg):
                        self.event_type     = e.eventtype()         # event type is pubmsg, privmsg,etc
                        self.source         = e.source()            # source user's nick mask
                        self.target         = e.target()            # target user/channel to reply to
                        self.nick           = nm_to_n(e.source())   # source user's nickname
                        self.raw_message    = msg                   # raw message sent by user
                        self.command        = msg.split()[0].lower()# command string is the first word
                        self.payload        = None                  # payload is the first argument
                        self.args           = None                  # all arguments given after command
                        self.arguments      = None
                        if len(msg.split()) >= 2:
                                self.payload    = msg.split()[1]
                                self.args       = msg.split()[1:]
                                self.arguments  = msg[len(self.command)+1:]
       
class BF3Pickup(SingleServerIRCBot):
 
        def __init__(self, channel, nickname, server, port=6667):
                self.game = Game()
                SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
                self.channel = channel
                self.protect = Protection()
                self.connection.add_global_handler("all_events", self.on_all_events, -100)
 
        def on_all_events(self, c, e):
                if e.eventtype() != "all_raw_messages":
                        print e.source(), e.eventtype().upper(), e.target(), e.arguments()
 
        def on_nicknameinuse(self, c, e):
                c.nick(c.get_nickname() + "_")
 
        def on_join(self, c, e):
                nick = nm_to_n(e.source())
                c.notice(nick,"Welcome to #battlefield3. For the rules type !rules. Please report all bugs on the bot to Russ.")
               
        def on_part(self, c, e):
                GB = self.game
                GB.part(c,e)

        def on_kick(self, c, e):
                GB = self.game
                nick = e.arguments()[0]
                GB.kick(c,e,nick)
               
        def on_quit(self, c, e):
                GB = self.game
                GB.part(c,e)
               
        def on_nick(self, c, e):
                GB = self.game
                GB.nick(c,e)

        def on_whoisuser(self, c, e):
                self.protect.getUser(c,e)
                self.protect.do_Commands(c,e)
       
        def on_whoiswas(self, c, e):
                self.protect.getUser(c,e)
                self.protect.do_Commands(c,e)
       
        def on_welcome(self, c, e):
                c.privmsg("NickServ","identify <password>")
                c.mode(c.get_nickname, "+B")
                c.join(self.channel)
 
        def on_privmsg(self, c, e):
                self.do_command(e, e.arguments()[0])
                self.do_commandProt(e, e.arguments()[0])
 
        def on_pubmsg(self, c, e):
                args = e.arguments()[0].split()
                if len(args) > 1 and irc_lower(args[0]).startswith(irc_lower(c.get_nickname())):
                        if args[1] == "":
                                return
                        self.do_command(e, " ".join(args[1:]).strip())
                elif e.arguments()[0][0] == '!':
                        if len(e.arguments()[0])>=2:
                                self.do_command(e, (" ".join(args)[1:]).strip())
                elif e.arguments()[0][0] == '$':
                        if len(e.arguments()[0])>=2:
                                self.do_commandProt(e, (" ".join(args)[1:]).strip())
 
        def do_command(self, e, msg):
                c = self.connection
                e = Command_Message(e, msg)
                GB = self.game
		access = Access_Lists()
                isAdminCommand=False
		if access.isGeneralAccess(c,e,msg):
                        isAdminCommand = True
	                if e.command == "die":
        	                if e.nick.lower() in ['Russ']:
                	                self.die("Killed by admin (%s)" % e.nick)
                        elif e.command in ['forcemove','move']:
        	                GB.forcemove(c,e,msg)
                	elif e.command in ['forceremove','forcerem']:
                        	GB.forceremove(c,e,msg)
	                elif e.command in ['swap']:
        	                GB.swap(c,e,msg)
                	elif e.command in ['map','cmap','changemap']:
                        	GB.cmap(c,e,msg)
                	elif e.command in ['server','cserver','changeserver']:
                        	GB.cserver(c,e,msg)
                	elif e.command in ['cadmin','admin','changeadmin']:
                        	GB.cadmin(c,e,msg)
			elif e.command in ['cmode','mode','changemode']:
				GB.cmode(c,e,msg)
			elif e.command in ['shuffle']:
                                GB.shuffle(c,e)
			elif e.command in ['start','sg','startgame']:
                                GB.start(c,e,msg)
	                elif e.command in ['cg','cancel','stop','cancelgame']:
        	                GB.stop(c,e,msg)
        	        elif e.command in ['whois','wi','kick','k','ban','b','kickban','kb','unb','unban','remb','removeban','remban','aop','deaop','vop','devop','dehop']:
                                self.protect.get_Commands(c,e,msg)
                        elif e.command in ['setnews']:
        	                GB.doNews(c,e,msg)
                        else:
                                isAdminCommand = False
                if e.command in ['rules']:
                        GB.showRules(c,e)
                elif e.command in['time']:
                        time = strftime("%Y-%m-%d %H:%M:%S")
                        c.privmsg(e.target,"The time is "+time)
                elif e.command in ['weapons']:
                        GB.showWeapons(c,e)
                elif e.command in ['maps']:
                        GB.showMaps(c,e)
                elif e.command in ['pool','pools','team','teams']:
                        GB.showpool(c,e)
                elif e.command in ['add','addme']:
                        GB.add(c,e,msg)
                elif e.command in ['rem','remove','removeme']:
                        GB.remove(c,e)
                elif e.command in ['moveme']:
                        GB.move(c,e,msg)
                elif e.command in ['game','info','gameinfo','status']:
                        GB.gameinfo(c,e)
                elif e.command in ['lastgame']:
                        GB.lastgame(c,e)
                elif e.command in ['lastteams','lastpool','lastpools','lastteam']:
                        GB.lastteams(c,e)
                elif e.command in ['voip','mumble', 'ts']:
                        GB.ts(c,e)
                elif e.command == 'servers':
                        GB.listservers(c,e,msg)
                elif e.command == 'stats':
                        GB.doStats(c,e,msg)
                elif e.command == 'total':
                        GB.doTotal(c,e)
                elif e.command in ['join']:
                        c.join("#battlefield3")
                elif e.command in ['bf3stats']:
                        c.notice(e.nick, "Running Battlefield3 stat bot")
                elif e.command in ['bf3update']:
                        c.notice(e.nick, "Running Battlefield3 stat update")
                elif e.command in ['help','cmds','commands']:
                        c.notice(e.nick,"Commands: !add , !rem , !moveme , !game , !lastgame , !teams , !lastteams, !servers, !stats, !total")
                       # if access.isGeneralAccess(c,e):
                               # c.notice(e.nick,"Admin commands: !sg <map_name> <server> <mode>, !cg, !forcerem <name>, !shuffle")
                               # c.notice(e.nick,"!forcemove <name>, !swap <name1> <name2>, !map <map_name>, !server <server_name>")
                               # c.notice(e.nick,"!mode <mode>, !kick <name> <reason>, !kickban <name> <reason(WITH DATE TO UNBAN)>")
                #else:
                        #if not isAdminCommand:
                                #c.notice(e.nick, "Invalid command (Ask for 'help'): " + e.command)

        def do_commandProt(self, e, msg):
                c = self.connection
                e = Command_Message(e, msg)
                GB = self.game
                if e.command in ['access']:
                        access = Access_Lists()
                        access.AccessList(c,e,msg)
                 
def main():
        import sys
   
        if len(sys.argv) > 1:
                if len(sys.argv) != 4:
                        print "Usage: BF3Pickup <server[:port]> <channel> <nickname>"
                        sys.exit(1)
   
                s = str.split(sys.argv[1], ":", 1)
                server = s[0]
                if len(s) == 2:
                        try:
                                port = int(s[1])
                        except ValueError:
                                print "Error: Erroneous port."
                                sys.exit(1)
                else:
                        port = 6667
                channel = sys.argv[2]
                nickname = sys.argv[3]
       
                bot = BF3Pickup(channel, nickname, server, port)
        else:
                bot = BF3Pickup("#battlefield3", "BF3Pickup", "za.shadowfire.org", 6667)
        try:
                bot.start()
        except KeyboardInterrupt:
                print "^C - Exiting gracefully..."
                bot.disconnect("Terminated at terminal.")
                sys.exit(0)
 
if __name__ == "__main__":
        main()
