# #  STRING METHODS (VERY IMPORTANT)

# text1="       hello python learner       "

# #Remove Spaces

# print("Orignal text:", text1)
# print("Remove spaces:", text1.strip())


# #Covert to capital letters
# print("Capital Letters :", text1.upper().strip())

# #Covert to proper case
# print("Proper Letters :", text1.title().strip())

# #Covert to Lower case
# print("Lower Letters :", text1.lower().strip())

# #Replace
# print("Replace python word with SQL",text1.replace("python","SQL"))

# #Coutn occurrences of a letter of word
# print("Count of o", text1.count("o"))


# # Check if text start with something
# print("Start with hello?", text1.strip().startswith("hello"))

# # Check if only numbers are presents in data
# mobile="9876543210"
# print("Is numeric:", mobile.isnumeric())


msg="Welcome to Python Course"


# #Split string into list of words
# words=msg.split()
# print("Word list : ", words)

# #Join back with hyphen
# joined_text="-".join(words)
# print("Joined text:", joined_text)

# # Find position of letter
# print("Index of P :",msg.find("P"))

# #Extract domain
# email="student@example.com"
# domain = email[email.find("@")+1:]
# print("Domain :", domain)




# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: ₹3500/-" → "3500"
# price_text = "Price: ₹3500/-"
# clean_price = price_text.replace("Price:", "") \
#                         .replace("₹", "") \
#                         .replace("/-", "") \
#                         .strip()
# print("Clean Price:", clean_price)