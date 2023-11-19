"""Functions for the Sandbox module."""

def dollarizer(word):
    """Replace all 's' characters with '$'."""
    replacement = '$'
    return word.replace('s', replacement)

def eurizer(word):
    """Replace all 'e' characters with '€'."""
    replacement = '€'
    return word.replace('e', replacement)

def replace(word, replacee, replacement):
    """Replace all instances of replacee with replacement."""
    return word.replace(replacee, replacement)

def wonky_text(word):
    """Replace all 's' characters with '$' and all 'e' characters with '€'."""
    word = dollarizer(word)
    word = eurizer(word)
    word = replace(word, 'e', '€')
    word = replace(word, 'l', '£')
    return word

def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def age_in_days(age):
    """Convert an age in years to an age in days."""
    return age * 365

def simple_interest(principal, interest_rate, years):
    """Calculate simple interest."""
    return principal * interest_rate * years

def plan_finances(principal, interest_rate, years, desired_final_amount):
    """Determine if a financial plan will work."""
    current_amount = principal
    for year in range(years):
        current_amount = simple_interest(current_amount, interest_rate, 1)
        current_amount += principal
    return current_amount >= desired_final_amount

print("Dollarizer: ", dollarizer("testcase"))
print("Eurizer: ", eurizer("testcase"))
print("Replace: ", replace("testcase", "t", "T"))
print("Wonky Text: ", wonky_text("testcase lucy"))
print("Celsius to Fahrenheit: ", celsius_to_fahrenheit(20))
print("Age in Days: ", age_in_days(20))
print("Simple Interest: ", simple_interest(100, 0.05, 1))
print("Plan Finances: ", plan_finances(100, 0.05, 1, 200))
