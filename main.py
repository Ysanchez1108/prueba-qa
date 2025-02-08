def sort_list(input_list):
    print(input_list)
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    print(input_list)
    return input_list

lista =[3,4,6,8,1,9]
sort_list(lista)
