devices2=[]
file=open("devices2.txt","r")
for item in file:
    item=item.strip()
    devices2.append(item)
file.close()
print(devices2)
