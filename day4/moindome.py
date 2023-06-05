# my_name = "giorgi"

# if "g" in my_name:
#     print("sheicavs k-s")
# my_name = "gio"
# my_surname = "goletiani"
# my_pet_name = "miki"



# my_sentence = "aa {2} bb {0} cc {1}".format(my_name, my_pet_name, my_surname)


# print(my_sentence)

# name1 = "gio"
# name2 = "goletiani"
# name3 = "23"

# name4 = "me var {} chemi gvaria {} chemi asakia {}".format(name1, name2, name3)

# print(name4)

# my_name = "giorgi"

# if "i" in my_name:
#     print("nayiini nayini")
# else:
#     print("ar sheicavs")


#input
#output

# my_age = 22

# my_age += 3

# name1 = input("enter your name: ")
# name2 = input("enter your usarname: ")
# name3 = input("enter your age: ")

# print("my name is {} my usarname is {} my age is {}".format(name1, name2, name3))

# new_age = int(name3) + 3

# name3 = "after 3 years i am now {} years old".format(new_age)


# print(name3)

# nam1 = int(input("enter your answer: "))
# nam2 = int(input("enter your answer2: "))

# product = nam1 * nam2
# if product > 100:
#     print(product)
# else:
#     print("you loose")

#print(20 % 6)       # % aris nashtis chveneba 3*6= 18 20-18=2

# nika = "gio"
# nika += "123"      # += nishnavs inkrementacia anu damateba cvladis 

# print(nika)    

# input, %, if, +=  gamoyenebit gavaketot amocana 
    

                            # even - luwi  odd - kenti


# nam1 = int(input("take your bet: "))
# nam2 = int(input("take your bet2: "))
# nam3 = int(input("take your bet3: "))

# nam1 += (35 % 4)
# nam2 += (25 % 3)
# nam3 += (13 % 2)

# product = (nam1, nam2, nam3)
 
# print(product)
# name1 = input("enter your name1: ")
# name2 = input("enter your name2: ")

#  shevqmnat ori sainkrementacio cvladi

# ammount_of_vowels_in_name1 = 0
# ammount_of_vowels_in_name2 = 0

# giorgi   # nika

# for char in name1:
#     if char in "aeiou":
#         ammount_of_vowels_in_name1 += 1
# for char in name2:
#     if char in "aeiou":
#         ammount_of_vowels_in_name2 += 1

# if ammount_of_vowels_in_name1 > ammount_of_vowels_in_name2:
#     print("the ammount of vowels in name 1 is more and it contains {} vowels".format(ammount_of_vowels_in_name1))
# elif ammount_of_vowels_in_name1 < ammount_of_vowels_in_name2:
#     print("the ammount of vowels in name 2 is more and it contains {} vowels".format(ammount_of_vowels_in_name2))
# else:
#     print("they have equal of vowels")


# nam1 = input("enter some txt: ")

# ammount_of_a = 0

# for char in nam1:
#     if char == "a":
#         ammount_of_a += 1

# print('there is {} "a" in my text'.format(ammount_of_a))


# num = 12
# if num > 51:
#     print("bigger than 5")
#     if num <= 47:
#         print("between 5 and 47")


num1 = input("enter your name: ")
num2 = input("enter your name2: ")

numbers_of_consonants_in_num1 = 0
numbers_of_consonants_in_num2 = 0


for char in num1:
    if char in "bgdvztiklmno":
        numbers_of_consonants_in_num1 += 1
for char in num2:
    if char in "bgdvztiklmno":
        numbers_of_consonants_in_num2 += 1

if numbers_of_consonants_in_num1 > numbers_of_consonants_in_num2:
    print("the nombers in consonants in num1 is more and it contains {}".format(numbers_of_consonants_in_num1))
elif numbers_of_consonants_in_num1 < numbers_of_consonants_in_num2:
    print("the nombers in consonants in num2 is more and it contains {}".format(numbers_of_consonants_in_num2))
else:
    print("its not worked")
    



