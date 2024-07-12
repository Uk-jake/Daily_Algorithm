def print_order(input_list, n, m):

    print_queue = [int(value) for value in input_list]

    idx = 0
    count = 0

    while True:
        
        idx = idx % n
        
        if print_queue[idx] >= max(print_queue):
            count += 1

            if (idx == m):
                break

            print_queue[idx] = 0

        idx += 1
    
    return count


answer_list = []

testcase_count = int(input().strip())

for i in range(testcase_count):
    n, m = map(int, input().strip().split())
    print_queue = input().strip().split()
    # int_list = [int(value) for value in print_queue]

    # print(f"n : {n} , m : {m}")
    # print(f"int_list : {int_list}")

    answer_list.append(print_order(print_queue, n, m))
    
for i in answer_list:
    print(i)