import time 
cool = ["hell0",'i',"am","divad"]
p=5
print(p)
time.sleep(0.5)
while p<10:
    s =cool[abs(p-len(cool))]
    p-=1
    print(s)
    time.sleep(0.5)