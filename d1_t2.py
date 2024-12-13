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

kv_store = {}
sum_score = 0
i = 0
j = 0
while i < len(arr1) and j < len(arr2): # good cond?
    print(f"we're at i = {i}, j = {j}")
    print(f"{arr1[i], arr2[j]}")
    num = arr1[i]

    # if they're equal, we look for how much (as arr are sorted)
    if arr1[i] == arr2[j]:
        if num not in kv_store.keys():
            kv_store[num] = 1
        else:
            kv_store[num] += 1
        j += 1

    elif arr1[i] < arr2[j]:
        i += 1

    elif arr1[i] > arr2[j]:
        j += 1

for k, v in kv_store.items():
    sum_score += k * v

print(sum_score)