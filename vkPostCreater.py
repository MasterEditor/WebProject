#!/usr/bin/env python
import os
import sys
import time
import datetime
import vk
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


#start of the programm
print("Console Application is loading... Please, don't close it")
print("Console Application loaded")
now = datetime.datetime.now()
logReader = open("log %d_" % now.hour + "%d_" % now.day + "%d_" % now.month + "%d_" % now.year + ".txt", "w+",) #open the log
logReader.write("[%d." % now.second + "%d." % now.minute + "%d." % now.hour + "%d." % now.day + "%d." % now.month + "%d]" % now.year + " Start of the programm\n") # write [data] Start of the programm
logReader.write("[%d." % now.second + "%d." % now.minute + "%d." % now.hour + "%d." % now.day + "%d." % now.month + "%d]" % now.year + " Waiting...")
while True:
    n = datetime.datetime.now()
    if n.hour == 16 and n.minute == 57:
        session = vk.AuthSession(app_id='6106140', user_login='375295722933', user_password='Jediacademy1',
                                 scope='messages')
        api = vk.API(session)
        q = api.messages.send(chat_id="41", message="Проверка", attachment="photo-142863411_456239019,photo-142863411_456239020,photo-142863411_456239021,photo-142863411_456239022,photo-142863411_456239023,photo-142863411_456239024,photo-142863411_456239025,photo-142863411_456239026,photo-142863411_456239027,photo-142863411_456239028,photo-142863411_456239029")
        logReader.write("[%d." % now.second + "%d." % now.minute + "%d." % now.hour + "%d." % now.day + "%d." % now.month + "%d]" % now.year + " Photo have been added")
        time.sleep(60)
