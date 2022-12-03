with open('input') as input_calories:
    elf_id = 0
    calories_count = [0]
    for line in input_calories:
        if line == '\n':
            elf_id += 1
            calories_count.append(0)
        else:
            calories_count[elf_id] += int(line)
    calories_count.sort(reverse=True)

# Get the top and the top 3 elves from the array
top_elf = calories_count[0]
top_three_elves = calories_count[0] + calories_count[1] + calories_count[2]

# Print the result to console
print("Top elf:", top_elf)
print("Top three elves: ", top_three_elves)
