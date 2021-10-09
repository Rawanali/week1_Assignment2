#  Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def fun(fun_list):
    for i in range(len(fun_list)):
        if fun_list[i] > 0:
            fun_list[i] = "big"
    return fun_list
            
            
f_list = [1,-1,-2,-3,3,4,5,6]
new_list = fun(f_list)
print(new_list)


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def positive_num(p_list):
    count = 0 
    for i in range(len(p_list)):
        if p_list[i] > 0:
            count+= 1 
    p_list[-1] = count 
    return p_list

f_list = [1,-1,-2,-3,3,4,4,7,6,5,4,9,5,6]
new_list1 = positive_num(f_list)
print(new_list1)


#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def fun_sum(s_list):
    sum = 0 
    for i in range(len(s_list)):
        sum = sum + s_list[i]
    
    return sum

f_list = [3,4,4,7,6,5,4,9,5,6]
print(fun_sum(f_list))


# Average - Create a function that takes a list and returns the average of all the values.
def fun_avg(a_list):
    sum = 0 
    avg = 0 
    for i in range(len(a_list)):
        sum = sum + a_list[i]
    avg = sum / len(a_list)
    
    return avg

f_list = [3,4,4,7,6,5,4,9,5,6]
print(fun_avg(f_list))


#  Length - Create a function that takes a list and returns the length of the list.
def fun_len(l_list):
    count = 0 
    for i in range(len(l_list)):
        count +=1 
    
    return count

f_list = [3,4,4,7,6,5,4,9,5,6]
print(fun_len(f_list))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. (Optional) If the list is empty, have the function return False.
def fun_min(mn_list):
    min = mn_list[0]
    if len(mn_list) == 0 :
            min = False
    for i in range(len(mn_list)):
        if mn_list[i] < min :
            min = mn_list[i]
        
    
    return min

f_list = [193884,8234986,98729864,49174]
print(fun_min(f_list))


# Maximum - Create a function that takes a list and returns the maximum value in the array. (Optional) If the list is empty, have the function return False.
def fun_max(mx_list):
    max = mx_list[0]
    if len(mx_list) == 0 :
             max = False
    for i in range(len(mx_list)):
        if mx_list[i] > max :
            max = mx_list[i]
        
    
    return max

f_list = [193884,8234986,98729864,49174]
print(fun_max(f_list))


# Ultimate Analysis (Optional) - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(a_list):
    sum_total = 0 
    avg = 0 
    count = 0 
    min = a_list[0]
    max = a_list[0]
    for i in range(len(a_list)):
        sum_total = sum_total + a_list[i]
        if a_list[i] > max:
            max = a_list[i]
        elif a_list[i] < min:
            min = a_list[i]
        count += 1
            
                
    avg = sum_total / count
    my_dic = {'sum':sum_total ,'average': avg ,'minimum': min ,'maximum':max,'length':count}
    return my_dic

print(ultimate_analysis([37,2,1,-9]))


# Reverse List (Optional) - Create a function that takes a list and returns that list with values reversed. Do this without creating a second list.
def reverse_list(r_list):
    last_item = 0 
    for i in range(len(r_list)):
        last_item = r_list.pop()
        r_list.insert(i,last_item)
        
    return r_list
print(reverse_list([37,2,1,-9]))


  
