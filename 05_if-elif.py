aclNum = int(input("What is IPv4 ACL number ? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a STANDART IPv4 ACL.")
elif aclNum >= 100 and aclNum <= 199:
    print("This is an EXTENDED IPv4 ACL.")
else:
    print("This is not a STANDART or EXTENDED IPv4 ACL. ")
