def number_game(mobile_number):
    result = ""
    i = 0

    while i < len(mobile_number):
        current_sum = 0
        current_state = int(mobile_number[i]) % 2  # Check initial state (odd or even)

        while (
            i < len(mobile_number)
            and (current_sum + int(mobile_number[i])) % 2 == current_state
        ):
            current_sum += int(mobile_number[i])
            i += 1

        result += str(current_sum)

    return result


mobile_number = input("Enter a mobile number: ")
output = number_game(mobile_number)
print("Concatenated result:", output)