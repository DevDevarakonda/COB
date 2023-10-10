with open('filename.txt','r')as file:
    a=file.read()
    b=a.split()
    dic={}
    for i in b:
        dic[i]=dic.get(i,0)+1
    for i,j in dic.items():
        print(f"{b}:{j}")