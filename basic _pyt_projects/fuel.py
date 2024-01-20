def fuel_gauge():
    while True:
        try:
            fraction_input = input("Enter a fraction (X/Y): ")
            numerator_str, denominator_str = fraction_input.split('/')
            numerator = int(numerator_str)
            denominator = int(denominator_str)
            if not (isinstance(numerator, int) and isinstance(denominator, int)):
                raise ValueError("Both X and Y must be integers")
            if numerator > denominator or denominator == 0:
                raise ValueError("Invalid fraction, Enter a valid fraction (X/Y)")
            percentage = round((numerator / denominator) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except ValueError as e:
                print(f"Error: {e}")
fuel_gauge()