#посчитать произведение числе, кратных 5

числа = [1,2,3,4,5,6,5,4,55,4,155,6,7,9,15]

произведение = 1

for x in числа:
    if x // 5 == x / 5:
        произведение *= x
        
        print(произведение)
