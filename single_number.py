def single_number(array):
    output=0
    for i in range(len(array)):
        output=output^array[i]
    return output

array=list(map(int,input().split()))
print(single_number(array))