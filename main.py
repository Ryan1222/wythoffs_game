import math
s=((1.0+math.sqrt(5.0))/2.0)
while True:
    try:
        a,b =map(int,input('输入a,b空格隔开:').split())
        #a,b=map(int,input().strip().split())
        if a>b:
            a,b=b,a#a,b互换
        if(math.floor((b-a)*s)==a):
            print("0")#0代表后者失败
        else:
            print("1")#1代表后者胜利
    except:
        break