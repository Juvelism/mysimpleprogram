def calculate_love_score(name1, name2):
    word = "true"
    checked = []
    total_count = 0

    for letter in word:
        if letter not in checked:
            count = name1.count(letter)
            total_count += count
            times = "time" if count == 1 else "times"
            print(f"{letter.upper()} occurs {count} {times}")
    print(f"Total = {total_count}")

calculate_love_score("Kanye West", "Kim Kardashian")

