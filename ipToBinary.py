ip = input("Input your IPV4 address: ")
ip = ip.split(".")

mask = input("Input your mask(example: 255.255.255.0): ")
mask = mask.split(".")


print(f'''
    IP Address:
    {int(ip[0]):<8} {int(ip[1]):<8} {int(ip[2]):<8} {int(ip[3]):<8}
    {int(ip[0]):08b} {int(ip[1]):08b} {int(ip[2]):08b} {int(ip[3]):08b} 
    
    Mask:
    {int(mask[0]):<8} {int(mask[1]):<8} {int(mask[2]):<8} {int(mask[3]):<8}
    {int(mask[0]):08b} {int(mask[1]):08b} {int(mask[2]):08b} {int(mask[3]):08b} 
    ''')
