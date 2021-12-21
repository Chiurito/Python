# this expression takes 2 parameters (first name and last name).
# strip() delete the spaces
# title() capitalize first letter and put the rest in lower case

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print("Hello " + full_name(input("First Name: "), input("Last Name: ")))
