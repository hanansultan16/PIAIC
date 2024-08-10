#1. Simple Messages
message = "Hello World"
print(message)

#2. Simple Messages
message = "Hello Hanan"
print(message)
message = "Hello Hanan Sultan"
print(message)

#3. Personal Message
personal = "Hello Hamza, Would you like to learn some python today?"
print(personal)

#4. Name Cases
name = "Hanan Sultan"
print(name.upper())
print(name.lower())
print(name.title())

#5. Famous Quote
quote = "Tom Fitzgerald said, \"If you can dream it, you can do it\""
print(quote)

#6. Famouse Quote 2
famous_person = "Theodore Roosevelt"
quote2 = f'{famous_person} once said, "Believe you can and you\'re halfway there."'
print(quote2)

#7. Stripping Names
name = "\tHanan Sultan\n"
#with whitespace
print(name)
#with lstrip
print(name.lstrip())
#with rstrip
print(name.rstrip())
#with strip
print(name.strip())


#8. Variable Sum
x = 5
y = 10
z = 15
print(x + y + z)

#9. Variable Swap
a = 25
b = 50
#Before Swap
print(f"a = {a}, b = {b}")
#After Swap
a, b = b, a
print("a =", a, "b =", b)


#10. Favorite Colour
favorite_color = "Yellow"
#Before changing the variable name
print(favorite_color)
my_color = favorite_color
#After changing the variable name
print(my_color)


#11. Pet Name
pet_name = "Buddy"
print(pet_name)
pet_name = "Max"
print(pet_name)


#12. Observing Name Error
weather = "Sunshine"
print(weather)
# Wrong
print(sunsine) 
#Output: NameError: name 'sunsine' is not defined


#13. Reassigning Score
score = 100
print(score)
score = 200
print(score)


#14. City Name
city = "Lahore"
print(city)


#15. Title Case Text
text = "Python Programming"
print(text.title())


#16. Lowercase Conversion
mixed = "PyThOn iS ThE fuTUrE"
print(mixed.lower())


#17. Uppercase Conversion
mixed = "PyThOn iS ThE fuTUrE"
print(mixed.upper())


#18. Current Temperature
temperature = 35
print(f"The current temperature is {temperature} degrees.")


#19. Printing a Poem
poem = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""
print(poem)

