'''
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"

'''


def name_shuffle(name):
    name = name.split(" ")
    firstName, lastName = name[0], name[1]
    return lastName + " " + firstName


print(name_shuffle("Rosie O'Donnell"))
