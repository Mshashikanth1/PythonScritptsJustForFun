#greedy approach:
#first take read coins and sort them
#allways choose the coin which is greater than 
#available in coins and less than the amount
#this will not give correct for every coin set


C=list(map(int,input().split()))
res=0
co=0
rest=""
am=int(input())
while am!=0:
      for i in range(len(c)-1,-1,-1):
          if am>=c[i]:
             res=c[i]
      am-=res
      rest+=("+"+str(res))
      co+=1
print(rest[1:])
print(co)
