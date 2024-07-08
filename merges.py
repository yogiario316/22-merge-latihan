nama = ["Yogi Ario Pratama", "2313020004", "Merge & Short"]
for i in nama:
    print(i)

def merge_list(l1, l2):
    sorted_list1 = sorted(l1)
    sorted_list2 = sorted(l2)
    merge_list =  []
    p,o = 0,0
    while p < len(sorted_list1) and o < len(sorted_list2):
        if sorted_list1[p] < sorted_list2 [o]:
            merge_list.append(sorted_list1[p])
            p += 1
        else:
            merge_list.append(sorted_list2[o])
            o += 1
    while p < len(sorted_list1):
        merge_list.append(sorted_list1[p])
        p +=1
    while o < len(sorted_list2):
        merge_list.append(sorted_list2[o])
        o +=1
    return sorted_list1, sorted_list2