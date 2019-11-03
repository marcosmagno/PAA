def findSubSequency(arr,k):
    current_seq = 0
    changes = 0

    for i in arr:
        if i % 2 == 1:
            current_seq = current_seq + 1
        else:
            if current_seq > k:
                changes = current_seq - k
                current_seq = 0
    return changes


v = [2,3,5,7,9,11,12]
print(findSubSequency(v, 3))