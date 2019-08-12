file=open("devices2.txt","r")
for item in file:
    item=item.strip()
    print(item)
file.close()
