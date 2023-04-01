filename = "student.txt"
subjects = {}

with open(filename, "r") as f:
    for line in f:
        data = line.strip().split(":")
        subject = data[0]
        classes = data[1].split()
        num_classes = 0
        for c in classes:
            if c.isdigit():
                num_classes += int(c)
        subjects[subject] = num_classes

print(subjects)
