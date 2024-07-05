# n = int(input("Enter the range =\t"))
# participant1 = [i for i in range(1, n + 1)]
# participant2 = [i for i in range(1, n + 1, 2)]
# i = 1
# while len(participant2) != 1:
#     if len(participant2) > i:
#         del participant2[i]
#         i += 1
#     else:
#         i = 1

# print(participant2)

# participant3 = [i for i in range(1, n + 1, 4)]
# participant4 = [i for i in range(1, n + 1, 8)]
# participant5 = [i for i in range(1, n + 1, 12)]


# print(participant1, "\n", len(participant1), "\n")
# print(participant2, "\n", len(participant2), "\n")
# print(participant3, "\n", len(participant3), "\n")
# print(participant4, "\n", len(participant4), "\n")
# print(participant5, "\n", len(participant5), "\n")


# participant1 = [i for i in range(1, n + 1, 2)]
# participant2 = [i for i in range(1, n + 1, 4)]
# participant3 = [i for i in range(1, n + 1, 6)]
# participant4 = [i for i in range(1, n + 1, 8)]
# participant5 = [i for i in range(1, n + 1, 9)]
# participant5 = [i for i in range(1, n + 1, 11)]

# print(participant5, "\n", len(participant5), "\n")

# print(participant1)
# print(participant2)
# print(participant3)
# print(participant4)
# print(participant5)


def josephus_survivor(num_people):
    # Creating a list of people numbered from 1 to num_people
    people = list(range(1, num_people + 1))

    # Index to track the current person in the circle
    current_index = 0

    # Continue the elimination until only one person remains
    while len(people) > 1:
        # Eliminate the next person
        del people[current_index]

        # Move to the next person (after elimination)
        current_index = (current_index + 1) % len(people)

    # Return the survivor
    return people[0]


# Example with 100 people
num_people = 100
survivor = josephus_survivor(num_people)
print(f"The survivor in the game with {num_people} people is person {survivor}.")
