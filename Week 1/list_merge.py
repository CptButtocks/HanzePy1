def sortedMerge(L1, L2):
    for x in L2:
        L1.append(x);
    output = [];
    while L1:
        smallest = min(L1)
        index = L1.index(smallest)
        output.append(L1.pop(index))
    return output;

list1 = [1, 5, 3];
list2 = [4, 8, 1];

print(sortedMerge(list1, list2)); #[1, 1, 3, 4, 5, 8]
