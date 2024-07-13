n = int(input().strip())

for i in range(n):
    input_data = input().strip().split(" ")
    
    for j in input_data:
        print(j[::-1], end=" ")
        
        # for k in range( -1, -len(input_data[j]) -1, -1):
        #     print(f"{input_data[j][k]}", end="")
            
        # print(" ", end="")
    
    print("")