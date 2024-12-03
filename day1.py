#!/usr/bin/python3

arr1 = []
arr2 = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        x, y = map(int, l.split())

        arr1.append(x)
        arr2.append(y)

arr1.sort()
arr2.sort()

total_diff = 0

i = 0
while i < len(arr1):
    diff = 0
    if arr1[i] > arr2[i]:
        diff = arr1[i] - arr2[i]
    if arr1[i] < arr2[i]:
        diff = arr2[i] - arr1[i]

    total_diff += diff
    i += 1

print(total_diff)