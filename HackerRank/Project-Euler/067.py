#Author: Andres Felipe Ortega Montoya - Luis Miguel Marin Loaiza
#HackerRank Project Euler #67 - Maximum path sum II

tc = int(input().strip())
for i in range(tc):
	n = int(input().strip())
	list = []
	for j in range(n):
		list.append([int(i) for i in input().strip().split(" ")])
	for j in range(1,n):
	  for k in range(n-j):
	    list[-j-1][k]
	    list[-j-1][k]+= max(list[-j][k], list[-j][k+1])
	print(list[0][0])
