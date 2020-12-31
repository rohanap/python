name = "ada lovelace"
print(name)
print(name.title()) 
print(name.upper())
print(name.lower())


first_name = "ada"
last_name = "lovelace"
full_name = first_name+' '+last_name
full_name = f"{first_name} {last_name}"
print(full_name) 

print(f"Hello, {full_name.title()}!")

new_message = f"Hello,{full_name.title()}!"
print(new_message)
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace

favorite_language = "python "
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

favorite_language = " python"
print(favorite_language.lstrip())

print(favorite_language.strip())
