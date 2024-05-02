import datetime

current_age = int(input("What is your age? "))
retire_age = int(input("At what age would you like to retire? "))
current_year = datetime.datetime.now().year
retire_year = current_year + (retire_age - current_age)

print(f"It's {current_year}. You will retire in {retire_year}. "
      f"You have only {retire_age - current_age} years of word to go!")