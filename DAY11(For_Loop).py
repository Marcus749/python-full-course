# DAY 11 – For Loop 



# # 1 Basic Loop
# for i in range(1,11):
#     print(i)


# # 2 Print Characters
# word="Python"

# for alphabet in word:
#     print(alphabet)

# word2 = "SQL"
# for j in range(1,11):
#     print(word2)




# # 3 Loop through list
# items = ["Pen", "Book", "Laptop"]
# for item  in items:
#     print(item)


# 4️ Even numbers
# print("Print Odd Numbers :")
# for n in range(1, 21, 2):
#     print(n)

# 5️ Total calculation
# marks = [78, 82, 90,95,65,78,65]
# total = 0
# for m in marks:
#     total += m
# print("Total:", total)


# 6️ Clean city names
# cities = ["  MUMbai", "pune  ", "  CHENNAI"]
# cleaned = []
# for c in cities:
#     cleaned.append(c.strip().title())
# print(cleaned)



# 7️ Loop with If Condition
# nums = [5, 12, 3, 18, 7]
# for n in nums:
#     if n > 10:
#         print(n, "is greater than 10")
#     else:
#         print(n," is not greater than 10")


# # 8 Loop with If Condition
# nums = [5, 12, 3, 18, 7]
# for n in nums:
#     if n % 2==0:
#         print(n, "- Even Number")
#     else:
#         print(n,"- Odd Number")

# 9 Extract last digits from IDs
# ids = ["EMP-001122", "EMP-889900"]
# for last4 in ids:
#     print(last4[-5:])