# # 1
# def biggie(arr):
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             arr[i] = 'big'
#     return arr
# print(biggie([-1, 3, 5, -5]))

# # 2
# def countPositives(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             count += 1
#     arr[-1] = count
#     return arr
# print(countPositives([-1,1,1,1]))

# # 3
# def sumArr(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum
# print(sumArr([1,2,3,4]))

# # 4
# def average(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum / len(arr)
# print(average([1,2,3,4]))


# # 5
# def length(arr):
#     return len(arr)
# print(length([37,2,1,-9]))

# 6
# def minimum(arr):
#     min = arr[0]
#     if len(arr) == 0:
#         return False
#     for i in arr:
#         if i < min:
#             min = i
#     return min
# print(minimum([37,2,1,-9]))

# # 7
# def maximum(arr):
#     max = arr[0]
#     if len(arr) == 0:
#         return False
#     for i in arr:
#         if i > max:
#             max = i
#     return max
# print(maximum([37,2,1,-9]))

# # 8
# def analysis(arr):
#     dic = {'sumTotal': 0, 'average': 0, 'minimum': arr[0], 'maximun': arr[0], 'length': len(arr)}
#     for i in arr:
#         if dic['minimum']<i:
#             dic['minimum'] = i
#         if dic['maximun']>i:
#             dic['maximun'] = i
#         dic['sumTotal']+= i
#         dic['average']=dic['sumTotal']/len(arr)
#     return dic
# print(analysis([37,2,1,-9]))

# # 9
# def reversed(arr):
#     for i in range(0, (len(arr)-1)//2):
#         temp = arr[i]
#         arr[i] = arr[len(arr)-1-i]
#         arr[len(arr)-1-i] = temp
#     return arr
# print(reversed([37,2,1,-9]))