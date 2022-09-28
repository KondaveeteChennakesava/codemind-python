p,r,t=map(int,input().split())
ans=p*(pow((1+r/100),t))
print('{:.2f}'.format(ans))