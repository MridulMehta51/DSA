# Minimize the Heights II
# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.


# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

arr = list(map(int,input("Enter array ").strip("").split(" ")))
k = int(input("Enter factor "))
n = int(input("Enter length "))
new_arr = []
arr_new = []
for i in range(n):
    if (arr[i]-k) < 0:
        new_arr.append(arr[i]+k)
        arr_new.append(arr[i]+k)
    else:
        new_arr.append(arr[i]-k)
        arr_new.append(arr[i]+k)
print(min(max(new_arr) - min(new_arr),(max(arr_new) - min(arr_new)),(max(new_arr) - min(arr_new)),(max(arr_new) - min(new_arr))))


# Aliter
arr.sort()
mindi= arr[-1]-arr[0]
for i in range(1,n):
    if arr[i]>=k:
        maxi=max(arr[i-1]+k, arr[-1]-k)
        mini=min(arr[0]+k, arr[i]-k)
        mindi= min(mindi,maxi-mini)
print(mindi)
