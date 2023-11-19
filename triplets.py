name1 = input("Enter the name of the first person: ")
name1_formatted = name1.strip().capitalize()
name2 = input("Enter the name of the second person: ")
name2_formatted = name2.strip().capitalize()
name3 = input("Enter the name of the third person: ")
name3_formatted = name3.strip().capitalize()

print(f"The names are: {name1_formatted}, {name2_formatted}, and {name3_formatted}")

x = input("Give me a number to multiply by 10: ").replace(",", "")

print(float(x) * 10)