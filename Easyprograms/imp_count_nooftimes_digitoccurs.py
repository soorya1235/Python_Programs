number = int(input("Enter the number"))
dic_no = {}
while number!=0:
    no = number % 10
    if no in dic_no:
        dic_no[no] = dic_no[no] + 1
    else:
        dic_no[no]=1
    number = number // 10
print(f'The Dictionary numbers are {dic_no}')
