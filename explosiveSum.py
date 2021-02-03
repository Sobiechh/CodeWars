def exp_sum(n):
    ans = []
    ans.append(n)
    for x in range(1, n):
        b= []
        for y in range(1, n-x):
            b.append(x)
        ans.append(b)
    return ans

a = exp_sum(5)
print(a)

def subgrups(my_list):
    partitions = partition(len(my_list))
    permed = []
    for each_partition in partitions:
        permed.append(set(itertools.permutations(each_partition, len(each_partition))))

    for each_tuple in itertools.chain(*permed):
        yield list(slice_by_lengths(each_tuple, deepcopy(my_list)))