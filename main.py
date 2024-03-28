import requests
import threading
# import discord
import time
import json
import getpass 
import sys
import argparse
from playsound import playsound
class bot:
    def __init__(self):
        # self.TOKEN = "7192623363:AAHtoA9rmaDtBDYzY64s2j5IUkOUX4BIq6o"
        self.username = ""
        self.password = ""
        self.param_for_look = ""
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--user", help="give the username", required=True)
        parser.add_argument("-p", "--param", help="give the username", required=True)
        arg = parser.parse_args()
        self.username = arg.user
        self.password = getpass.getpass("[*] Enter your password : ")
        self.param_for_look = arg.param
        # intents = discord.Intents.default()
        self.ticket_list = []
        # # intents.message_content = True
        # self.client = discord.Client(intents=intents)
        # self.bot = telebot.TeleBot(self.TOKEN)
        
    def ticket_check(self):
        payload = {"os_username":self.username, "os_password":self.password}
        req = requests.Session()
        loging = req.post("https://sm.hostiran.com/secure/Dashboard.jspa", data=payload)
        if loging.status_code == 200:
            print("[+] You are logged in successfully !")
            # try:
            print(self.check(req))
            # except Exception as e:
            #     print(f"[X] Exception as : {e}")
        if loging.status_code != 200:
            print("[X] Failed to login to server !")
            sys.exit(1)

    def check(self, sess):
        while True:
            # try:
                js_data = sess.get('https://sm.hostiran.com/rest/servicedesk/1/servicedesk/HCS/issuelist?asc=true&issuesPerPage=50&columnNames=issuekey&columnNames=summary&columnNames=status&columnNames=customfield_10400&columnNames=assignee&columnNames=reporter&columnNames=updated&columnNames=lastViewed&columnNames=labels&excludeLinkedToMajorIncidents=false&jql=project+%3D+HCS+AND+issuetype+in+(Support%2C+%22Admin+Time%22)+AND+status+in+(Open%2C+Reopened%2C+Pending%2C+Canceled%2C+%22In+Progress%22%2C+Waiting%2C+%22Waiting+for+customer%22%2C+Escalated)+AND+labels+is+EMPTY&startIndex=0&orderBy=assignee')
                with open(".tmp.js", 'wb+') as out:
                    # print(type(js_data.text))
                    # js =  js_data.text.replace(",","\n")
                    out.write(bytes(js_data.text.encode()))
                js_file = open(".tmp.js")
                js_obj = json.load(js_file)
                for issue in js_obj.get("issues"):
                    # if "HCS-387351" in issue.get("fields")[0]:
                    # print(f"[{self.param_for_look}]")
                    # print("[*] Issue : ",issue.get("fields")[4].get("fieldAsHtml"))
                    if self.username in issue.get("fields")[4].get("fieldAsHtml") or self.param_for_look in issue.get("fields")[4].get("fieldAsHtml").strip():
                        print(issue.get("fields")[1].get("fieldAsHtml").split("\n")[1].split(">")[1].split("<")[0])
                        print("https://sm.hostiran.com"+issue.get("fields")[0].get("fieldAsHtml").split("<a")[-1].split("href=")[-1].split("</a>")[0].split('"')[1])
                        txt = "{}\n{}".format(issue.get("fields")[1].get("fieldAsHtml").split("\n")[1].split(">")[1].split("<")[0], "https://sm.hostiran.com"+issue.get("fields")[0].get("fieldAsHtml").split("<a")[-1].split("href=")[-1].split("</a>")[0].split('"')[1])
                        if txt not in self.ticket_list:
                            self.ticket_list.append(txt)
                            print("[+] Found a pair : ", txt)
                            playsound("alarm.mp3")
                            playsound("alarm.mp3")
                            
                        if txt not in self.ticket_list:
                            time.sleep(10)
                    else:
                        time.sleep(20)
                        # return txt
            # except:
                # print("[*] Reached timeout for 5 seconds ....")
                # time.sleep(5)

                # print(issue.get("fields")[4])

                # for part in issue.get("fields"):
                #     # if "e.bahadori@hostiran.com" in part:
                #     print(part,)



            # sys.exit(1)
            # time.sleep(5)
    # def bot_send_message(self, message, txt):
    #     pass

        # self.bot.send_message(message, txt)
    def run(self):
        self.ticket_check()
        # @self.client.event
        # async def on_ready():
            # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
            # guild_count = 0

            # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
            # for guild in self.client.guilds:
                # PRINT THE SERVER'S ID AND NAME.
                # print(f"- {guild.id} (name: {guild.name})")

                # INCREMENTS THE GUILD COUNTER.
                # guild_count = guild_count + 1

            # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
            # print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

        # EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
        # @self.client.event
        # async def on_message(message):
        #     # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
        #     if message.content == "hello" or message.content == "start":
        #         # SENDS BACK A MESSAGE TO THE CHANNEL.
        #         await message.channel.send("Hello , write p:password and u:username\nin form of u:username,p:password\nthen send it to me to start looking for you tickets ")
        #     if "p:" in message.content and "u:" in message.content:
                # self.username = message.content.split(",")[0].split(":")[-1]
                # self.password = message.content.split(",")[-1].split(":")[-1]
                # # if "u:" in self.username and "p:" in self.password:
                # await message.channel.send(f"start looking for ticket assign to {self.username} ... ")
                # while True:
                #     if 'stop' in message.content:
                #         time.sleep(300)
                #     if 'kill' in message.content:
                #         message.channel.send("killing the bot!")
                #         message.channel.send("Goodbye!")
                #         sys.exit(1)
                #     mess = self.ticket_check()
                #     if mess:
                #         await message.channel.send(mess)
                #         # await message.channel.send("timeout 5")
                #         time.sleep(30)
                #     else:
                #         await message.channel.send("timeout 5")
                #         time.sleep(300)
                # # f"start looking for ticket assign to {self.username} ... this is the second test ")

        # self.client.run("MTIxODEyNjExNTg4NjA3MTkwMA.GPtjcV.e44OleeIfTVDDL4uetwCZDjM8CfXHlhD4fDgNY")
        # def do(message):
        #     self.bot.send_message(message, "Start checking your account ! ")
        #     self.ticket_check(message)
        # self.bot.polling()

te = bot()
te.run()