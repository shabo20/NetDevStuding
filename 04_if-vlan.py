nativeVLAN = input("Please input number of native VLAN ? ")
dataVLAN = input("Please input number of data VLAN ? ")
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("The native VLAN and the data VLAN are different.")
