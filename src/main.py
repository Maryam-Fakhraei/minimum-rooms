def ClassesPerHour(schedule):
    # Initialize A List To Store The Number Of Classes Per Hour .
    classes_per_hour = [0] * 25

    # Iterate Through Each Hour And Count The Number Of Classes .
    for hour in range(25):
        for start, end in schedule:
            if hour >= start and hour < end:
                classes_per_hour[hour] += 1

    return classes_per_hour

def main():
    # Read In The Class Schedule From File .
    schedule = []
    path = f"{__file__}\\..\\class_schedule.txt"
    with open(path, "r") as file:
        for line in file:
            start, end = line.strip().split("..")
            schedule.append((int(start), int(end)))

    classes_per_hour = ClassesPerHour(schedule)
    print(classes_per_hour)

if __name__ == "__main__":
    main()