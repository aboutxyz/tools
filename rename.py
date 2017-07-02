#coding:utf-8

import os
strtext = ""
with open(os.getcwd()+"\\gurantee.txt","r") as filetext:
    strtext = filetext.read()

strlist = strtext.split()
path = "C:\Users\haish\Desktop\guarantee"
files=os.listdir(path)
files.sort(key=lambda x: int(filter(str.isdigit,x[-6:-4])))
for i in range(len(files)):
    os.rename(os.path.join(path,files[i]),os.path.join(path,strlist[i]+".doc"))