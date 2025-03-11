def sum_rec(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_rec(item)
        else:
            total += item
    return total
test_list = [1, [2, [3, 4, [5]]]]
print(sum_rec(test_list))

def sum_iter(lst):
    total = 0
    stack = [lst]
    while stack:
        item = stack.pop()
        for element in item:
            if isinstance(element, list):
                stack.append(element)
            else:
                total += element
    return total
test_list = [1, [2, [3, 4, [5]]]]
print(sum_iter(test_list))

def rec(k):
    if k == 1:
        return 1, 1     
    a, b = rec(k-1)
    a_k = 0.5 * (b ** 0.5 + 0.5 * a ** 0.5) 
    b_k = 1.5 * b ** 0.5 + 0.5 * (a ** 2)
    return a_k, b_k
k = 700
a_k, b_k = rec(k)
print(f"a_{k} = {a_k}, b_{k} = {b_k}")

def iter(k):
    if k == 1:
        return 1, 1
    a, b = 1, 1
    for i in range(2, k + 1):
        a_k = 0.5 * (b ** 0.5 + 0.5 * a ** 0.5)
        b_k = 1.5 * b ** 0.5 + 0.5 * (a ** 2)
        a, b = a_k, b_k
    return a, b
a_k, b_k = iter(k)
print(f"a_{k} = {a_k}, b_{k} = {b_k}")