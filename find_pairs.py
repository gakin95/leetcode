def find_pairs(arr1, arr2,target):
    output = []
    for num in arr2:
       diff = target - num
       if diff in set(arr1):
           output.append((diff, num))
    return output




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)