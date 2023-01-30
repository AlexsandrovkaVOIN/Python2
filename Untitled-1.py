
print("Введите год: ")
god = int(input())
sum = 0
dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if(god % 4 == 0):
    dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for x in range(1, len(dict)+1):
    dey = dict[x]
    i = 1
    while dey >= i:
        if(i >= 10):
            stroka = str(i)
            sum += int(stroka[0]) + int(stroka[1])
        else:
            sum += i
        i += 1
print(sum)