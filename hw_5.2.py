filename = "test.txt"

with open(filename, "r") as f:
    lines = f.readlines()
    num_lines = len(lines)
    num_words = 0
    for line in lines:
        words = line.split()
        num_words += len(words)
        print(f"Количество слов в строке: {len(words)}")

    print(f"Количество строк: {num_lines}")
    print(f"Количество слов: {num_words}")