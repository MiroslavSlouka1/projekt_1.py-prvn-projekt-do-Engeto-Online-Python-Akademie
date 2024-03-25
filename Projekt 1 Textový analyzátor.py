"""
první projekt do Engeto Online Python Akademie

author: Miroslav Slouka
email: miroslav.slouka@kitron.com
discord: mirek_63517

"""

TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

length_words = []

used_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

print("$ python projekt1.py")

username = input("Insert username: ")
password = input("Insert password: ")
print("-" * 40)

if username in used_password and (used_password[username]) == password:
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("-"*40)
else:
    print("unregistered user, terminating the program..")
    exit()

select_text = input("Enter a number btw. 1 and 3 to select: ")
print("-"*40)
if select_text in ("1", "2", "3"):
    index = int(select_text)-1
else:
    print("Bad number, terminating the program.. ")
    exit()

select = TEXTS[index]
words = select.split()

titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_numbers = 0

for word in words:
    length_words.append(len(word))
    if word.istitle():
        titlecase_words += 1

    caplet = 0
    for letter in word:               # rozdeli slovo na pismena
        if letter.isupper():          # porovna jestli je pismeno velke
            caplet += 1
            if caplet == len(word):   # porovna pocet velkych pismen s delkou slova
                uppercase_words += 1

    if word.islower():
        lowercase_words += 1

    if word.isnumeric():
        numeric_strings += 1
        sum_numbers += int(word)

print("There are "+str(len(words))+" words in the selected text.")
print("There are "+str(titlecase_words)+" titlecase words.")
print("There are "+str(uppercase_words)+" uppercase words.")
print("There are "+str(lowercase_words)+" lowercase words.")
print("There are "+str(numeric_strings)+" numeric strings.")
print("The sum of all the numbers "+str(sum_numbers))
print("-"*40)

print("LEN|   OCCURENCES   |NR.")
print("-" * 40)
for order in range(1, max(length_words)+1):
    stars = 0
    for number in length_words:
        if order == number:
            stars += 1
    if order < 10:
        space = "  "
    else:
        space = " "
    print(space+str(order)+"|"+"*"*stars+" "*(16-stars)+"|"+str(stars))
