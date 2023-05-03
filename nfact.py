import random


with open("file.txt", "r") as file:
    data = file.read().lower()
    

bigrams = {}
for i in range(len(data)-1):
    current = data[i]
    next_char = data[i+1]
    if current in bigrams:
        if next_char in bigrams[current]:
            bigrams[current][next_char] += 1
        else:
            bigrams[current][next_char] = 1
    else:
        bigrams[current] = {next_char: 1}


for current in bigrams:
    total = sum(bigrams[current].values())
    for next_char in bigrams[current]:
        bigrams[current][next_char] /= total


def generate_name():
    current = random.choice(list(bigrams.keys()))
    name = current
    while True:
        if current in bigrams:
            next_char = random.choices(list(bigrams[current].keys()), list(bigrams[current].values()))[0]
            name += next_char
            current = name[-1]
        else:
            break
    return name


for current in bigrams:
    for next_char in bigrams[current]:
        print(f"{current} -> {next_char}: {bigrams[current][next_char]}")
