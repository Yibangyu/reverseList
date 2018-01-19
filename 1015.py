#!/usr/bin/python

row_line = input()

B,N,K = row_line.split()
N,K = int(N),int(K)

dt = {}
li = []
li1 = []

#linkedList = {"000000":{"element":4,"next":"999999"},"00100":{"element":1,"next":"12309"},"68237":{"element":6,"next":"-1"},"33218":{"element":3,"next":"000000"},"999999":{"element":5,"next":"68237"},"12309":{"element":2,"next":"33218"}}


for i in range(N):
    row_line = input()
    tmp_list = list(row_line.split())
    tmp_dict = {"element":tmp_list[1],"next":tmp_list[2]}
    dt[tmp_list[0]] = tmp_dict


currKey,currNode = B,dt[B]
while True:
    tmp_list = [currKey,currNode['element'],currNode['next']]
    li.append(tmp_list)
    if currNode['next'] != '-1' and dt[currNode['next']]:
        currKey = currNode['next']
        currNode = dt[currKey]
    else:
        break

node = 0

while True:
    
    tmp_li = li[node:(node+K)]
    if(len(tmp_li) == K):
        tmp_li.reverse()
        li1.extend(tmp_li)
        node = node+K
    else:
        li1.extend(tmp_li)
        break

for index in range(0,len(li1)-1):
    li1[index][2] = li1[index+1][0]

for item in li1:
    print(' '.join(item))

