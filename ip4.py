def check(n):
    a=n.split(".")
    if len(a)!=4:
        return False
    for i in a:
        if not(i.isdigit() or int(i)<0 or int(i)>255):
            return False
        return True
    
n=input("Enter the IPv4 address:-")
if check(n):
    print("IPv4 is valid")
else:
    print("Ipv4 is not valid")