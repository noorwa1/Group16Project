"""
Registering functions
"""

import csv

targetlist=["ID","Username","Password","Title"]




def updateUser():
   with open('data.csv','a') as data_file:
       writer=csv.writer(data_file)
       writer.writerow(targetlist)



targetlist[0]=int(315198564)
targetlist[1]="Moradte"
targetlist[2]=int(1234567)
targetlist[3]="Manager"



updateUser()



