#!/bin/python

def is_safe(arr):
    updown = {'up': 0, 'down': 0, 'eq': 0}
    is_safe_by_delta = False
    for i in range(1, len(arr)):
        delta = arr[i] - arr[i - 1]
        # print(f"Delta: {delta}")
        if abs(delta) > 0 and abs(delta) < 4: # 2 cmp are suboptimal, but best I can do now
            is_safe_by_delta = True
        else:
            return False 


        if delta < 0:
            updown['down'] += 1
        elif delta > 0:
            updown['up'] += 1
        else:
            updown['eq'] += 1

    return is_safe_by_delta and (updown['up'] == len(arr)-1 or updown['down'] == len(arr)-1)

safe_reports_cnt = 0
with open('input.txt', 'r') as f:
    reports = f.readlines()
    for r in reports:
        arr = list(map(int, r.split()))
        if is_safe(arr):
            safe_reports_cnt += 1
print(safe_reports_cnt)