import os
print("[-]you shoud run this command as sudo user ")
o = open("/home/mohamed/Desktop/users.txt")
li = o.readlines()
for i in li :
	os.system("useradd "+i)
print("[+]users was added ")
	

