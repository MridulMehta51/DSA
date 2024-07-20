# Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.
arr = list(map(int,input("Enter the array ").strip().split()))
print(arr)
minimum = min(arr)
maximum =max(arr)
ans,sol = 0,0
res = []
for i in range(len(arr)):
    if arr[i] >= 0:
        ans += arr[i]
        sol += arr[i]
        res.append(ans)
        if (sol !=0):
            res.append(sol)
    else :
        ans += arr[i]
        res.append(ans)
        if (sol !=0):
            res.append(sol)
        sol = 0
if  maximum > max(res):
    print(maximum)
else :
    print(max(res))
    
# 1 4 5 -9 8 6 -8 10
