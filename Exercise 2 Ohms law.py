def ohms_law_calculator():
    print("Ohm's Law Calculator")
    print("1. Calculate Current")
    print("2. Calculate Voltage")
    print("3. Calculate Resistance")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        voltage = float(input("Enter voltage: "))
        resistance = float(input("Enter resistance: "))
        try:
            current = voltage / resistance
            print(f"Current: {current: .2f} A")
        except ZeroDivisionError:
            print("Please change your value.")

    elif choice == 2:
        current = float(input("Enter current: "))
        resistance = float(input("Enter resistance: "))
        try:
            voltage = current * resistance
            print(f"Voltage: {voltage: .2f} V")
        except ZeroDivisionError:
            print("Please change your value.")

    elif choice == 3:
        voltage = float(input("Enter voltage: "))
        current = float(input("Enter current: "))
        try:
            resistance = voltage / current
            print(f"Resistance: {resistance: .2f} ohms")
        except ZeroDivisionError:
            print("Please change your value.")

    else:
        print("Invalid choice")


ohms_law_calculator()