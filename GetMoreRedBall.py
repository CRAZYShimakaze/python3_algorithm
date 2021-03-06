# -*- coding: utf-8 -*-
'''
@Description: m红球个数，n白球个数，x拿球个数，求拿到红球多于白球的概率
@Date: 2019-09-04 21:33:59
@Author: CRAZYShimakaze
'''
def pro(m, n, x, y):
    if(y>x): return 0
    if(y==0): return 1
    if(y>m): return 0
    if(x-n>y): return 1
    p1 = pro(m-1,n,x-1,y-1)
    p2 = pro(m,n-1,x-1,y)
    return float(m/(m+n)*p1) + float(n/(m+n)*p2)

if __name__ == "__main__":
    while(1):
        m,n,x = map(int, input().strip().split())
        if m==n and n==x and x==0:
            break
        y = x//2+1
        print(pro(m,n,x,y))
        

