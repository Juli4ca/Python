for i in range(1,101):
    if (i > 20 and i%10 == 1) or i == 1:
        print(f'{i} процент')
    elif (i > 20 and (i%10 == 2 or i%10 == 3 or i%10 == 4)) or 2 <= i <= 4:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')