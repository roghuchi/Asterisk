import os
import datetime
import re
import shutil


#Keep only 6 months

#Find out how long it should be kept
date = (datetime.date.today() - datetime.timedelta(6*365/12)).isoformat()
x = re.search("(\d*)-(\d*)-(\d*)", date)
year = x.group(1)
mon = x.group(2)

folder_path_1 = '/var/spool/asterisk/monitor/'

#list of years folders
list1 = os.listdir (folder_path_1)
list1 = [int(i) for i in list1]

#Delete old records
for j in list1:
        if j < int(year):
                shutil.rmtree(folder_path_1+str(j))
        else:
                folder_path_2=folder_path_1+year
                list2 = os.listdir (folder_path_2)
                list2 = [int(i) for i in list2]
                for i in list2:
                        if i < int(mon):
                                if i <10:
                                        shutil.rmtree(folder_path_2+"/0"+str(i))
                                else:
                                        shutil.rmtree(folder_path_2+"/"+str(i))
print ("finish")
