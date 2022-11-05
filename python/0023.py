D ,M=map(int,input().split())
month=['31','28','31','30','31','30','31','31','30','31','30','31']
Day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(M-1):
    D+=int(month[i])
print(Day[(D+2)%7])