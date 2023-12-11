 # # # # # r =0
 # # # # # for i in range(0, 3):
 # # # # #     for j in range(0, 4):
 # # # # #         r += j
 # # # # # print(r)
 # # # # # a = "HGJOYOKJ"
 # # # # a = "AAAAAAFd"
 # # # # b = len(a)
 # # # # c = True
 # # # # i = 0
 # # # # while (i < b / 2) or c: 
 # # # #     if a[i] != a[b - i - 1]:
 # # # #         print(a[i], a[b - i - 1])
 # # # #         c = False
 # # # #         i += 1
 # # # # print('res', c)
 # # # # num = int(input())
 # # # # flag = True
 # # # # for i in range(2, num // 2 + 1):
 # # # #     if num % i == 0:
 # # # #         flag = False
 # # # # if num > 1 and flag == True:
 # # # #     print('Число простое')
 # # # # else:
 # # # #     print('Число составное')
 # # # # count = 0
 # # # # p = 1
 # # # # for i in range(1, 3):
 # # # #     x = int(input())
 # # # #     if x > 0:
 # # # #         p = p * x
 # # # #         count = count + 1
 # # # # if count > 0:
 # # # #     print(x)
 # # # #     print(p)
 # # # # else:
 # # # #     print('NO')
 # # # # num = int(input())
 # # # # max1 = 0
 # # # # flag = True
 # # # # while num > 0:
 # # # #     last_num = num % 10
 # # # #     num = num // 10
 # # # #     if last_num % 3 == 0:
 # # # #         flag = False
 # # # #         if last_num > max1:
 # # # #             max1 = last_num
 # # # # if flag == True:
 # # # #     print("NO")
 # # # # else: 
 # # # #     print(max1)
 # # # # num = int(input())
 # # # # mult = 1
 # # # # while num > 0:
 # # # #     last_num = num % 10
 # # # #     num = num // 10
 # # # #     mult *= last_num
 # # # # print(mult)
 # # # # num = int(input())
 # # # # for i in range(num):
 # # # #     for j in range(3):
 # # # #         print(num, end=" ")
 # # # #     print()
 # # # num = int(input())
 # # # for i in range(1, num + 1):
 # # #     for j in range(i):
 # # #         print(i, end = "")
 # # #     print()
 # # # a = int(input())
 # # # b = int(input())
 # # # max1 = 0
 # # # temp = 0
 # # # for num in range(a, b + 1):
 # # #     sum = 0
 # # #     for i in range(1, num + 1):
 # # #         if num % i == 0:
 # # #             sum += i
 # # #     if sum >= max1:
 # # #         max1 = sum
 # # #         temp = i
 # # # print(temp, max1)
 # # # num = int(input())
 # # # for i in range(1, num + 1):
 # # #     print(i, end="")
 # # #     for j in range(1, i + 1):
 # # #         if i % j == 0:
 # # #             print("+", end = "")
 # # # #     print()
 # # # num = int(input())
 # # # sum = 0
 # # # sum2 = 0
 # # # sum3 = 0
 # # # while num > 0:
 # # #     last_num = num % 10
 # # #     sum = last_num + sum
 # # #     num = num // 10
 # # # if sum > 9:
 # # #     num2 = sum
 # # #     while num2 > 0:
 # # #         last_num2 = num2 % 10
 # # #         sum2 = last_num2 + sum2
 # # #         num2 = num2 // 10
 # # #     num3 = sum2
 # # #     while num3 > 0:
 # # #         last_num3 = num3 % 10
 # # #         sum3 = last_num3 + sum3
 # # #         num3 = num3 // 10
 # # #     print(sum3)
 # # # else:
 # # #     print(sum)
 # # # def fact(n):
 # # #     mult = 1
 # # #     for i in range(1, n + 1):
 # # #         mult = i * mult
 # # #     return mult
 # # # num = int(input())
 # # # sum = 0
 # # # for j in range(1, num + 1):
 # # #     res = fact(j)
 # # #     sum += res
 # # # print(sum)
 # # # def simple_num(n):
 # # #     flag = True
 # # #     for i in range(2, n):
 # # #         if n % i == 0:
 # # #             flag = False
 # # #             break
 # # #     return flag
 # # # a = int(input())
 # # # b = int(input())
 # # # for i in range(a,b + 1):
 # # #     simp1 = simple_num(i)
 # # #     if simp1 == True and i != 1:
 # # #         print(i)
 # # # for i in range(10, 5, -1):
 # # #     print(i)
 # # # num = int(input())
 # # # for i in range(num):
 # # #     for j in range(19):
 # # #         if i == 0 or i == num - 1:
 # # #             print("*", end = "")
 # # #         else:
 # # #             if j == 0 or j == 18:
 # # #                 print("*", end = "")
 # # #             else:
 # # #                 print(" ", end = "")
 # # # #     print()
 # # # num = int(input())
 # # # while num > 0:
 # # #     last_num = num % 10
 # # #     num = num // 10
 # # #     print(last_num)
 # # num = int(input())
 # # num2 = num
 # # counter = 0
 # # counter_last = 0
 # # counter_chet = 0
 # # sum5 = 0
 # # proizv = 1
 # # sum05 = 0
 # # sum = 0
 # # sum1 = 0
 # # mult = 1
 # # last_one = num % 10
 # # while num != 0:
 # #     last = num % 10
 # #     if last == 3:
 # #         counter += 1
 # #     if last == last_one:
 # #         counter_last += 1
 # #     if last % 2 == 0:
 # #         counter_chet += 1
 # #     if last > 5:
 # #         sum5 += last
 # #     if last > 7:
 # #         proizv *= last
 # #     if last == 0 or last == 5:
 # #         sum05 += 1

 # #     sum += last 
 # #     sum1 += 1
 # #     mult *= last
 # #     num = num // 10
 # # sred = sum / sum1
 # # step = 10 ** (sum1 - 1)
 # # print(counter)
 # # print(counter_last)
 # # print(counter_chet)
 # # print(sum5)
 # # print(proizv)
 # # print(sum05)

# # # # # # # # text = input()

# # # # # # # # num = (len(text) / 2)
# # # # # # # # isEven = len(text) % 2
# # # # # # # # num2 = int(num)

# # # # # # # # tex2 =text[:num2 + isEven]
# # # # # # # # if text[num2:] == tex2[::-1]:
# # # # # # # #     print("YES")
# # # # # # # # else:
# # # # # # # #     print("NO")

# # # # # # # # text = input()
# # # # # # # # print(len(text))
# # # # # # # # print(text*3)
# # # # # # # # print(text[:1])
# # # # # # # # print(text[:3])
# # # # # # # # print(text[-3:])
# # # # # # # # print(text[::-1])
# # # # # # # # print(text[1:-1])

# # # # # # # text = input()
# # # # # # # num = (len(text) / 2)
# # # # # # # isEven = len(text) % 2
# # # # # # # num2 = int(num)

# # # # # # # tex2 = text[:num2]
# # # # # # # texOdd = text[:num2+1]


# # # # # # # if isEven:
# # # # # # #     print(text[num2+1:] + texOdd)
# # # # # # # else:
# # # # # # #     print(text[num2:] + tex2)
# # # # # # # # if text[num2:] == tex2[::-1]:
# # # # # # # #     print("YES")
# # # # # # # # else:
# # # # # # # #     print("NO")

# # # # # # # name = input()
# # # # # # # if name == name.title():
# # # # # # #     print("YES")
# # # # # # # else:
# # # # # # #     print("NO")

# # # # # # # text = input()
# # # # # # # print(text.swapcase())

# # # # # # # text = input()

# # # # # # # flag = False
# # # # # # # text2 = text.lower()
# # # # # # # if text2.find("хорош") != -1:
# # # # # # #     flag = True
# # # # # # # if flag:
# # # # # # #     print("YES")
# # # # # # # else:
# # # # # # #     print("NO")

# # # # # # text = input()
# # # # # # counter = 0

# # # # # # for i in range(len(text)):
# # # # # #     text2 = text[i].lower()
# # # # # #     if text[i] in '0123456789':
# # # # # #         continue
# # # # # #     if text2 == text[i]:
# # # # # #         counter +=1
# # # # # # print(counter)

# # # # # s = 'foo bar foo baz foo qux'
# # # # # print(s.replace('foo', 'grault'))

# # # # # text = input()
# # # # # print(text.count(" ")+1)

# # # # # gen = input()
# # # # # a = gen.count("а") + gen.count("А")
# # # # # g = gen.count("г") + gen.count("Г")
# # # # # c = gen.count("ц") + gen.count("Ц")
# # # # # t = gen.count("т") + gen.count("Т")
# # # # # print("Аденин:", a)
# # # # # print("Гуанин:", g)
# # # # # print("Цитозин:", c)
# # # # # print("Тимин:", t)

# # # # num = int(input())
# # # # counter = 0
# # # # for i in range(num):
# # # #     text = input()
# # # #     counter2 = text.count("11")
# # # #     if counter2 >= 3:
# # # #         counter += 1
# # # # print(counter)

# # # # text = input()
# # # # print(text.count("0") + text.count("1")+ text.count("2")+ text.count("3")+ text.count("4")+ text.count("5")+ text.count("6")+ text.count("7")+ text.count("8")+ text.count("9"))

# # # text = input()
# # # flag = False
# # # if text.endswith(".com") or text.endswith(".ru"):
# # #     print("YES")
# # # else:
# # #     print("NO")

# # # text = input()
# # # counter = 0
# # # symbol = " "
# # # for i in range(len(text)):
# # #     if text.count(text[i]) >= counter:
# # #         counter = text.count(text[i])
# # #         symbol = text[i]
# # # print(symbol)

# # text = input()
# # index = text.find("f")
# # last_index = text.rfind("f")

# # if index == -1:
# #     print("NO")
# # elif index == last_index:
# #     print(index)
# # elif last_index > index:
# #     print(index, last_index)

# text = input()
# first = text.find("h")
# last = text.rfind("h")

# text2 = text[:first]
# text3 = text[last+1:]
# print(text2 + text3)

# num = int(input())
# text = input()
# for i in range(len(text)):
#     ord1 = ord(text[i])
#     ord1 = ord1 - num
#     raznic = 0
#     if ord1 < 97:
#         raznic = 97 - ord1
#         ord1 = 122 - raznic+1
#         print(chr(ord1), end='')
#     else:
#         print(chr(ord1), end='')
# text = input()
# for i in range(len(text)):
#     if i % 3 != 0:
#         print(text[i], end="")
# text = input()
# for i in range(len(text)):
#     if text[i] == "1":
#         print("one", end="")
#     else:
#         print(text[i], end="")

# text = input()
# counter = 0
# for i in range(len(text)):
#     if text[i] == 'f':
#         counter += 1
#         if counter == 2:
#             print(i)
#             break
# if counter == 1:
#     print("-1")
# if counter == 0:
#     print("-2")

# text = input()
# index1 = text.find("h")
# index2 = text.rfind("h")

# print(text[:index1+1], end="")
# text_center = text[index1+1:index2:]
# print(text_center[::-1], end="")
# print(text[index2:], end="")

# num = int(input())
# list1 = list(range(1, num + 1))
# print(list1)

# num = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# list1 = list(abc)
# print(list1[:num])

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# numbers[::-1]
# print(numbers[1:-1])

# spis = []
# for i in range(26):
#     spis.append(chr(97+i)*(i+1))
# print(spis)

# num = int(input())
# spis = []
# for i in range(num):
#     num2 = int(input())
#     spis.append(num2**3)
# print(spis)

# num = int(input())
# spis = []
# for i in range(1, num+1):
#     if num % i == 0:
#         spis.append(i)
# print(spis)

# num = int(input())
# spis = []
# prev = 0
# for i in range(1, num+1):
#     num2 = int(input())
#     if i != 1:
#         spis.append(num2 + prev)
#     prev = num2
# print(spis)

# spis = []
# num = int(input())
# for i in range(num):
#     num2 = int(input())
#     if i % 2 == 0:
#         spis.append(num2)
# print(spis)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum = 0
# for i in range(len(numbers)):
#     sq = numbers[i] ** 2
#     sum += sq
# print(sum)

# spis = []
# spis2 = []
# num = int(input())
# for i in range(num):
#     x = int(input())
#     spis.append(x)
#     form = x**2 + 2*x + 1
#     spis2.append(form)
# print(*spis, sep = "\n")
# print()
# print(*spis2, sep = "\n")

# spis = []
# num = int(input())
# for i in range(num):
#     num2 = int(input())
#     spis.append(num2)    

# max1 = max(spis)
# index1 = spis.index(max1)
# del spis[index1]

# min1 = min(spis)
# index2 = spis.index(min1)
# del spis[index2]
# print(*spis, sep = "\n")

# spis = []
# num = int(input())
# for i in range(num):
#     text = input()
#     if text in spis:
#         continue
#     spis.append(text)
# print(*spis, sep="\n")

# spis = []
# num = int(input())
# for i in range(num):
#     text = input()
#     spis.append(text)

# search = input().lower()

# for j in range(num):
#     low = spis[j].lower()
#     if search in low:
#         print(spis[j])

# spis = []
# num = int(input())
# for i in range(num):
#     text = input()
#     spis.append(text)

# count = int(input())
# spis2 = []
# spis3 = []
# for j in range(count):
#     text2 = input()
#     spis2.append(text2)
# for k in range(len(spis)):
#     for k2 in range(len(spis2)):
#         lowSpis = spis[k].lower()
#         if (spis2[k2].lower() in lowSpis) and (k2 == 0):
#             spis3.append(spis[k])
#         if len(spis3) == 0:
#             continue
#         if spis2[k2].lower() in spis3[-1].lower():
#             continue
#         else:
#             del spis3[-1]
# print(*spis3, sep="\n")

# spisPlus = []
# spisZero = []
# spisNegat = []
# num = int(input())
# for i in range(num):
#     num2 = int(input())
#     if num2 < 0:
#         spisNegat.append(num2)
#     elif num2 == 0:
#         spisZero.append(num2)
#     elif num2 > 0:
#         spisPlus.append(num2)
# print(*spisNegat, sep = "\n")
# print(*spisZero, sep = "\n")
# print(*spisPlus, sep = "\n")

# text = input()
# word = text.split()
# print(*word, sep="\n")

# text = input()
# spis = []
# words = text.split()
# for i in range(len(words)):
#     current = words[i]
#     fir_leter = current[0]
#     spis.append(fir_leter)
# text2 = '.'.join(spis)
# print(text2)

# text = input()
# word = text.split('\\')
# print(*word, end='', sep='\n')

# text = input()
# words = text.split()
# for i in range(len(words)):
#     int_i = int(words[i])
#     for j in range(int_i):
#         print("+", end='')
#     print()

# flag = True
# ip = input()
# split_dot = ip.split('.')
# for i in range(len(split_dot)):
#     if int(split_dot[i]) <= 255:
#         flag = True
#     else:
#         flag = False
#         break
# if flag == True:
#     print("ДА")
# else:
#     print("НЕТ")

# spis = []
# text = input()
# sep = input()
# for i in range(len(text)):
#     spis.append(text[i])
# text1 = sep.join(spis)
# print(text1)

# counter = 0
# text = input()
# numbers = text.split(' ')
# print(numbers)
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             counter += 1
# print(counter)

# numbers = [8, 9, 10, 11]
# numbers.remove(9)
# numbers.insert(1, 17)
# temp1 = [4, 5, 6]
# numbers.extend(temp1)
# del numbers[0]
# temp2 = numbers.copy()
# numbers.extend(temp2)
# numbers.insert(3, 25)
# print(numbers)

# text = input()
# spis = []
# list_str = text.split(' ')
# for i in range(len(list_str)):
#     spis.append(int(list_str[i]))
# min1 = min(spis)
# max1 = max(spis)
# index_min = spis.index(min1)
# index_max = spis.index(max1)
# spis.insert(index_max, min1)
# del spis[index_max + 1]
# spis.insert(index_min, max1)
# del spis[index_min + 1]
# print(*spis, sep=' ')

# text = input()
# list1 = text.split(' ')
# cnt1 = list1.count('a')
# cnt2 = list1.count('A')
# cnt3 = list1.count('an')
# cnt4 = list1.count('An')
# cnt5 = list1.count('the')
# cnt6 = list1.count('The')
# sum1 = cnt1 + cnt2 + cnt3 + cnt4 + cnt5 + cnt6
# print("Общее количество артиклей:", sum1)

# str = input()
# spis = []
# res_str = str.replace('#', '')
# res_int = int(res_str)
# for i in range(res_int):
#     text = input()
#     ind = text.find("#")
#     if ind == -1:
#         spis.append(text)
#     else:
#         spis.append(text[:ind].rstrip())
# print(*spis, end='', sep='\n')

# str = input()
# res_str = str.split(' ')
# spis = []
# for i in range(len(res_str)):
#     spis.append(int(res_str[i]))
# spis.sort()
# print(*spis, sep=' ')
# spis.sort(reverse = True)
# print(*spis, sep=' ')

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [keywords[1::] for i in range(len(keywords))]

# print(new_keywords)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99, 55, -22, 1, 6]
# n = len(a)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами 

# print('Отсортированный список:', a)

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
# flag = False
# n = len(a)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#     if flag == False:
#         break
# print(a)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)
# for i in range(n):
#     newS = a[:n]
#     max_ind = newS.index(max(newS))
    
#     a[n-1], a[max_ind] = a[max_ind], a[n-1]
#     n -= 1
# print(a)

# 1. Дан список [1, 5, 3, 8, 5, 9, 7]. Выведи на экран наибольшее четное и наибольшее нечетное. Вариант1 - использовать метод maх, вариант2 - не использовать max
# numbers = [1, 5, 3, 8, 5, 9, 7]
# max_chet = []
# max_nechet = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         max_chet.append(numbers[i])
#     else:
#         max_nechet.append(numbers[i])
# print(*max_chet, sep='\n')
# max2 = max(max_nechet)
# print(max2)

# numbers = [2, 5, 3, 8, 5, 9, 7, 6]
# max_chet = 0
# spis_chet = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         spis_chet.append(numbers[i])
#         if spis_chet > max_chet:
#             spis_chet.append(max_chet)
#             print(spis_chet)

# string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
# list1 = []
# counter_a = 0
# ch_a = 'a'
# # list.append(string)
# counter = string.count(' ') +1
# # print('Количество слов:', counter)
# words = string.split()
# for i in range(len(words)):
#     if ch_a in string:
#         counter_a += 1
#     else:
#         print('не найден')
# print(counter_a)
# # a = words.count('a')
# # print(a)

# for j in range(len(words)):
#     w1 = words[j].split()
#     w2 = list(w1[0])
#     # list1.append(w2)
#     for k in range(len(w2)):
#         list1.append(w2[k])
# symb = []
# for l in range(97, 123):
#     symb.append(chr(l))
# print()
# for sym in range(len(symb)):
#     for letter in range(len(list1)):
#         if symb[sym] == list1[letter]:
#             print('Символ', symb[sym])
# text = input()
# text1 = len(text)
# print(text1)

# text = input()
# counter = 0
# list = list(text)
# text1 = len(text)
# print(list)
# for i in range(len(list)):
#     if list[i] == 'a':
#         counter += 1
# print(counter)

# list = ['a', 'a', 'b', 'b', 'c', 'c']
# spis = []
# for i in range(len(list)):
#     if list[i] != 'b':
#         spis.append(list[i])
#     else:
#         print('No')
# print(list)
# print(spis)

# sum1 = 0
# text = input()
# spis = []
# list = list(text)
# for i in range(len(list)):
#     sum1 += int(list[i])
# print(sum1)

# text = input()
# couter = 0
# while text != '0':
#     if text == '1':
#         couter += 1
#     text = input()
# print(couter)

# text = input()
# spis = []
# while text != '0':
#     split = text.split(' ')
#     spis.extend(split)
#     print(len(spis))
#     text = input()

# spis_num = ['1', '2', '3', '4']
# spis_text = ['a', 'b', 'c', 'd']
# spis = []
# spis_rev = spis_text.copy()
# rever1 = spis_rev[::-1]
# for i in range(len(spis_num)):
#     # spis_rev = spis_text.copy()
#     # rever1 = spis_rev[::-1]
#     temp1 = spis_num[i] + rever1[i]
#     # spis_rev = spis_text.copy()
#     # rever1 = spis_rev[::-1]
#     spis.append(temp1)
# print(spis)

# text = input()
# glas = ['a', 'o', 'i']
# while text != '0':
#     if text[0] in glas:
#         print(text[::-1])
#     text = input()

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:-1]
# print(my_list)

# num = int(input())
# spis = []
# for i in range(num + 1):
#     if i % 2 == 0 and i != 0:
#         spis.append(i)
# print(spis)

# num1 = input()
# num2 = input()
# spis1 = num1.split(' ')
# spis2 = num2.split(' ')
# spis3 = []
# for i in range(len(spis1)):
#     sum1 = int(spis1[i]) + int(spis2[i])
#     spis3.append(sum1)
# print(*spis3, sep=' ')

# num = input()
# sum1 = 0
# spis = num.split(' ')
# for i in range(len(spis)):
#     sum1 += int(spis[i])
# print(*spis, sep='+', end='')
# print('=', sum1, sep='')

# num = input()
# flag = True
# spis = num.split('-')
# numbers = '0123456789'
# flag1 = len(spis) == 3 and len(spis[0]) == 3 and len(spis[1]) == 3 and len(spis[2]) == 4
# flag2 = len(spis) == 4 and len(spis[0]) == 1 and len(spis[1]) == 3 and len(spis[2]) == 3 and len(spis[3]) == 4 and spis[0] == '7'
# if flag1 or flag2:
#     for i in range(len(spis)):
#         for j in range(len(spis[i])):
#             if spis[i][j] not in numbers:
#                 flag = False
#                 break
#         if flag == False:
#             break
# else:
#     flag = False
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# text = input()
# counter = 0
# spis = text.split(' ')
# for i in range(len(spis)):
#     if len(spis[i]) > counter:
#         counter = len(spis[i])
# print(counter)

# text = input()
# spis = text.split(' ')
# for i in range(len(spis)):
#     elem = spis[i]
#     ek2 = elem[1:] + elem[0] + 'ки'
#     print(ek2, end = ' ')

# # объявление функции
# def draw_box():
#     for i in range(14):
#         if i == 0 or i == 13:
#             print('*' * 10)
#         else:
#             print('*        *')
# основная программа
# draw_box()  # вызов функции

# def draw_box():
#     for i in range(10):
#         print('*' * (i + 1))
# draw_box()

# def draw_triangle(fill, base):
#     half = base // 2 + 1
#     for i in range(base):
#         if i < half:
#             print(fill * (i + 1))
#         else:
#             print(fill * (base - i))
# fill = input()
# base = int(input())
# draw_triangle(fill, base)



# # объявление функции
# def print_fio(name, surname, patronymic):
#     sym_name = name[0].upper()
#     sym_surname = surname[0].upper()
#     sym_patr = patronymic[0].upper()
#     print(sym_surname, sym_name, sym_patr, sep='')


# # считываем данные
# name, surname, patronymic = input(), input(), input()

# # вызываем функцию
# print_fio(name, surname, patronymic)



# #
#  объявление функции
# def print_digit_sum(num):
#     counter = 0
#     spis = str(num)
#     for i in range(len(spis)):
#         counter += int(spis[i])
#     print(counter)

# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)

# birds = 5000   # глобальная переменная

# def print_texas():
#     global birds
#     birds = 40
#     print('В Техасе обитает', birds, 'птиц.')


# def print_california():
#     print('В Калифорнии обитает', birds, 'птиц.')

# print_texas()

# print_california()

# x = 5
# def add():
#     global x
#     x = 3
#     x = x + 5
#     print(x)

# add()
# print(x)

# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i    
#     return result

# def do_something2(numbers):
#     result = 1
#     for i in range(len(numbers)):
#         result *= i    
#     return result
# # print(do_something([2, 2, 2, 2]))
# print(do_something2([2, 2, 2, 2]))

# # объявление функции
# def get_factors(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     return counter

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))




# # объявление функции
# def find_all(target, symbol):
#     spis = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             spis.append(i)
#     return spis
# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))





# # объявление функции
# def merge(list1, list2):
#     list3 = list1 + list2
#     for i in range(len(list3)):
#         for j in range(i, len(list3)):
#             if list3[i] > list3[j]:
#                 list3[i], list3[j] = list3[j], list3[i]
#     return list3

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))


# def create_spis(num):
#     spis = []
#     for i in range(num):
#         numbers1 = [int(c) for c in input().split()]
#         for el in numbers1:
#             spis.append(el)
#     res = spis.sort()
#     return spis
# num = int(input())
# r = create_spis(num)
# print(r)

# объявление функции
# def is_valid_triangle(a, b, c):
#     if a >= b >= c or a >= c >= b:
#         max = a
#         if max < b + c:
#             return True
#         else:
#             return False
#     if b >= a >= c or b >= c >= a:
#         max = b
#         if max < c + a:
#             return True
#         else:
#             return False
#     if c >= a >= b or c >= b >= a:
#         max = c
#         if max < a + b:
#             return True
#         else:
#             return False

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True



# # считываем данные
# # n = int(input())

# # вызываем функцию
# # print(is_prime(n))

# # объявление функции
# def get_next_prime(num):
#     next_n = num + 1
#     while not is_prime(next_n):
#         next_n += 1
#     return next_n

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))






# # объявление функции
# def is_password_good(password):
#     is_8 = False
#     is_upper = False
#     is_lower = False
#     is_number = False
#     if len(password) >= 8:
#         is_8 = True
#     for i in range(len(password)):
#         if password[i].isupper():
#             is_upper = True
#         if password[i].islower():
#             is_lower = True
#         if password[i].isnumeric():
#             is_number = True
#     if is_8 == True and is_upper == True and is_lower == True and is_number == True:
#         return True
#     else:
#         return False
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))




# # объявление функции
# def is_one_away(word1, word2):
#     counter = 0
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             counter += 1
#     if counter == 1:
#         return True
#     else:
#         return False
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))




# # объявление функции
# def is_palindrome(text):
#     new_string = text.replace(' ', '')
#     new_string = new_string.replace(',', '')
#     new_string = new_string.replace('.', '')
#     new_string = new_string.replace('!', '')
#     new_string = new_string.replace('?', '')
#     new_string = new_string.replace('-', '')
#     half_of_string = len(new_string) / 2
#     for i in range(1, int(half_of_string) + 1):
#         if new_string[i-1].lower() !=  new_string[-i].lower():
#             return False
#     return True
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))




# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def is_palindrome(text):
#     half_of_string = len(text) / 2
#     for i in range(1, int(half_of_string) + 1):
#         if text[i-1] !=  text[-i]:
#             return False
#     return True
# def is_odd(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# def is_valid_password(password):
#     new_password = password.split(':')
#     if len(new_password) > 3:
#         return False
#     is_palindrome1 = is_palindrome(new_password[0])
#     is_prime1 = is_prime(int(new_password[1]))
#     is_odd1 = is_odd(int(new_password[2]))
#     return is_palindrome1 == True and is_odd1 == True and is_prime1 == True 


    

# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))



# # объявление функции
# def is_correct_bracket(text):
#     counter = 0
#     if text[0] == ')':
#         return False
#     for i in range(len(text)):
#         if text[i] == '(':
#             counter += 1
#         else:
#             counter -= 1
#         if counter < 0:
#             return False
#     if counter == 0:
#         return True
#     else:
#         return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))


# объявление функции
# def convert_to_python_case(text):
#     spis = []
#     spis.append(text[0].lower())
#     for i in range(1, len(text)):
#         if text[i] in '0123456789':
#             spis.append(text[i])
#             continue
#         if text[i] == text[i].upper():
#             temp_symbol = '_' + text[i].lower()
#             spis.append(temp_symbol)
#         else:
#             spis.append(text[i])
#     spis = ''.join(spis)
#     return spis

# # считываем данные
# txt = input()

# # вызываем функцию
# print(convert_to_python_case(txt))


# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     res1 = (x1 + x2) / 2
#     res2 = (y1 + y2) / 2
#     return res1, res2

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# # объявление функции
# import math
# def get_circle(radius):
#     c = 2*math.pi*radius
#     s = math.pi*r**2
#     return c, s

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)


# # объявление функции
# from math import *
# def solve(a, b, c):
#     D = b**2 - (4 * a * c)
#     if D > 0:
#         res1 = ((b * -1) + sqrt(D)) / (2 * a)
#         res2 = ((b * -1) - sqrt(D)) / (2 * a)
#         min1 = min(res1, res2)
#         max1 = max(res1, res2)
#         return min1, max1
#     elif D == 0:
#         res3 = ((b * -1) / (2 * a))
#         return res3, res3

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)



# def function_1(symbol):
#     if symbol == '+':
#         print('10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
#     if symbol == '-':
#         print ('1, 2, 3, 4, 5, 6, 7, 8, 9, 10')

# def function_2(symbol):
#     if symbol != '+' and symbol != '-':
#         return 0

#     spis = []
    
#     for i in range(1, 11):
#         spis.append(i)
    
#     if symbol == '-':
#         spis = spis[::-1]
    
    
#     return spis

# symbol = input()
# p = function_2(symbol)
# print(p)



# def before(number):
#     spis1 = []
#     for i in range(0, number + 1):
#         spis1.append(i)
#     return spis1

# def after(number):
#     spis2 = []
#     for i in range(number + 1):
#         spis2.append(i)
#     sp3 = spis2[::-1]
        
#     return sp3
# numer = int(input())
# a = before(numer)
# b = after(numer)
# print(a)
# print(b)



# def reversed_text(text):
#     words = text.split(' ')
#     w1 = words[::-1]
#     w2 = " ".join(w1)
#     return w2

# text = input()
# print(reversed_text(text))


# def reversed_text(text):
#     slash = '/'
#     # if slash[0] == text[0]:
#         # return text
    
#     while text[0] == slash:
#         text = text[1:]

#     if text[0] != slash[0]:
#         return '/' + text     


# text = input()
# print(reversed_text(text))




# def draw_triangle():
#     n = 15
#     centr = n // 2 + 1 
#     for i in range(8):
#         for j in range(1, 16):
#             if j >= centr - i and j <= centr + i: 
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()


# draw_triangle()


# def draw_triangle():
#     n = 15
#     for i in range(1, n +1, 2):
#         print(' ' * ((n - i) // 2) + '*' * i) 

# draw_triangle()



# # объявление функции
# def get_shipping_cost(quantity):
#     counter = 0
#     if quantity == 1:
#         return 1000
#     counter = (quantity - 1) * 120
#     return 1000 + counter

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_shipping_cost(n))

# import math
# # объявление функции
# def compute_binom(n, k):
#     nf = math.factorial(n)
#     nk = math.factorial(k)
#     nkf = math.factorial(n-k)
#     res = nf / (nk * nkf)
#     return int(res)

# # считываем данные
# n = int(input())
# k = int(input())

# # вызываем функцию
# print(compute_binom(n, k))


# объявление функции
# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num > 0 and num <= 10:
#         return list_1[num - 1]
#     if num > 10 and num < 20:
#         a = num // 10
#         b = num % 10
#         return list_11[b - 1]

#     if num > 19:
#         a = num // 10
#         b = num % 10

#         if b == 0:
#             return list_21[a - 2]
#         else:
#             des = list_21[a - 2]
#             ed = list_1[b - 1]
#             return des + " " + ed    
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))



# # объявление функции
# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == 'ru':
#         return lng_ru[number - 1]
#     else:
#         return lng_en[number - 1]

# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))


# # объявление функции
# def is_magic(date):
#     list1 = date.split('.')
#     number1 = int(list1[0]) 
#     number2 = int(list1[1])
#     number3 = int(list1[2])
#     mult = number1 * number2
#     test1 = int(list1[2][2:])
#     if mult == test1:
#         return True
#     else:
#         return False

# # считываем данные
# date = input()

# # вызываем функцию
# print(is_magic(date))


# # объявление функции
# def is_pangram(text):
#     spis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     text1 = text.replace(' ', '').lower()
#     for i in range(len(text1)):
#         if text1[i] not in spis:
#             continue
#         else:
#             spis.remove(text1[i])
        
#     if len(spis) == 0:
#         return True
#     else:
#             return False
# # считываем данные
# text = input()

# # вызываем функцию
# print(is_pangram(text))

# import random
# def random_num():
#     num = int(input())
#     rand1 = random.randint(1, num)
#     left = 1
#     counter = 0
#     right = num
#     middle = (left + right) // 2 
#     # while rand1 != middle:
#     while True:
#         counter += 1
#         if middle < rand1:
#             left = middle + 1
#             if left == rand1:
#                 break
#             # middle = (left + right) // 2

#         if middle > rand1:
#             right = middle - 1
#             if right == rand1:
#                 break
#             # middle = (left + right) // 2
#     return counter

# print(random_num())


# import random
# def is_valid(n1):
#     if n1 > 0 and n1 <= 100:
#         return True
#     else:
#         return False


# print('Добро пожаловать в числовую угадайку')
# # number = int(input())


# def game1():
#     num1 = int(input('Введите правое число:'))
#     ran1 = random.randint(1, num1)
#     print("comp:",ran1)
#     counter = 1
#     while True:
#         number = int(input())
#         if is_valid(number):
#             if number < ran1:
#                 print('Ваше число меньше загаданного, попробуйте еще разок')
#                 counter += 1
#             elif number > ran1:
#                 print('Ваше число больше загаданного, попробуйте еще разок')
#                 counter += 1
#             else:
#                 print('Вы угадали, поздравляем!')
#                 print('Ваше число попыток равно:', counter)
#                 break
#         else:
#             print('А может быть все-таки введем целое число от 1 до 100?')

# while True:
#     game1()
#     text1 = input("завершить игру?")
#     if text1 == 'Да':
#         break
# print("Спасибо, что играли в числовую угадайку. Еще увидимся...")




#Задача 1 Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in range(len(a)):
#     if a[i] < 5:
#         b.append(a[i])
# print(b)

#Задача 2 Нужно вернуть список, который состоит из элементов, общих для этих двух списков. (50/50)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# spis = []
# a.sort()
# b.sort()
# for i in range(len(b)):
#     if a[i] == b[i]:
#         spis.append(a[i])
#     else:
#         continue
# print(spis)

#Задача 6 Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
# number = 100
# print(str(number))

# Задача 7 Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
# number = int(input())
# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(row)
#         row = [sum(x) for x in zip([0]+row, row+[0])]
        
# PrintPasTriangle(number)

# Задача 8 Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
# def is_palindrome(text):
#     new_string = text.replace(' ', '')
#     new_string = new_string.replace(',', '')
#     new_string = new_string.replace('.', '')
#     new_string = new_string.replace('!', '')
#     new_string = new_string.replace('?', '')
#     new_string = new_string.replace('-', '')
#     half_of_string = len(new_string) / 2
#     for i in range(1, int(half_of_string) + 1):
#         if new_string[i-1].lower() !=  new_string[-i].lower():
#             return 'Эта строка не палиндром'
#     return 'Эта строка является палиндромом'
# txt = input()

# print(is_palindrome(txt))

# Задача 9 Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# insh = int(input())
# second = 0
# minutes = 0
# hours = 0
# days = 0
# for i in range(1, insh+1):
#     if i >= 60:
#         # minutes += 1
#         if i == 61:
#             second = 0
#         else:
#             minutes += 1
#     if minutes >= 60:
#         # hours += 1
#         if minutes == 61:
#             minutes = 0
#         else:
#             hours += 1
#     if hours >= 24:
#         # days += 1
#         if hours == 25:
#             hours = 0
#         else:
#             days += 1
# print(days,':', hours,':', minutes,':', second)



# import random
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# name = input()
# print('Привет', name)
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
#            "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#            "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
#            "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
# def choice(answers):
#     random_answer = random.randint(0, len(answers))
#     return answers[random_answer]
# while True:
#     question = input('Задайте вопрос: ')
#     print(choice(answers))
#     text1 = input('Хотите завершить ?')
#     if text1 == 'Да' or text1 == 'да':
#         break
# print('Возвращайся если возникнут вопросы!')



# import random
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_.'
# chars = ''
# value_pass = int(input('Количество паролей для генерации: '))
# len_pass = int(input('Длину одного пароля: '))
# ans_number = input('Включать ли цифры 0123456789: ')
# if ans_number == 'да':
#     chars += digits
# ans_upperSym = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ: ')
# if ans_upperSym == 'да':
#     chars += uppercase_letters
# ans_lowerSym = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz: ')
# if ans_lowerSym == 'да':
#     chars += lowercase_letters
# ans_symbols = input('Включать ли символы !#$%&*+-=?@^_: ')
# if ans_symbols == 'да':
#     chars += punctuation
# def generate_password(length, chars):
#     srt1 = ''
#     for i in range(length):
#         ran_num = random.randint(0, len(chars) - 1)
#         srt1 += chars[ran_num]
#     print(srt1)


# for i in range(value_pass):
#     generate_password(len_pass, chars)




# # num = int(input())
# text = input()

# def rus_letters_codding(num, text):
#     for i in range(len(text)):
#         ord1 = ord(text[i])
#         ord1 = ord1 + num
#         raznic = 0
#         if ord(text[i]) == 44 or ord(text[i]) == 32 or ord(text[i]) == 33:
#             print(text[i], end='')
#             continue
#         if ord1 > 1103:
#             raznic = ord1 - 1103
#             ord1 = 1040 + raznic - 1
#             print(chr(ord1), end='')
#         else:
#             print(chr(ord1), end='')
# # rus_letters(num, text)

# def eng_letters(num, text):
#     res = ''
#     for i in range(len(text)):
#         ord1 = ord(text[i])
#         ord1 = ord1 + num
#         raznic = 0
#         if ord(text[i]) == 44 or ord(text[i]) == 32 or ord(text[i]) == 33:
#             print(text[i], end='')
#             continue
#         if text[i].isupper():
#             if ord1 > 90:
#                 raznic = ord1 - 90
#                 ord1 = 65 + raznic - 1
#                 res += chr(ord1)
#             else:
#                 res += chr(ord1)
#         else:
#             if ord1 > 122:
#                 raznic = ord1 - 122
#                 ord1 = 97 + raznic - 1
#                 res+= chr(ord1)
#             else:
#                 res+= chr(ord1)
#     return res
# # eng_letters(num, text)

# def rus_letters_decodding(num, text):
#     for i in range(len(text)):
#         ord1 = ord(text[i])
#         ord1 = ord1 - num
#         raznic = 0
#         if ord(text[i]) == 44 or ord(text[i]) == 32 or ord(text[i]) == 33 or ord(text[i]) == 46:
#             print(text[i], end='')
#             continue
#         if text[i].isupper():
#             if ord1 < 1040:
#                 raznic = 1040 - ord1
#                 ord1 = 1103 - raznic + 1
#                 print(chr(ord1).upper(), end='')
#             else:
#                 print(chr(ord1).upper(), end='')
#         else:
#             if ord1 < 1040:
#                 raznic = 1040 - ord1
#                 ord1 = 1103 - raznic + 1
#                 print(chr(ord1).lower(), end='')
#             else:
#                 print(chr(ord1).lower(), end='')       
# # rus_letters_decodding(num, text)

# def eng_letters_decode(num, text):
#     for i in range(len(text)):
#         ord1 = ord(text[i])
#         ord1 = ord1 - num
#         raznic = 0
#         if ord(text[i]) == 44 or ord(text[i]) == 32 or ord(text[i]) == 33 or ord(text[i]) == 46:
#             print(text[i], end='')
#             continue
#         if text[i].isupper():
#             if ord1 < 65:
#                 raznic = 90 - ord1
#                 ord1 = 90 - raznic + 1
#                 print(chr(ord1).upper(), end='')
#             else:
#                 print(chr(ord1).upper(), end='')
#         else:
#             if ord1 < 97:
#                 raznic = 122 - ord1
#                 ord1 = 122 - raznic + 1
#                 print(chr(ord1).lower(), end='')
#             else:
#                 print(chr(ord1).lower(), end='')
# # eng_letters_decode(num, text)


# # for i in range(0, 10):
# #     rus_letters_decodding(i, text)
# #     print()

# # eng_letters(num, text)
# spis = text.split(' ')
# spec_symb = [',', '.', '"', '!']
# for i in range(len(spis)):
#     temp_text = ''
#     temp_symb_end = ''
#     temp_symb_start = ''
#     for j in range(len(spis[i])):
#         if spis[i][j] in spec_symb:
#             if j == 0:
#                 temp_symb_start = spis[i][j]
#             else:
#                 temp_symb_end = spis[i][j]
#         else:
#             temp_text += spis[i][j]
#     res = eng_letters(len(temp_text), temp_text)
#     res = temp_symb_start + res + temp_symb_end + ' '
#     print(res, end='')
#     # print(temp_symb)

# num = int(input())
# def translate_num(num, letter):
#     if letter == 'b':
#         bin1 = bin(num)
#         return bin1
#     if letter == 'o':
#         oct1 = oct(num)
#         return oct1
#     if letter == 'h':
#         hex1 = hex(num)
#         return hex1

# print(translate_num(num, 'b')[2:])
# print(translate_num(num, 'o')[2:])
# print(translate_num(num, 'h')[2:].upper())



# import random
# word_list = ['Человек', 'Сова', 'Кошка', 'Собака', 'Торт', 'Печенье']

# def play(word):
    
#     word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
#     guessed = False                    # сигнальная метка
#     guessed_letters = []               # список уже названных букв
#     guessed_words = []                 # список уже названных слов
#     tries = 6                          # количество попыток
    
#     print('Давайте играть в угадайку слов!')
#     display_hangman(tries)
#     print(word_completion)
    
# def get_word():
#     return random.choice(word_list).upper()

# def display_hangman(tries):
#     stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     / \\
#                    -
#                 ''',
#                 # голова, торс, обе руки, одна нога
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |     /
#                    -
#                 ''',
#                 # голова, торс, обе руки
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|/
#                    |      |
#                    |      
#                    -
#                 ''',
#                 # голова, торс и одна рука
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |     \\|
#                    |      |
#                    |     
#                    -
#                 ''',
#                 # голова и торс
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |      |
#                    |      |
#                    |     
#                    -
#                 ''',
#                 # голова
#                 '''
#                    --------
#                    |      |
#                    |      O
#                    |    
#                    |      
#                    |     
#                    -
#                 ''',
#                 # начальное состояние
#                 '''
#                    --------
#                    |      |
#                    |      
#                    |    
#                    |      
#                    |     
#                    -
#                 '''
#     ]
#     return stages[tries]


# def is_valid(g):
#         if g.isalpha() == True:
#             return True
#         else:
#             return False


# def play(word):
    
#     word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
#     guessed = False                    # сигнальная метка
#     guessed_letters = []               # список уже названных букв
#     guessed_words = []                 # список уже названных слов
#     tries = 6                          # количество попыток
    
#     print('Давайте играть в угадайку слов!')
#     display_hangman(tries)
#     print(word_completion)
    
#     while True:
#         guess = input('Ответ: ').upper()
#         if is_valid(guess) == False:
#             print('Ответ принимается только русскими буквами')
#             continue
        
#         elif is_valid(guess) == True:  # валидация
#             check = word.find(guess)
            
#             if guess in word_completion:
#                 print('Вы уже угадали эту букву. Попробуйте что-то еще')
#                 continue
                        
#             if guess == word:  # если угадал сразу слово
#                 print('Поздравляем, вы угадали слово! Вы победили!')
#                 break
            
#             if check == -1:  # неверная попытка
#                 print('Неправильно')
#                 tries -= 1
#                 print(display_hangman(tries))
#             else:
#                 if len(guess) == 1:
#                     for i in range(len(word_completion)):  # правильная буква
#                         if word[i] == guess:
#                             word_completion = word_completion[:i] + guess + word_completion[i + 1:]
#                     print(word_completion)
#                 elif len(guess) > 1:
#                     print('Ответ принимается в виде 1 буквы либо слова целиком')
#                     continue
                        
#             if word_completion == word:
#                 print('Поздравляем, вы угадали слово! Вы победили!')
#                 break
            
#             if tries == 0:
#                 print('Вы проиграли. Правильный ответ был:', word)
#                 break

# def play_again():
#     print('Сыграем еще раз?')
#     flag = ''
#     while flag != 'stop':
#         answer = input()
#         if answer.isalpha() == True and answer.lower() == 'да':
#             flag == 'stop'
#             return True
            
#         elif answer.isalpha() == True and answer.lower() == 'нет':
#             flag == 'stop'
#             return False
#         else:
#             print('Ответ принимает только да/нет')
            
# while True:
#     word = get_word()
#     play(word)                 
    
#     if play_again() == True:
#         continue
#     else:
#         print('Спасибо, что играли . Еще увидимся!')
#         break

# import math
# a = int(input())
# b = int(input())
# sum = a + b
# raz = a - b
# proiz = a * b
# chas = a / b
# celChas = a // b
# ostChas = a % b
# c = (a ** 10) + (b ** 10)
# sqrt1 = math.sqrt(c)
# print(sum)
# print(raz)
# print(proiz)
# print(chas)
# print(celChas)
# print(ostChas)
# print(sqrt1)



# Индекс массы тела
# weight = float(input())
# size = float(input())
# imt = weight / (size * size)
# if imt >= 18.5 and imt <= 25:
#     print('Оптимальная масса')
# elif imt < 18.5:
#     print('Недостаточная масса')
# else:
#     print('Избыточная масса')

# Стоимость строки
# text = input()
# len_text = len(text) * 60
# rub = len_text // 100
# cop = len_text % 100
# print(rub, 'р.', cop, 'коп.')

# Количество слов
# text = input()
# split1 = text.split(' ')
# new_list = [x for x in split1 if x != '']
# print(len(new_list))

# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# year = int(input())
# year2 = year % 12
# print(animals[year2])

# num = input()
# if len(num) == 5:
#     num1 = num[::-1]
#     print(int(num1))
# else:
#     num1 = num[1:]
#     num2 = num1[::-1]
#     num3 = num[0] + num2
#     print(int(num3))


# num = int(input())
# counter = 0
# spis = []
# while num > 0:
#     num1 = num % 10
#     num = num // 10
#     counter += 1
#     spis.append(num1)
#     if counter == 3:
#         spis.append(',')
#         counter = 0
# inv = spis[::-1]
# if inv[0] == ',':
#     del inv[0]
# print(*inv, end='\n', sep='')

# numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
# res = 0
# for num in numbers:
#     res += (num % 2 == 1) and (num > 1) 
# print(res)





# # объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False

# # считываем данные
# num1, num2 = int(input()), int(input())

# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')





# range1 = int(input())
# def quarter(x, y):
#     if x > 0 and y > 0:
#         return 1
#     if x < 0 and y > 0:
#         return 2
#     if x < 0 and y < 0:
#         return 3
#     if x > 0 and y < 0:
#         return 4
            


# counter1 = 0
# counter2 = 0
# counter3 = 0
# counter4 = 0

# for i in range(range1):
#     coord = input() 
#     a = coord.split(" ")
#     x = int(a[0])
#     y = int(a[1])
    
#     if quarter(x, y) == 1:
#         counter1 += 1
#     if quarter(x, y) == 2:
#         counter2 += 1
#     if quarter(x, y) == 3:
#         counter3 += 1
#     if quarter(x, y) == 4:
#         counter4 += 1

# print('Первая четверть:', counter1)
# print('Вторая четверть:', counter2)
# print('Третья четверть:', counter3)
# print('Четвертая четверть:', counter4)



# numbers = input()
# a = numbers.split(' ')
# tek = 0
# counter = 0
# for i in range(len(a)):
#     if i == 0:
#         tek = a[i]
#         continue
#     if int(a[i]) > int(tek):
#         counter += 1
#     tek = a[i]

# print(counter)


# numbers = input()
# list1 = numbers.split(' ')
# for i in range(0, len(list1)-1, 2):
#     list1[i], list1[i+1] = list1[i+1], list1[i]
# print(*list1, end='\n')

# numbers = input()
# list1 = numbers.split(' ')
# last = list1[-1:]
# print(*last + list1[:-1], end='\n')


#numbers = input()
# spis = numbers.split(' ')
# for i in range(len(spis)):



# numbers = input()
# a = numbers.split(' ')
# tek = 0
# counter = 1
# for i in range(len(a)):
#     if i == 0:
#         tek = a[i]
#         continue
#     if int(a[i]) > int(tek):
#         counter += 1
#     tek = a[i]
# print(counter)


# Timur = input()
# Ruslan = input()
# if Timur == 'камень' and Ruslan == 'ножницы':
#     print('Тимур')
# if Timur == 'ножницы' and Ruslan == 'бумага':
#     print('Тимур')
# if Timur == 'бумага' and Ruslan == 'камень':
#     print('Тимур')

# if Ruslan == 'камень' and Timur == 'ножницы':
#     print('Руслан')
# if Ruslan == 'ножницы' and Timur == 'бумага':
#     print('Руслан')
# if Ruslan == 'бумага' and Timur == 'камень':
#     print('Руслан')

# if Timur == 'камень' and Ruslan == 'камень':
#     print('ничья')
# if Timur == 'ножницы' and Ruslan == 'ножницы':
#     print('ничья')
# if Timur == 'бумага' and Ruslan == 'бумага':
#     print('ничья')


# list1 = [[1, 7, 8], 
#          [9, 7, 102], 
#          [6, 106, 105], 
#          [100, 99, 98, 103], 
#          [1, 2, 3]
#          ]
# maximum = -1
# for i in range(len(list1)):
#     temp1 = max(list1[i])
#     if maximum > temp1:
#         continue
#     maximum = temp1 
# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in range(len(list1)):
#     list1[i].reverse()
# print(list1)



# n = 3
# list1 = []

# for _ in range(n):
#     row = input().split()
#     list1.extend(row)

# print(list1)


# number = int(input())
# for i in range(number):
#     spis = []
#     for j in range(number):
#         spis.append(j + 1)
#     print(spis)


# number = int(input())
# for i in range(1, number + 1):
#     spis = []
#     for j in range(i):
#         spis.append(j + 1)
#     print(spis)


# letters = input()
# spis = letters.split()
# res = []
# for i in range(len(spis)):
#     spis_temp = []
#     spis_temp.append(spis[i])
#     if i == 0:
#         res.append(spis_temp)
#         continue  
#     if spis[i-1] == spis[i]:
#         res[-1].append(spis[i])
#     else:
#         res.append(spis_temp)
# print(res)



# number = int(input())
# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(*row, end='\n')
#         row = [sum(x) for x in zip([0]+row, row+[0])]
        
# PrintPasTriangle(number)



# n = 5
# a = [[19, 21, 33, 78, 99], 
#      [41, 53, 66, 98, 76], 
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]

# maximum = -1
# minimum = 100

# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)


# n = int(input())
# m = int(input())
# spis = list([])
# def inpput(n, m):
#     for i in range(n):
#         spis.append([])
#         for j in range(m):
#             spis[i].append(input())
# inpput(n,m)
# def output1(n, m):
#     for i in range(n):
#         for j in range(m):
#             print(spis[i][j], end=' ')
#         print()
# output1(n,m)



# n = int(input())
# m = int(input())
# matrix = [[0]*m for _ in range(n)]
# matrix2 = [[0]*n for _ in range(m)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = input()
#         matrix2[j][i] = matrix[i][j]
# def output1(n, m, spis):
#     for i in range(n):
#         for j in range(m):
#             print(spis[i][j], end=' ')
#         print()
# output1(n,m,matrix)
# print()
# output1(m,n,matrix2)

# n = int(input())
# matrix = [[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         matrix[i][j] = input()
# print(matrix)



# range1 = int(input())
# spis = []
# counter = 0
# for i in range(range1):
#     str_number = input().split(' ')
#     spis.append(str_number)
# for j in range(range1):
#     counter += int(spis[j][j])
# print(counter)



# range1 = int(input())
# spis = []
# for i in range(range1):
#     str_number = input().split(' ')
#     temp_spis = []
#     for k in range(len(str_number)):
#         temp_spis.append(int(str_number[k]))
#     spis.append(temp_spis)
# for j in range(range1):
#     counter = 0
#     sumator = sum(spis[j])
#     arefm = sumator / len(spis[j])
#     for l in range(len(spis[j])):
#         if spis[j][l] > arefm:
#             counter += 1
#     print(counter)




# range1 = int(input())
# spis = []
# for i in range(range1):
#     str_number = input().split(' ')
#     temp_spis = []
#     for k in range(len(str_number)):
#         temp_spis.append(int(str_number[k]))
#     spis.append(temp_spis)
# max1 = spis[0][0]
# for i in range(range1):
#     for j in range(i+1):
#         if spis[i][j] > max1:
#             max1 = spis[i][j]
# print(max1)



# range1 = int(input())
# spis = []
# for i in range(range1):
#     str_number = input().split(' ')
#     temp_spis = []
#     for j in range(len(str_number)):
#         temp_spis.append(int(str_number[j]))
#     spis.append(temp_spis)
# max1 = spis[0][0]
# for i in range(range1):
#     for j in range(range1):
#         if i >= j and i < len(spis) - j:
#             # print(spis[i][j])
#             if spis[i][j] > max1:
#                 max1 = spis[i][j]
#         if i <= j and i >= len(spis) - 1 - j:
#             # print(spis[i][j], '*')
#             if spis[i][j] > max1:
#                 max1 = spis[i][j]
# print(max1)



# range1 = int(input())
# spis = []
# sum_up = 0
# sum_down = 0
# sum_left = 0
# sum_right = 0
# for i in range(range1):
#     str_number = input().split(' ')
#     temp_spis = []
#     for j in range(len(str_number)):
#         temp_spis.append(int(str_number[j]))
#     spis.append(temp_spis)
# for i in range(range1):
#     for j in range(range1):
#         if i > j and i < len(spis) - 1 - j:
#             # print(spis[i][j])
#             sum_left += spis[i][j]
#         if i < j and i > len(spis) - 1 - j:
#             # print(spis[i][j], '*')
#             sum_right += spis[i][j]
#         if i < j and i < len(spis) - 1 - j:
#             # print(spis[i][j])
#             sum_up += spis[i][j]
#         if i > j and i > len(spis) - 1 - j:
#             # print(spis[i][j], '*')
#             sum_down += spis[i][j]
# print('Верхняя четверть:', sum_up)
# print('Правая четверть:',sum_right)
# print('Нижняя четверть:', sum_down)
# print('Левая четверть:',sum_left)


# n = int(input())
# m = int(input())
# matrix = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * j
#         matrix[i][j] = str(matrix[i][j])
#     myString = '  '.join(matrix[i])
#     print(myString)



# n = int(input())
# m = int(input())
# strok = 0
# stolb = 0
# spis = []
# for i in range(n):
#     str_number = input().split(' ')
#     temp_spis = []
#     for j in range(m):
#         temp_spis.append(int(str_number[j]))
#     spis.append(temp_spis)

# for i in range(n):
#     for j in range(m):
#         if spis[i][j] > spis[strok][stolb]:
#             strok, stolb = i, j
# print(strok, stolb)




# n = int(input())
# m = int(input())
# strok = 0
# stolb = 0
# spis = []
# for i in range(n):
#     str_number = input().split(' ')
#     temp_spis = []
#     for j in range(m):
#         temp_spis.append(int(str_number[j]))
#     spis.append(temp_spis)
# number = input().split(' ')
# number[0] = int(number[0])
# number[1] = int(number[1])
# for i in range(n):
#     for j in range(m):
#         if j == number[0]:
#             spis[i][number[1]], spis[i][number[0]] = spis[i][number[0]], spis[i][number[1]]
# def output1(n, m, spis):
#     for i in range(n):
#         for j in range(m):
#             print(spis[i][j], end=' ')
#         print()
# output1(n, m, spis)



# n = int(input())
# spis = []
# for i in range(n):
#     str_number = input().split(' ')
#     temp_spis = []
#     for j in range(n):
#         temp_spis.append(int(str_number[j]))
#     spis.append(temp_spis)
# flag = True
# for i in range(n):
#     for j in range(n):
#         if spis[i][j] != spis[j][i]:
#             flag = False
#             break
        
# if flag:
#     print('YES')
# else:
#     print('NO')

# temp_str = input().split(' ')
# n = int(temp_str[0])
# m = int(temp_str[1])

# def matrix_input(n, m):
#     spis = []
#     for i in range(n):
#         str_number = input().split(' ')
#         temp_spis = []
#         for j in range(m):
#             temp_spis.append(int(str_number[j]))
#         spis.append(temp_spis)
#     return spis

# m1 = matrix_input(n, m)
# input()
# m2 = matrix_input(n, m)

# def matrix_sum(m1, m2, n, m):
#     m_sum = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             m_sum[i][j] = m1[i][j] + m2[i][j]
#     return m_sum

# def output1(n, m, spis):
#     for i in range(n):
#         for j in range(m):
#             print(spis[i][j], end=' ')
#         print()

# m_res = matrix_sum(m1, m2, n, m)
# output1(n, m, m_res)




# def matrix_input():
#     temp_str = input().split(' ')
#     n = int(temp_str[0])
#     m = int(temp_str[1])
#     spis = []
#     for i in range(n):
#         str_number = input().split(' ')
#         temp_spis = []
#         for j in range(m):
#             temp_spis.append(int(str_number[j]))
#         spis.append(temp_spis)
#     return spis

# m1 = matrix_input()
# input()
# m2 = matrix_input()

# def matrix_mult(m1, m2, n, m):
#     m_sum = [[0]*m for _ in range(m)]

#     for i in range(m):
#         for j in range(m):
#             for k in range(n):
#                 m_sum[i][j] += (m1[i][k] * m2[k][j])
#     return m_sum

# def output1(n, m, spis):
#     for i in range(n):
#         for j in range(m):
#             print(spis[i][j], end=' ')
#         print()
# n = len(m1[0])
# m = len(m2[0])
# m_res = matrix_mult(m1, m2, n, m)
# output1(m, m, m_res)


# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()] 
# non_empty_tuples = [i for i in tuples if len(i) > 0]
# print(non_empty_tuples)

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# counter = 1
# for i in range(len(numbers)):
#     counter *= numbers[i]
# print(counter)


# data = 'Python для продвинутых!'
# tpl = tuple(data)
# print(tpl)


# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = list(poet_data)
# poet_data[2] = 'Москва'
# poet_data = tuple(poet_data)
# print(poet_data)


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# spis = []
# for i in range(len(numbers)):
#     sumator1 = sum(numbers[i])
#     spis.append(sumator1 / len(numbers[i]))
# print(spis)



# a = int(input())
# b = int(input())
# c = int(input())
# x = -(b/(2*a))
# y = ((4*a*c)-(b**2)) / (4*a)
# cort = (x,y)
# print(cort)


# n = int(input())
# a = 1
# b = 1
# c = 1
# spis = []
# for i in range(n):
#     print(a, end=' ')
#     a, b, c = b, c, a + b + c
# print(1, 1, *spis[:-2])



# text1 = input()
# text2 = input()
# temp1 = set('0123456789')
# text3 = text1 + text2
# mn = set(text3)
# if mn == temp1:
#     print('YES')
# else:
#     print('NO')


# text = input().split()
# mn1, mn2, mn3 = text[0], text[1], text[2]
# temp1,temp2,temp3 = set(mn1),set(mn2),set(mn3)
# if temp1 == temp2 and temp2 == temp3:
#     print('YES')
# else:
#     print('NO')


# myset = set('python')

# item = myset.pop()
# print(item, len(myset))

# temp2 = int(input())
# spis = []
# sting1 = ''
# def sybmol1(text):
#     text_lower = text.lower()
#     mnoge = set(text_lower)
#     return len(mnoge)

# for i in range(temp2):
#     text = input()
#     sting1 += text
# temp1 = sybmol1(sting1)
# print(temp1)


# text = input().lower()
# ignore = '.,;:-?!'
# new_string = ''

# for i in range(len(text)):
#     if text[i] not in ignore:
#         new_string += text[i]
# spis = new_string.split(' ')
# mnoge = set(spis)
# print(len(mnoge))



# string_of_numbers = input()
# mnoge = set()
# spis = string_of_numbers.split()
# for i in range(len(spis)):
#     el = int(spis[i])
#     if el in mnoge:
#         print('YES')
#     else:
#         mnoge.add(el)
#         print('NO')


# set1 = {'a', 'b', 'c', 'd', 'h'}
# set2 = {'b', 'd', 'f', 'h'}

# set3 = set1 - set2 & set1
# print()



# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     mnoge = set(spis1)

#     return mnoge

# def intersection_numbers(mnoge1, mnoge2):
#     myset3 = mnoge1.intersection(mnoge2)
#     return len(myset3)

# mnoge1 = create_mnoge()
# mnoge2 = create_mnoge()

# res = intersection_numbers(mnoge1, mnoge2)
# print(res)


# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# def intersection_numbers(mnoge1, mnoge2):
#     myset3 = mnoge1.intersection(mnoge2)
#     return myset3

# mnoge1 = create_mnoge()
# mnoge2 = create_mnoge()

# intersection1 = intersection_numbers(mnoge1, mnoge2)
# sorted_intersection = sorted(intersection1)

# print(*sorted_intersection, sep=' ')



# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# def difference_numbers(mnoge1, mnoge2):
#     myset3 = mnoge1.difference(mnoge2)
#     return myset3

# mnoge1 = create_mnoge()
# mnoge2 = create_mnoge()

# difference1 = difference_numbers(mnoge1, mnoge2)
# sorted_difference = sorted(difference1)

# print(*sorted_difference, sep=' ')



# range1 = int(input())
# spis = []
# def create_mnoge():
#     numbers = input()
#     spis3 = []
#     for i in range(len(numbers)):
#         integer = int(numbers[i])
#         spis3.append(integer)
    
#     spis2 = []
#     for i in range(len(spis3)):
#         spis2.append(int(spis3[i]))

#     mnoge = set(spis2)
#     return mnoge
# for i in range(range1):
#     temp1 = create_mnoge()
#     spis.append(temp1)
# res_mnoge = set(spis[0])
# for i in range(1, len(spis)):
#     temp2 = spis[i].intersection(res_mnoge)
#     res_mnoge = temp2
# print(*sorted(res_mnoge))


# num1 = input()
# num2 = input()
# set1 = set(num1)
# set2 = set(num2)
# if set1.isdisjoint(set2):
#     print('NO')
# else:
#     print('YES')


# num1 = input()
# num2 = input()
# set1 = set(num1)
# set2 = set(num2)
# if set2.issubset(set1):
#     print('YES')
# else:
#     print('NO')


# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# set1 = create_mnoge()
# set2 = create_mnoge()
# set3 = create_mnoge()
# res_set = set1 & set2
# if set3 not in set1 and set3 not in set2:
#     res = res_set - set3
#     print(*sorted(res ,reverse=True ), end='\n') 


# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# set1 = create_mnoge()
# set2 = create_mnoge()
# set3 = create_mnoge()
# spis = []
# union_set = set1 | set2 | set3
# intersection_set = set1 & set2 & set3
# res = sorted(union_set.difference(intersection_set))
# if union_set.difference(intersection_set):
#     print(*res,end='\n')



# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# set1 = create_mnoge()
# set2 = create_mnoge()
# set3 = create_mnoge()
# spis = []
# union_set = set1 | set2
# intersection_set = set3 - union_set
# res = sorted(intersection_set, reverse=True)
# print(*res, end='\n')


# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# set1 = create_mnoge()
# set2 = create_mnoge()
# set3 = create_mnoge()
# numbers = {0,1,2,3,4,5,6,7,8,9,10}
# union_set = set1 | set2 | set3
# print(*sorted(numbers.difference(union_set)), end='\n')

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {i[0].lower() for i in words}
# print(*sorted(myset))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# new_string = ''
# ignore = ".,!:;()'"
# for i in range(len(sentence)):
#     if sentence[i] not in ignore:
#         new_string += sentence[i]

# sentence2 = new_string.split()

# myset = {i.lower() for i in sentence2 if len(i) < 4}
# print(*sorted(myset))




# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# png = '.png'
# myset = {i.lower() for i in files}
# myset2 = {i for i in myset if png in i}
# print(*sorted(myset2))


# n = int(input())
# m = int(input())
# k = int(input())
# p = int(input())

# sobaka = n - m
# svet = n - k
# oba = (sobaka + svet) - n
# print(oba + p)


# numbers = input()
# spis = numbers.split()
# len_spis = len(spis)
# mnoge = set(spis)
# len_mnoge = len(mnoge)
# res = len_spis - len_mnoge
# print(res)

# range1 = int(input())
# spis = []
# for i in range(range1 + 1):
#     text = input()
#     spis.append(text)
# mnoge = set(spis)
# res = len(spis) - len(mnoge)
# if res == 0:
#     print('OK')
# else:
#     print("REPEAT") 



# range1 = int(input())
# range2 = int(input())
# spis1 = []
# for i in range(range1):
#     text = input()
#     spis1.append(text)
# spis_res = []
# for i in range(range2):
#     text = input()
#     if text in spis1:
#         spis_res.append('YES')
#     else:
#         spis_res.append('NO')
# for i in range(len(spis_res)):
#     print(spis_res[i])



# def create_mnoge():
#     numbers = input()
#     spis1 = numbers.split()
#     spis2 = []
#     for i in range(len(spis1)):
#         spis2.append(int(spis1[i]))
#     mnoge = set(spis2)
#     return mnoge

# set1 = create_mnoge()
# set2 = create_mnoge()
# set3 = set1.intersection(set2)
# if not set3:
#     print('BAD DAY')
# else:
#     print(*sorted(set3, reverse = True))


# numbers1 = input().split()
# numbers2 = input().split()

# set1 = set(numbers1)
# set2 = set(numbers2)

# res = set1.issubset(set2)
# if res == True and len(set2) <= len(set1):
#     print('YES')
# else:
#     print('NO')



# range1 = int(input())
# range2 = int(input())
# spis1 = []
# spis2 = []
# for i in range(range1):
#     text = input()
#     spis1.append(text)

# for i in range(range2):
#     text = input()
#     spis2.append(text)

# mnoge1 = set(spis1)
# mnoge2 = set(spis2)
# res1 = mnoge1.difference(mnoge2)
# res2 = mnoge2.difference(mnoge1)
# res = len(res1) + len(res2)
# if res == 0:
#     print('NO')
# else:
#     print(res)



# numbers1 = input().split()
# numbers2 = input().split()

# set1 = set(numbers1)
# set2 = set(numbers2)

# res = set1.union(set2)
# print(*sorted(res))


# range1 = int(input())
# range2 = int(input())
# spis1 = []
# spis2 = []
# for i in range(range1):
#     text = input()
#     spis1.append(text)

# for i in range(range2):
#     text = input()
#     spis2.append(text)

# mnoge1 = set(spis1)
# mnoge2 = set(spis2)
# res = mnoge1.symmetric_difference(mnoge2)
# if len(res) == 0:
#     print('NO')
# else:
#     print(len(res))


# n, m = int(input()), int(input())
# n += m
# s1, s2 = set(), set()
# for i in range(n):
#     student = (input())
#     if student in s1:
#         s1.remove(student)
#         s2.add(student) 
#     else:
#         s1.add(student)
# if len(s1) <= 0:
#     print('NO')
# else:
#     print(len(s1))


# n = int(input())
# lst = [set(input() for _ in range(int(input()))) for _ in range(n)]
# res = lst[0]
# for i in lst:
#     res = res.intersection(i)
# print(*sorted(res),sep = '\n')


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# print(*sorted( [ i['name'] for i in users if i.get('email', '') == '' ] ))


# slov = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# number = input()
# for i in range(len(number)):
#     temp1 = number[i]
#     print(slov[temp1], end = ' ')



# string1 = input()
# slov = {
#     'CS101': {'number': '3004', 'teacher': 'Хайнс', 'time': '8:00'}, 
#     'CS102': {'number': '4501', 'teacher': 'Альварадо', 'time': '9:00'}, 
#     'CS103': {'number': '6755', 'teacher': 'Рич', 'time': '10:00'}, 
#     'NT110': {'number': '1244', 'teacher': 'Берк', 'time': '11:00'}, 
#     'CM241': {'number': '1411', 'teacher': 'Ли', 'time': '13:00'}
#     }

# slov2 = {
#     'CS101': [' 3004, ','Хайнс, ', '8:00'], 
#     'CS102': [' 4501, ','Альварадо, ', '9:00'], 
#     'CS103': [' 6755, ','Рич, ', '10:00'], 
#     'NT110': [' 1244, ','Берк, ', '11:00'], 
#     'CM241': [' 1411, ','Ли, ', '13:00']
#     }
# print(string1,':', *slov2[string1], sep='')



# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# string1 = input()
# for i in string1:
#     for key, value in keyboard.items():
#         if i.upper() in value:
#             for j in value:
#                 print(key, end='')
#                 if j == i.upper():
#                     break


# text = input().upper()
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# info = dict(zip(letters, morse))
# for i in range(len(text)):
#     temp1 = text[i]
#     if text[i] == '0123456789':
#         text[i].lower()
#     if text[i] in ' +-=,!.?':
#         continue
#     print(info[temp1], end = ' ')
# print(info[text])



# result = {}
# for i in range(1, 16):
#     temp1 = {i : i**2}
#     result.update(temp1)



# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# mnoge = set()
# result = {}
# keys1 = dict1.keys()
# keys2 = dict2.keys()
# for i in keys1:
#     mnoge.add(i)
# for i in keys2:
#     mnoge.add(i)
# for i in mnoge:
#     temp1 = dict2.setdefault(i, 0)
#     temp2 = {i : dict1.setdefault(i, 0)+temp1}
#     result.update(temp2)


# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for i in text:
#     key_count = 1
#     if i in result:
#         key_count += result.get(i)
#     temp_dict = {i:key_count}
#     result.update(temp_dict)


# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# spis = s.split()
# spis_max = []
# result = {}
# for i in spis:
#     key_count = 1
#     if i in result:
#         key_count += result.get(i)
#     temp_dict = {i:key_count}
#     result.update(temp_dict)
# max1 = max(result.values())
# for i in result:
#     temp = result[i]
#     if temp == max1:
#         spis_max.append(i)
# min1 = min(spis_max)
# print(min1)


# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}

# for i in pets:
#     temp_pets = []
#     local_key = i[1:4]
#     local_value = i[0]

#     if local_key in result:
#         result_value = result.get(local_key)
#         result_value.append(local_value)
#         temp_pets = result_value
#     else:
#         temp_pets.append(local_value)

#     temp1 = {local_key : temp_pets}
#     result.update(temp1)



# s = input().lower()
# ignore = '.,!?:;-'
# spis = s.split()
# spis_max = []
# result = {}
# for i in spis:
#     key_count = 100
#     if i in result:
#         key_count -= result.get(i)
#     temp_dict = {i:key_count}
#     result.update(temp_dict)
# min1 = min(result.values())
# for i in result:
#     temp = result[i]
#     if temp == min1:
#         spis_max.append(i)
# min1 = min(spis_max)
# print(min1)



# text = input().split()
# ignore = '.,!?:;-'
# spis_clear = []
# for i in text:
#     if text[i] in ignore:
#         print(1)


# spis = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = {}
# spis_max = []
# for i in spis:
#     key_count = 1
#     if i in result:
#         key_count += result.get(i)
#     temp_dict = {i:key_count}
#     result.update(temp_dict)

# min1 = min(result.values())
# for i in result:
#     temp = result[i]
#     if temp == min1:
#         spis_max.append(i)
# min2 = min(spis_max)
# print(min2)


# def counter_el(spis, el):
#     counter = 0
#     for i in spis:
#         if i == el:
#             counter += 1
#     return counter
# spis = input().split()
# result = []
# for i in spis:
#     if i in result:
#         counter = counter_el(result, i)
#         print(i, '_', counter, sep='', end=' ')
#         result.append(i)
#         continue
#     result.append(i)
#     print(i, end=' ')


# range1 = int(input())
# dict_res = {}

# for i in range(range1):
#     keys,value = input().split(':')
#     keys = keys.lower()
#     value = value.lstrip()
#     dict_res[keys] = value

# range2 = int(input())
# spis = []
# for i in range(range2):
#     res_key = input()
#     spis.append(res_key.lower())
# for i in spis:
#     if dict_res.get(i, 0):
#         print(dict_res[i])
#     else:
#         print('Не найдено')


# def counter_el(spis, el):
#     counter = 0
#     for i in spis:
#         if i == el:
#             counter += 1
#     return counter
# string1 = input()
# string2 = input()
# counter_el(string1)
# print()



# string1 = input()
# string2 = input()
# result1 = {}
# result2 = {}

# for i in string1:
#     key_count = 1
#     if i in result1:
#         key_count += result1.get(i)
#     temp_dict = {i:key_count}
#     result1.update(temp_dict)

# for i in string2:
#     key_count = 1
#     if i in result2:
#         key_count += result2.get(i)
#     temp_dict = {i:key_count}
#     result2.update(temp_dict)


# if result1[i] == result2[i]:
#     print('YES')



# spis = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = {}
# spis_max = []
# for i in spis:
#     key_count = 1
#     if i in result:
#         key_count += result.get(i)
#     temp_dict = {i:key_count}
#     result.update(temp_dict)
# print(result)


# text1 = input()
# text2 = input()
# string1 = text1.lower()
# string2 = text2.lower()
# spis1 = string1.split()
# spis2 = string2.split()
# dict1 = {}
# dict2 = {}
# for i in string1:
#     if i in '.,!?:;- ':
#         continue
#     counter = 1
#     if i in dict1:
#         counter += dict1.get(i)
#     temp_dict = {i:counter}
#     dict1.update(temp_dict)
# for i in string2:
#     if i in '.,!?:;- ':
#         continue
#     counter = 1
#     if i in dict2:
#         counter += dict2.get(i)
#     temp_dict = {i:counter}
#     dict2.update(temp_dict)
# if dict1 == dict2:
#     print("YES")
# else:
#     print('NO')


# range1 = int(input())
# dict_res = {}
# for i in range(range1):
#     text = input()
#     spis = text.split(' ')
#     temp_dict = {spis[0]:spis[1]}
#     dict_res.update(temp_dict)
# key_find = input()

# if key_find not in dict_res:
#     keys = list(dict_res.keys())
#     index = list(dict_res.values()).index(key_find)
#     key = keys[index]
#     print(key)
# else:
#     print(dict_res.get(key_find))


# def get_key(d, value):
#     for k, v in d.items():
#         if value in v:
#             return k

# range1 = int(input())
# dict_res = {}
# spis_res = []

# for i in range(range1):
#     contry_city = input()
#     contry_city_split = contry_city.split()
#     cities = contry_city_split[1:]
#     contry = contry_city_split[0]
#     temp_dict = {contry:cities}
#     dict_res.update(temp_dict)

# range2 = int(input())
# for i in range(range2):
#     key_find = input()
#     res_country = get_key(dict_res, key_find)
#     spis_res.append(res_country)
# print(*spis_res, sep='\n')




# range1 = int(input())
# dict_res = {}
# name_request = []
# for i in range(range1):
#     text = input()
#     spis = text.split(' ')
#     number = spis[0]
#     name = spis[1]
#     name_upper = name.upper()
#     if name_upper in dict_res:
#         dict_res[name_upper].append(number)
#         continue
#     else:
#         spis_numbers = [number]

#     dict1 = {name_upper:spis_numbers}
#     dict_res.update(dict1)
# range2 = int(input())
# for i in range(range2):
#     text2 = input()
#     text2_up = text2.upper()
#     name_request.append(text2_up)
# for i in name_request:
#     if i in dict_res:
#         print(*dict_res[i])
#     else:
#         print('абонент не найден')



# def create_dict_desh():
#     dict_res = {}
#     range1 = int(input())
#     for i in range(range1):
#         key, value = input().split(': ')
#         value = int(value)
#         dict1 = {key:value}
#         dict_res.update(dict1)
#     return dict_res

# def create_dist_shif(text):
#     dict_res = {}
#     for i in text:
#         if i in dict_res:
#             value = dict_res[i]
#             temp_dict = {i:value+1}
#         else:
#             temp_dict = {i:1}
#         dict_res.update(temp_dict)
#     return dict_res

# def result(el, temp1, temp2):
#     for key, value in temp1.items():
#         for key2, value2 in temp2.items():
#             if value == value2 and el == key:
#                 return key2


# text = input()
# temp1 = create_dist_shif(text)
# temp2 = create_dict_desh()
# for i in text:
#     res1 = result(i, temp1, temp2)
#     print(res1, sep='', end='') 



# marks = { 
#    'class':{ 
#       'student':{ 
#          'name':'Rosaly',
#          'marks':{ 
#             'physics':70,
#             'history':80
#          }
#       }
#    }
# }
# print(marks['class'][0]['marks']['history'])


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i: numbers[i]**2 for i in range(len(numbers))}
# print(result)


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {i: colors[i] for i in colors if colors[i] != None}
# print(result)



# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}

# result = {i: favorite_numbers[i] for i in favorite_numbers if len(str(favorite_numbers[i])) == 2}
# print(result)


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {months[i]: i for i in months }
# print(result)


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(key): value for key, value in (a.split(':') for a in s.split())}
# print(result)


# def temp1(num):
#     spis = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             spis.append(i)
#     return spis
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {i: temp1(i) for i in numbers}


# def temp1(text):
#     spis = []
#     for i in text:
#         temp2 = ord(i)
#         spis.append(temp2)
#     return spis
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {i: temp1(i) for i in words}
# print(result)


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}

# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

# result = {i:letters[i] for i in letters if i not in remove_keys}



# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

# result = {i:students[i] for i in students if students[i][0] > 167 and students[i][1] < 75}
# print(result)



# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {i[0]: i[1:3] for i in tuples}
# print(result)



# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# zip1 = zip(student_names, student_grades)
# # dict1 = {student_names:student_grades}
# result = []
# dict_gen = {student_ids:zip1 for i in }
# print(dict_gen) 
# result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]




# def convert_r(list1):
#     temp = []
#     for i in list1:
#         if i < 20:
#             temp.append(i)
#     return temp
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# result = {i: convert_r(my_dict[i]) for i in my_dict}
# my_dict = result
# print(my_dict)




# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# result = []
# for i in emails:
#     for j in emails[i]:
#         result.append(j+'@'+i)
# print(*sorted(result),sep='\n')


# def convert_dna(dna):
#     slov_dna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
#     return slov_dna[dna]
# text = input()
# for i in text:
#     x = convert_dna(i)
#     print(x,end='')


# def create_dist_shif(text):
#     dict_res = {}
#     for i in text:
#         if i in dict_res:
#             value = dict_res[i]
#             temp_dict = {i:value+1}
#             print(temp_dict[i],end=' ')
#         else:
#             temp_dict = {i:1}
#             print(1, end=' ')
#         dict_res.update(temp_dict)
#     return dict_res
# text = input().split()
# create_dist_shif(text)



# text = input()
# points = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# counter = 0
# for i in text:
#     for j in points:
#         if i in points[j]:
#             counter += j
#             break
# print(counter)



# def build_query_string(slov):
#     temp = sorted(slov)
#     for i in range(len(temp)):
#         tempstr=temp[i]+"="+str(slov[temp[i]])
#         print(tempstr, end='')
#         if len(temp) != i+1:
#             print('&',end='')
    

# def build_query_string(params):
#     temp = sorted(params)
#     spis = []
#     for i in range(len(temp)):
#         tempstr=temp[i]+"="+str(params[temp[i]])
#         spis.append(tempstr)
#     return "&".join(spis)
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sort': 'hockey', 'game': 2, 'time': 17}))


# def merge(values):      # values - это список словарей
#     slov = {}
#     for i in values:
#         for j in i:
#             slov_temp3 = {i[j]}
#             if j in slov:
#                 slov[j].update(slov_temp3)
#                 # slov[j].update(dict(sorted(slov[j])))
#             else:
#                 slov_temp2 = {j:slov_temp3}
#                 slov.update(slov_temp2)
#         # slov[j].update(sorted(slov[j]))
#     return slov
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# # result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# print(result)



# slov = {'execute':[], 'read':[], 'write':[]}
# len_1 = int(input())
# for i in range(len_1):
#     spis = input().split()
#     for j in range(1, len(spis)):
#         if spis[j] == 'X':
#             slov['execute'].append(spis[0])
#         if spis[j] == 'W':
#             slov['write'].append(spis[0])
#         if spis[j] == 'R':
#             slov['read'].append(spis[0])
# # slov = {'execute':['dc_com'], 'read':[], 'write':["ave"]}
# len_2 = int(input())

# spis_res = []
# for i in range(len_2):
#     spis = input().split()
#     flag = False
#     if spis[1] in slov[spis[0]]:
#         spis_res.append('OK')
#     else:
#         spis_res.append('Access denied')


# for k in spis_res:
#     print(k)


# slov = {}
# len_1 = int(input())
# for i in range(len_1):
#     spis = input().split()
#     # spis[0] = имя
#     # spis[1] = товар
#     # spis[2] = кол-во
#     if spis[0] in slov:
#         if spis[1] in slov[spis[0]]:
#             temp_slov = {spis[1]: slov[spis[0]][spis[1]] + int(spis[2])}
#             slov[spis[0]].update(temp_slov)
#         else:
#             temp_slov = {spis[1]:int(spis[2])}
#             slov[spis[0]].update(temp_slov)
#     else:
#         temp_slov = {spis[1]:int(spis[2])}
#         slov.update({spis[0]:temp_slov})
# # print(slov)
# # slov = {'Вячеслав': {'Ручка': 30, 'Линейка': '4'}, 'Филип': {'Ручка': 1, 'Циркуль': '1'}, 'Виктория': {'Перо': 3, 'Тетрадь': '7'}}
# for i in sorted(slov):
#     print(i,':',sep='')
#     for j in sorted(slov[i]):
#         print(j, slov[i][j])



# import random
# range1 = int(input())
# for i in range(range1):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')


# import random
# n = int(input())    # количество попыток
# for i in range(n):
#     num = random.randint(1, 6)
#     print(num)


# import random
# spis = []
# length = int(input())    # длина пароля
# for i in range(length):
#     number = random.randint(0, 1)
#     if number == 0:
#         num1 = random.randint(65, 90)
#         symb1 = chr(num1)
#         spis.append(symb1)
#     else:
#         num2 = random.randint(97, 122)
#         symb2 = chr(num2)
#         spis.append(symb2)
# print(*spis, sep='')


# import random
# spis = []
# for i in range(7):
#     bilet = random.randint(1, 49)
#     spis.append(bilet)
# print(*sorted(spis))


# import random
# def generate_ip():
#     spis = []
#     for i in range(4):
#         num = random.randint(0, 255)
#         spis.append(str(num))
#     x = '.'.join(spis)
#     return x
# print(generate_ip())


# import random
# import string
# def generate_index():
#     spis = []
#     for i in range(5):
#         up = string.ascii_uppercase
#         if i == 2 or i == 3:
#             choice_num = random.randint(0, 99)
#             spis.append(str(choice_num))
#         choice_let = random.choice(up)
#         spis.append(choice_let)
#     spis[3] = '_'
#     temp_str = ''
#     for i in spis:
#         temp_str += i
#     return temp_str
# print(generate_index())



# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# for i in matrix:
#     random.shuffle(i)
# print(matrix)

# import random
# for i in range(100):
#     num = random.randint(1000000, 9999999)
#     print(num)


# import random
# word = input()
# list1 = list(word)
# shuf = random.shuffle(list1)
# print(*list1, sep='')


# import random
# numbers = ''
# while len(numbers) != 25:
#     x = random.randint(1, 75)
#     if len(numbers) != 12:

#         r = numbers.ljust(3)
#         numbers += r + str(x)
#     else:
#         numbers += '0'
#         numbers.ljust(3)
# #     if len(numbers) == 5 or len(numbers) == 10 or len(numbers) == 15 or len(numbers) == 20:
        
# # print(numbers)



# import random
# def random_mnoge():
#     mnoge = set()
#     while len(mnoge) != 25:
#         number = random.randint(1, 75)
#         mnoge.add(number)
#     return mnoge

# string1 = ''
# temp_str = ''
# x = random_mnoge()
# counter = 0
# for i in x:
#     counter += 1
#     if counter != 13:
#         print(str(i).ljust(3), end='')
#     else:
#         print(str(0).ljust(3), end='')
#     if counter % 5 == 0:
#         print()

# print(string1)
# for j in range(5):
#     print(string1,)



# import random
# spis = []
# result = []
# temp_spis = []
# # slov = {}
# range1 = int(input())

# for i in range(range1):
#     text = input()
#     spis.append(text)
#     temp_spis.append(text)

# for i in range(range1):
#     choice1 = random.choice(temp_spis)
#     while spis[i] == choice1:
#         choice1 = random.choice(temp_spis)
#     temp_spis.remove(choice1)
#     print(spis[i], '-',  choice1)


# import string
# import random

# def generate_password(length):
#     up_let = string.ascii_uppercase
#     low_let = string.ascii_lowercase
#     letters = string.ascii_letters
#     digits = string.digits
#     password = ''
#     choice_up = random.choice(up_let)
#     choice_low = random.choice(low_let)
#     choice_let = random.choice(letters)
#     choice_dig = random.choice(digits)

#     while len(password) != length:
#         choice_let = random.choice(letters)
#         choice_dig = random.choice(digits)
#         if choice_dig != '1' and choice_dig != '0' and choice_let != 'l' and choice_let != 'I' and choice_let != 'o' and choice_let != 'O':
#             choice = random.randint(0, 1)
#             if choice == 0:
#                 password += choice_let
#             else:
#                 password += choice_dig
#         else:
#             continue
#     def up_let_FN(pas):
#         for i in pas:
#             if i in up_let:
#                 return True
#         return False
#     def low_let_FN(pas):
#         for i in pas:
#             if i in low_let:
#                 return True
#         return False
#     def digits_FN(pas):
#         for i in pas:
#             if i in digits:
#                 return True
#         return False
#     def symb_FN(pas):
#         for i in pas:
#             if i in 'oO10lI':
#                 return False
#         return True
#     while up_let_FN(password) == False or low_let_FN(password) == False or digits_FN(password) == False or symb_FN(password) == False:
#         randi_up = random.randint(0, len(password) - 1)
#         randi_low = random.randint(0, len(password) - 1)
#         randi_dig = random.randint(0, len(password) - 1)
#         password = password[:randi_up] + choice_up + password[randi_up + 1:]
#         password = password[:randi_low] + choice_low + password[randi_low + 1:]
#         password = password[:randi_dig] + choice_dig + password[randi_dig + 1:]

#     return password
    

# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))

# n, m = int(input()), int(input())
# generate_passwords(n, m)






# import string
# import random

# def symb_FN(pas):
#     for i in pas:
#         if i in 'oO10lI':
#             return False
#     return True

# def generate_password(length):
#     up_let = string.ascii_uppercase
#     low_let = string.ascii_lowercase
#     digits = string.digits
#     choice_up = random.choice(up_let)
#     choice_low = random.choice(low_let)
#     choice_dig = random.choice(digits)
#     res = choice_up + choice_low + choice_dig

#     while symb_FN(res) == False:
#         up_let = string.ascii_uppercase
#         low_let = string.ascii_lowercase
#         digits = string.digits
#         choice_up = random.choice(up_let)
#         choice_low = random.choice(low_let)
#         choice_dig = random.choice(digits)
#         res = choice_up + choice_low + choice_dig
    
#     digs = '23456789'
#     for i in range(1, length-2):
#        choice_dig = random.choice(digs)
#        res += choice_dig
#     return res
# def generate_passwords(count, length):
#     for i in range(count):
#         print(generate_password(length))

# n, m = int(input()), int(input())
# generate_passwords(n, m)

# import random

# n = 10**6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)

#     if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
#         k += 1

# print((k/n)*s0)



# import random

# n = 10**6       # количество испытаний
# k = 0.0
# for i in range(n):
#     x = random.random()
#     y = random.random()
#     k += (x * x + y * y < 1.0)
# print(4 * k / n)


# from decimal import *
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
# space = s.split()
# lst = []
# for i in space:
#     lst.append(Decimal(i))
# min1 = min(lst)
# max1 = max(lst)
# print(min1 + max1)

# from decimal import *
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'

# numbers = s.split()
# lst = []
# sum1 = 0
# for i in numbers:
#     lst.append(Decimal(i))

# for i in lst:
#     sum1 += i

# sord = sorted(lst)
# print(sum1)
# sor = sorted(sord[-5:], reverse=True)
# print(*sor)


# from decimal import *
# number = Decimal(input())
# number_tuple = number.as_tuple()
# max1 = max(number_tuple.digits)
# min1 = min(number_tuple.digits)
# if int(number) == 0:
#     print(max1)
# else:
#     print(max1 + min1)


# from decimal import *
# d = Decimal(input())
# res = d.exp() + d.ln() + d.log10() + d.sqrt()
# print(res)



# from fractions import Fraction

# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# for i in numbers:
#     num = Fraction(i)
#     print(i, '=', num)


# from fractions import Fraction

# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

# numbers = s.split()
# maxS = max(numbers)
# minS = min(numbers)
# num1 = Fraction(maxS)
# num2 = Fraction(minS)
# print(num1 + num2)


# from fractions import Fraction
# numerator = int(input())
# denominator = int(input())
# num1 = Fraction(numerator)
# num2 = Fraction(denominator)
# print(num1/num2)

# from fractions import Fraction
# number1 = input()
# number2 = input()
# n1 = Fraction(number1)
# n2 = Fraction(number2)
# print(number1, '+', number2, '=',(n1 + n2))
# print(number1, '-', number2, '=',(n1 - n2))
# print(number1, '*', number2, '=',(n1 * n2))
# print(number1, ':', number2, '=',(n1 / n2))



# from fractions import Fraction
# num = int(input())
# temp_res = 0
# for i in range(1, num+1):
#     temp_res += Fraction(f'1/{i**2}')
# print(temp_res)


# from fractions import Fraction
# from math import *
# num = int(input())
# temp_res = 0
# for i in range(1, num+1):
#     temp_res += Fraction(f'1/{factorial(i)}')
# print(temp_res)



# from fractions import Fraction
# from math import *
# num = int(input())
# numerator = num // 2
# denominator = num - numerator
# while gcd(numerator, denominator) != 1:
#     numerator -= 1
#     denominator += 1
# print(Fraction(numerator, denominator))



# from fractions import Fraction
# from math import *
# num = int(input())
# spis = []
# for i in range(1, num+1):
#     for j in range(1, num+1):
#         if (i > j) or i == j:
#             continue
#         temp = gcd(i, j)
#         if (temp == 1):
#             spis.append(Fraction(i, j))
# print(*sorted(spis), sep='\n')



# num1 = complex(input())
# num2 = complex(input())
# print(num1, '+', num2, '=', complex(num1) + complex(num2))
# print(num1, '-', num2, '=', complex(num1) - complex(num2))
# print(num1, '*', num2, '=', complex(num1) * complex(num2))


# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# temp1 = max(numbers, key=abs)
# print(temp1)
# print(abs(temp1))



# n = int(input())
# z1 = complex(input())
# z2 = complex(input())
# z1s = z1.conjugate()
# z2s = z2.conjugate()
# print(z1**n + z2**n + z1s**n + z2s**(n+1))



# def fancy(length, char1, char2):
#     return (char1 + char2) * length + char1
# print(fancy(5, '-', '*'))


# lst = []
# def matrix(n=1, m=None, value=0):
#     if n == 1 and m == None:
#         m = 1
#     elif n != 1 and m == None:
#         m = n
#     return [[value]*m for i in range(n)]



# def count_args(*args):
#     return len(args)
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))



# def sq_sum(*args):
#     sum1 = 0
#     for i in args:
#         sum1 += i**2
#     return sum1
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))



# def mean(*args):
#     sum = 0
#     kol = 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#             sum += i
#             kol += 1
#     if sum == 0 and kol == 0:
#         return 0
#     else:
#         return sum / kol
    

# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))



# def greet(*args):
#     lst = ''
#     for i in args:
#         if len(args) == 1:
#             str_1 = 'Hello, ' + args[0] + '!'
#             return str_1
#         else:
#             if i == args[0]:
#                 str_2 = 'Hello, ' + i
#             else:
#                 str_3 = str_2 + ' and ' + i + '!'
#                 lst += str_3
#     lst += str_3, i
#     return str_3


# # print(greet('Timur'))
# # print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))



# def greet(n, *args):
#     string1 = 'Hello, '
#     string2 = ''
#     for i in range(len(args)):
#         if i < len(args):
#             string2 += ' and '
#         string2 += args[i]
            
#     return f"{string1}{n}{string2}!"
    
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))




# def print_products(*args):
#     args = [i for i in args if type(i) == str and len(i) > 0]
#     if args:
#         for i,j in enumerate(args):
#             print(f'{i+1}) {j}')
#         return ''
#     print('Нет продуктов')
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '') 





# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(key + ": " + str(value))
# print()


# def f1(x):
#     return 2*x+1


# def f2(x):
#     return x**2


# def f3(x):
#     return -x**2+1


# def f4(x):
#     return x-3


# funcs = [f1, f2, f3, f4]
# i = int(input())
# print(funcs[i](2))


# def func(a):
#     return sum(a) / len(a)
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# print(min(numbers, key=func(numbers)))
# print(max(numbers, key=func(numbers)))



# from math import *
# def func(j):
#     return sqrt(j[0]**2 + j[1]**2) 
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# points = sorted(points, key=func)


# print(points)


# def func(j):
#     return min(j) + max(j)
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# print(sorted(numbers, key=func))


# def sort1(x):
#     return x[num-1]
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# global num
# num = int(input())
# sor = sorted(athletes, key=sort1)
# for i in sor:
#     print(*i)



# from math import *
# def f1(x):
#     return x**2
# def f2(x):
#     return x**3
# def f3(x):
#     return sqrt(x)
# def f4(x):
#     return abs(x)
# def f5(x):
#     return sin(x)
# num = int(input())
# action = input()
# commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
# print(commands[action](num))



# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result

# def predicate(word):
#     return word == word[::-1]

# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
# filtered = filter(predicate, words)
# print(len(filtered))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))

# print(var1 + var2)


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(round(item, 2)))
#     return result

# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# temp = map(str, numbers)
# for i in temp:
#     print(i)



# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# numbersLen3 = []
# numbersDev5 = []
# for i in numbers:
#     if len(str(i)) == 3:
#         numbersLen3.append(i)
# for i in numbersLen3:
#     if int(i) % 5 == 2:
#         numbersDev5.append(i)
# for i in numbersDev5:
#     print(i**3)



# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc

# def func(x, y):
#     return x+y**2

# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# result = reduce(func, numbers, 0)
# print(result)



# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result

# def func(x):
#     return x**2

# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# res = sum(map(func, numbers))
# print(res)



# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# def double_digith(x):
#     return x % 7 == 0 and 9 < abs(x) < 100


# def squere(num):
#     return num**2

# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# filt = filter(double_digith, numbers)
# mp = map(squere, filt)
# print(sum(mp))



# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7

# def func_apply(function, values):
#     result = []
#     for item in values:
#         result.append(function(item))
#     return result

# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))



# high_ord_func = lambda x, func: x + func(x)

# result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)

# print(result)



# from functools import reduce 

# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]

# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name[::-1] == name, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

# print(map_result)
# print(filter_result)
# print(reduce_result)



# from functools import reduce

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]

# # filter_lambda = list(filter(lambda x:x[1] > 10000000, data))
# # red = list(filter(lambda x:x[1] > 10000000 and x[2] == 'primary', data))
# print('Cities: ' + ', '.join(sorted([city[0] for city in data if city[1]>10**7 and city[2]== 'primary'])))



# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda: True, primes))
# print(result)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result)


# func = lambda x: True if x % 19 == 0 and x % 13 == 0 else None
# print(func)


# func = lambda x: True if (x[0] == 'a' or x[0] == 'A') and (x[-1] == 'A' or x[-1] == 'a') else False
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))



# is_non_negative_num = lambda x: True if x[0] != '-' and x.count('.') < 2 and x.lower() == x.upper() else False

# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))



# # is_num = lambda x: True if x.replace('.', '1') and x.replace('-', '1') else False
# def is_num(x):
# #     for i in range(len(x)):
#         # if not x[i].isdigit() and x[i] != '.' and '-' not in i:
#         #     return False
#         try:
#             int(float(x))
#             return True
#         except ValueError:
#             return False

# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))



# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# res = sorted(filter(lambda x: True if len(x) == 6 else False, words))
# print(*res)


# def delete(lst):
#     for i in lst:
#         if i != i % 2 and i > 47:
#             lst.remove(i)
#         if i % 2 == 0:
#             i // 2
#     return lst
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# # odd = filter(lambda x: x > 47 and x // 2, numbers)
# print(delete(numbers))



# def delete(elem):
#     if (elem < 47 and elem % 2 != 0) or elem % 2 == 0:
#         return True
#     return False
    
# def devide_odd(elem):
#     if elem % 2 == 0:
#         return elem // 2
#     return elem
# #     new_lst = []
# #     for i in range(len(lst)):
# #         if lst[i] > 47 and lst[i] % 2 != 0:
# #             del lst[i]
# #         if lst[i] % 2 == 0:
# #             lst[i] = lst[i] // 2
# #     return lst

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# # numbers2 = list()
# numbers3 = list(map(devide_odd ,filter(delete ,numbers))) 
# print(*numbers3)
# # print(*numbers2)




# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# for i in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f"{i[1]}: {i[0]}")



# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# sort = sorted(data)
# res = sorted(sort, key=lambda x: len(x))
# print(*res)



# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# sort = max(mixed_list, key=lambda x:x if type(x) == int else 1)
# print(sort)



# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# sort_int = sorted(mixed_list, key=lambda x:x if type(x) == int else 0)
# sort_str = sorted(sort_int, key = lambda x:x if type(x) == str else ' ')
# print(*sort_str)



# rgb_colors = input().split()
# print(255 - int(rgb_colors[0]), 255 - int(rgb_colors[1]), 255 - int(rgb_colors[2]))



# from functools import reduce
# def evaluate(coefficients_inner, x):
#     res = 0
#     for i in range(len(coefficients_inner)):
#         int_i = int(coefficients_inner[i])
#         len_coef = len(coefficients_inner)
#         squere = x**(len_coef-1-i)
#         res += int_i * squere
#     return res


# coefficients = input().split()
# x = int(input())

# # def evaluate2(result, coefficients_inner):
# #     int_i = int(coefficients_inner)
# #     return int_i + result

# # print(reduce(evaluate2, coefficients, 0))
# print(evaluate(coefficients, x))




# numbers = [10, 30, 20, 50, 40, 60, 70, 80]

# total = 0
# for index, number in enumerate(numbers, 1):
#     if index % 2 == 0:
#         total += number
# print(total)





# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']    
#     for item in ignore:
#         if item in command:
#             return True
#     return False





# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# general = zip(countries, capitals, population)
# for i in general:
#     print(list(i)[1] + ' is the capital of ' + list(i)[0] + ', population equal ' + str(i[2]) + ' people.')




# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
# Radius = 4
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))



# import string
# ip = input().split('.')
# result = []
# for i in ip:
#     if i[0] not in string.ascii_letters and i[-1] not in string.ascii_letters:
#         if int(i) >= 0 and int(i) <= 255:
#             result.append(True)
#         else:
#             result.append(False)
#     else:
#         result.append(False)
# print(all(result))




# a = input()
# b = input()
# numbers = []
# result = []
# for i in range(int(a), int(b)+1):
#     numbers.append(i)

# for i in range(len(numbers)):
#     temp = []
#     for j in str(numbers[i]):
#         if '0' not in str(numbers[i]):
#             if numbers[i] % int(j) == 0:
#                 temp.append(True)
#             else:
#                 temp.append(False)

#     if all(temp) == True and len(temp) != 0:
#         result.append(numbers[i])
# print(*result)




# a = input()
# print("YES" if all([any(map(lambda x: x.isdigit(), a)), any(map(lambda x : x.islower(), a)), any(map(lambda x : x.isupper(), a)), len(a) > 6]) else "NO")




# class_count = int(input())
# result = []
# for i in range(class_count):
#     member_count = int(input())
#     temp_class = []
#     for j in range(member_count):
#         name_grade = input().split()
#         if name_grade[1] == '5':
#             temp_class.append(True)
#         else:
#             temp_class.append(False)
#     result.append(any(temp_class))
# if all(result) == True:
#     print('YES')
# else:
#     print('NO')






# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
#     str = f'To: {mail}\n'
#     str += f'Приветствую, {name}!\n'
#     str += f'Вам назначен экзамен, который пройдет {date}, в {time}.\n'
#     str += f'По адресу: {place}.\n' 
#     str += f'Экзамен будет проводить {teacher} в кабинете {number}.\n'
#     str += 'Желаем удачи на экзамене!'
#     return str

# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2', 'Василь Ярошевич', 23))





# def pretty_print(data, side='-', delimiter='|'):
#     str = ''
#     for i in data:
#         str += f'{delimiter} {i} '
#     str += delimiter
#     ln = len(str)-2
#     sd = f' {side*ln} '
#     print(sd)
#     print(str)
#     print(sd)

# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')




# from functools import reduce
# import operator

# def flatten(data):
#     return reduce(operator.concat, data, [])

# result = flatten([[1, 2], [3, 4], [], [5]])

# print(result)





# def concat(*imp, sep=' '):
#     result = ''
#     if len(imp) <= 1:
#         return imp[0]
    
#     for i in range(len(imp)):
#         if sep == ' ':
#             result += f'{str(imp[i])} '
#         if sep != ' ':
#             if i == len(imp)-1:
#                 result += f'{str(imp[i])}'
#             else:
#                 result += f'{str(imp[i])}{sep}'

#     return result


# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))





# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result




# words = 'the world is mine take a look what you have started'.split()
# print(*map(lambda x:f'"{x}"', words))


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# # print(*map(lambda x:numbers.remove(x) if x == x[::-1] else None, numbers))
# # for i in range(len(numbers)):
# #     if numbers[i] == numbers[i][::-1]:
# #         print(i)
# def sor(numbers):
#     lst = []
#     for i in numbers:
#         str_i = str(i)
#         if str_i != str_i[::-1]:
#             lst.append(i)
#     return lst
# print(*sor(numbers))




# def func(tup):
#     for i in numbers:
#         count = 0
#         ln = len(i)
#         for j in i:
#             count += j
#         arfm = count / ln
#     return arfm
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# # res = []
# # for i in numbers:
# #     count = 0
# #     ln = len(i)
# #     for j in i:
# #         count += j
# #     arfm = count / ln
#     # res.append(str(i) + ' = ' + str(arfm)) 
# # print(res)
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
# print(*sorted_numbers)





# def call(function, *num):
#     return function(*num)

# def mul7(x):
#     return x * 7


# def add2(x, y):
#     return x + y


# def add3(x, y, z):
#     return x + y + z


# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))






# def compose(a, b):
#     return lambda x: a(b(x))

# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7


# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))





# from operator import *
# def arithmetic_operation(operation):
#     return {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}[operation]

# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))




# text = input().split()
# print(*sorted(text, key=lambda x: x.lower()))




# def ip_to_decimal(ip):
#     octets = ip.split('.')
#     decimal_ip = 0
#     for i in range(4):
#         decimal_ip += int(octets[i]) * (256 ** (3 - i))
#     return decimal_ip

# def main():
#     n = int(input())
#     ip_addresses = [input().strip() for _ in range(n)]

#     sorted_ips = sorted(ip_addresses, key=lambda x: ip_to_decimal(x))

#     for ip in sorted_ips:
#         print(ip)

# if __name__ == "__main__":
#     main()







# file_inp = input()
# file = open(file_inp, 'r')
# for i in file:
#     content = list(map(str.strip, file.readlines()))
#     print(content)
# file.close()




# file = open('nums.txt', 'r')
# num = file.readlines()
# numbers1 = list(map(str.strip, file.readlines()))
# counter = 0
# for i in numbers1:
#   if len(i) >= 1:
#     counter += int(i)
# file.close()
# print(counter)



# with open('nums.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')



# import string
# with open('file.txt') as file:
#     lines = list(map(str.strip, file.readlines()))
#     tx = file.read().split()
#     letters = 0
#     words = 0
#     strings = 0
#     words = len(tx)
#     for i in range(len(lines)):
#         strings = len(lines)
#         for j in lines[i]:
#             if j in string.ascii_letters:
#                 letters += 1
#     print('Input file contains:')
#     print(str(letters) + ' letters')
#     print(str(words) + ' words')
#     print(str(strings) + ' lines')





# with open('population.txt') as file:
#     population = list(map(str.split, file.readlines()))
#     for i in population:
#       if i[0][0] == 'G' and int(i[1]) > 500000:
#         print(i[0])





# with open('class_scores.txt', 'r') as start_value, open('new_scores.txt', 'a') as output:
#     lines = list(map(str.strip, start_value.readlines()))
#     for i in lines:
#         new_scor = int(i[1]) + 5
#         print(str(i[0]) + str(new_scor))








# with open('goats.txt', 'r') as goats, open('answer.txt', 'a') as output:
#     lines = list(map(str.strip, goats.readlines()))
#     lines.remove('COLOURS')
#     lines.remove('GOATS')
#     dict_lst = {}
    
#     for i in lines:
#         if i not in dict_lst:
#             dct = {i:0}
#             dict_lst.update(dct)
#         else:
#             dict_lst[i] += 1
    
#     sum_goats = sum(dict_lst.values())
#     for i in dict_lst:
#         if dict_lst[i] * 100 > 7 * sum_goats:
#             print(i, file=output)




# n = int(input())
# result = ''

# for i in range(n):
#     with open(input()) as file:
#         result += file.read()
    
# with open('output.txt', 'w') as file:
#     file.write(result)




# def minutes(x):
#     res=[int(i) for i in x.split(':')]
#     return res[0]*60+res[1]

# with open ('logfile.txt', 'r') as file, open('output.txt', 'r') as output:
#     lines = list(map(str.strip, file.readlines()))
#     for i in lines:
#         print(minutes(i))





# def minutes(x):
#     res=[int(i) for i in x.split(':')]
#     return res[0]*60+res[1]

# with open ('logfile.txt', 'r', encoding="utf8") as logs, open('output.txt', 'a', encoding="utf8") as output:
#     lines = list(map(str.strip, logs.readlines()))
#     for i in lines:
#         lst = str(i).split(', ')
#         if minutes(lst[2]) - minutes(lst[1]) >= 60:
#             print(lst[0], file=output)




# word = input() + ' запретил букву'
# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# for i in alphabet:
#     if i in word:
#         print(word, i)
#         word = word.replace(i, '').replace('  ', ' ').strip()



# rang = int(input())
# res = []
# for i in range(rang):
#     anton = ['a', 'n', 't', 'o', 'n']
#     counter = 0
#     fridge = input()
#     for j in fridge:
#         if j in anton and j == anton[0]:
#             anton.remove(j)
#             counter += 1
#             if counter == 5:
#                 res.append(i+1)
#                 break
# print(*res)



# d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
#     'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
#     'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
#     'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
#     'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
#     }
# with open ('cyrillic.txt', 'r', encoding="utf8") as file, open('transliteration.txt', 'a', encoding="utf8") as output:
#     result = ''
#     lines = list(file.readlines())
#     for i in range(len(lines)):
#         for j in lines[i]:
#             if j in d:
#                 result += d[j]
#             else:
#                 result += j
#     print(result, file=output)






with open (input(), 'r', encoding="utf8") as file:
    result = []
    last_line = ' '
    for i in file:
        if i.startswith('def ') and not last_line.startswith('#'):
            result.append(i[4:i.find('(')])
        last_line = i

    if len(result):
        print(*result, sep='\n')
    else:
        print('Best Programming Team')