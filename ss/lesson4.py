# palindrom function
# def is_palidrom(word: str) -> bool:
#     return word == word[::-1]
# print(is_palidrom('tot'))


# def count_unique_item(word: str) -> int:
#     tmp = ''
#     s = 0
#     for i in word:
#         if i in tmp:
#             continue
#         s += 1
#         tmp += i
#     return s
#
# print(count_unique_item('Hello'))


# def make_sentence(*args):
#     result = ""
#     for i in args:
#         result += i + " "
#     return result.rstrip()
#
#
# print(make_sentence("Hello", "World", "Hi"))


# def make(*args):
#     return " ".join(args)
#
#
# print(make("Hello", "World", "Hi"))

# replace -> almashtirish uchun s.replace('h', 's') bunda h di s ga almashtir deyapti


# 103

# n = int(input())
# lis = list(map(int, input().split()))
# a, b = map(int, input().split())
# s = 0
# for i in range(a, b + 1):
#     s += lis[i - 1]
# print(f"{s / (b - a + 1):.1f}")

# lis = [1, 2, 3, 4, 5, 6, 7]
# """
# 0 - 1
# 1 - 2
# 2 - 3
# """


# def same_first_last(nums):
#     if len(nums) > 1 and nums[0] == nums[-1]:
#         return True
#     return False
#
#
#
# print(same_first_last([1, 2, 3, 4, 6, 1]))

# def common_end(a, b):
#     if len(a) > len(b):
#         return True
#     return False
# common_end([1, 2, 3], [2]) → False
#
# print(common_end([1, 2, 3], [7, 3]))
# from decimal import Decimal, getcontext, ROUND_HALF_UP
#
# getcontext().rounding = ROUND_HALF_UP
# input()
# nums = list(map(int, input().split()))
# a, b = map(int, input().split())
# minNum = min(nums)
# for i in range(a - 1, b):
#     nums[i] = nums[i] / minNum
# for i in nums:
#     print(f"{Decimal(i):.1f}", end=' ')


# n = int(input())
# lis = list(map(int, input().split()))
# a, b = map(int, input().split())
# s = 0
# k = 0
# for i in range(0, n):
#     if i < a - 1 or i > b - 1:
#         s += lis[i]
#         k += 1
# print(f"{s / k:.2f}")


# n = int(input())
# lis = list(map(int, input().split()))
# a, b = map(int, input().split())
# s = 0
# for i in range(a, b + 1):
#     s += lis[i - 1]
# print(f"{s / (b - a + 1):.1f}")

# todo matrix dan eng kop qatnashgan sondi topish
# matrix = [
#     [1, 2, 3, 2, 4, 5],
#     [6, 1, 2, 3, 5, 6],
#     [1, 3, 1, 1, 2, 3],
#     [4, 2, 6, 5, 3, 1]
# ]
#
# element_count = {}
#
# for row in matrix:
#     for element in row:
#         if element in element_count:
#             element_count[element] += 1
#         else:
#             element_count[element] = 1
#
# most_common_element = None
# max_count = 0
#
# for element, count in element_count.items():
#     if count > max_count:
#         most_common_element = element
#         max_count = count
#
# print(f"Eng ko'p uchragan element: {most_common_element}, {max_count} marta.")

# todo eng uzun sozdi topish index qaytaradi
# s = "python dasturlash tili"
# words = s.split()
# longest_word = max(words, key=len)
# s1 = len(longest_word)
#
# print(s1)

# todo eng uzun sozdi topish
# s = "python dasturlash tili"
# words = s.split()
# longest_word = max(words, key=len)
# print(longest_word)


# todo 1 marta takrorlangan elementni topish listdan
# def test(s):
#     return [x for x in s if s.count(x) == 1]
#
#
# l = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# result = test(l)
# print(result)


# todo fibanachi son
# def fibonacci(n):
#     if n <= 0:
#         return "Noto'g'ri son kiritildi"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#
#     a, b = 0, 1
#     for _ in range(2, n):
#         a, b = b, a + b
#     return b
#
#
# n = int(input())
# print(fibonacci(n))


# 0,1,1,2.3, 5, 8
# 0 + 1 = 1 + 1,2+1 =


# l = [1, 2, 3, 4, 5]
#
# l.pop(1)
# print(l)


# todo listdan n songacha bolgan elementlarni ochirish
# l = [1, 2, 3, 4, 5]
# n = int(input())
# del l[n:]
# print(l)


###################




