def room_area():
    length = float(input("Enter the length of the room in meters: "))
    width = float(input("Enter the width of the room in meters: "))
    print(f"The area is {length * width} in square meters and "
          f"{length * width * 10.7639:.2f} in square feet")
    
room_area()