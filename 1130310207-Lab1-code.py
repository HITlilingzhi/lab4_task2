# -*- coding: utf-8 -*-
#price代表第几个字母第多少组的价格
#stability代表第几个字母第多少组的稳定性
from __future__ import print_function

#import datetime,time
global Q,TR,TP,max_value
#starttime = datetime.datetime.now()

Q=0
TR=0
TP=0
max_value=0
prefix=[0]*30
appear_list = [0] * 30
dp = [([0] * 3010) for i in range(30)]  
method = [([0] * 3010) for i in range(30)]
answer = [0] * 30
service = [([''] * (501)) for i in range(22+1)]   
price = [([0] * (501)) for i in range(22+1)]    
mapping = [([0] * (501)) for i in range(22+1)]
stability = [([0] * (501)) for i in range(22+1)]

f_ser = open('SERVICE.txt','r')
f_pro = open('PROCESS.txt','r')
f_req = open('REQ.txt','r')
service_temp = f_ser.readlines()
process_temp = f_pro.readlines()
req_temp = f_req.readlines()
f_pro.close()
f_req.close()
f_ser.close()
letter_number = service_temp.__len__()/500
for count_j in range(500):
    price[0][count_j] = 0
    stability[0][count_j] = 0
for count_i in range(letter_number):
    tot = 0
    for count_j in range(500):
        service[count_i][count_j] = (service_temp[count_i*500+count_j].split(' '))
        tmp = (int(float(service[count_i][count_j][4])*100+1e-8))
        if(tmp <=3000):    
            price[count_i+1][tot] = tmp
            stability[count_i+1][tot] = (float(service[count_i][count_j][2]))            
            mapping[count_i+1][tot] = count_j            
            tot+=1

def DP(i,j):
    if(j<0):
        return 0 
    if(prefix[i]>j):
         return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    x = appear_list[i]
    ret = 0
    for k in range(500):
        if(price[x][k]==0):
            break
        tmp =DP(i-1,j-price[x][k]) * stability[x][k]
        if(j >= price[x][k] and ret < tmp):
            ret = tmp
            method[i][j]=k
    dp[i][j] = ret
    return ret

def solve(n,min_stability):     
    global Q,TR,TP
    Q = -0x7fffffff
    TR = 0
    TP = 0
    dp[0][0] = 1    
    prefix[0] = 0    

    for i in range(1,n):
        x = appear_list[i]
        prefix[i] = 0x7fffffff
        for j in range(500):
            if(price[x][j]==0):
                break
            prefix[i] = min(prefix[i], prefix[i-1] + price[x][j])
x
    for i in range(1,max_value+1):
        dp[0][i] = 0
    for i in range(1,n+1):
        for j in range(max_value+1):
            dp[i][j]=-1
    
    for i in range(0,max_value+1):
        tmp = DP(n,i)
        if(Q < tmp - i / 10000.0):
            Q = tmp - i / 10000.0
            TR = tmp
            TP = i/100.0
    tmp = TP*100
    for i in range(n,0,-1):
       answer[appear_list[i]] = method[i][int(tmp+1e-8)]
       tmp -= price[appear_list[i]][answer[appear_list[i]]]

for test in range(4):
    process_matrix = [([0] * 15) for i in range(15)] 
    how_many_letters = [0] * 15
    s = process_temp[test]
    fomart = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in s:
        if not c in fomart:
            s = s.replace(c,'')
    i = 0
    req_n = 0
    while i<len(s)-1:
        #print s[i]
        flag = 0
        for j in range(1,req_n+1):
            if(appear_list[j]==ord(s[i])-64):
                flag = 1
        if(not flag):
            appear_list[req_n+1] = ord(s[i])-64
            req_n += 1
        i += 1
    while i<len(s)-1:
        process_matrix[ord(s[i])-64][ord(s[i+1])-64] = 1  #(A,B)则(1,2)等于1
        how_many_letters[ord(s[i])-64] = 1
        how_many_letters[ord(s[i])-64] = 1
        i += 2
    req_max_value = int(float(req_temp[test][6:8]) *100+1e-8)
    req_min_stability = int(float(req_temp[test][1:5])*100+1e-8)
    max_value=req_max_value
    solve(req_n,req_min_stability)
    flag = 0    
    for i in range(len(s)):
        if(not flag):
            print ("(%c-%d,"%(s[i],mapping[ord(s[i])-64][answer[ord(s[i])-64]]+1),end='')
        else:
            print ("%c-%d),"%(s[i],mapping[ord(s[i])-64][answer[ord(s[i])-64]]+1),end='')
        flag^=1
    print ('')
    print ("Reliability=%f,Cost=%f,Q=%f\n"%(TR,TP,Q))

#    endtime = datetime.datetime.now()
#    print (endtime)  
#print (starttime)