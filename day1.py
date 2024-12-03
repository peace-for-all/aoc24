#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = f.readlines()
    total_diff = 0
    for l in lines:
        arr = list(map(int, l.strip().split()))
        
        if arr[0] == arr[1]:
            continue # adds 0 anyway
        if arr[0] > arr[1]:
            diff = arr[0] - arr[1]
        if arr[0] < arr[1]:
            diff = arr[1] - arr[0]
        total_diff += diff
    print(total_diff)