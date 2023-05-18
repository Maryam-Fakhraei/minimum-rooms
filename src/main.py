import matplotlib.pyplot as plt
from termcolor import colored

def ClassesPerHour(schedule):
    # Initialize A List To Store The Number Of Classes Per Hour .
    classes_per_hour = [0] * 25

    # Iterate Through Each Hour And Count The Number Of Classes .
    for hour in range(25):
        for start, end in schedule:
            if hour >= start and hour < end:
                classes_per_hour[hour] += 1

    return classes_per_hour

def RoomsNeeded(classes_per_hour):
    # Determine The Maximum Number Of Classes Per Hour .
    max_classes_per_hour = max(classes_per_hour)

    # Determine How Many Rooms Are Needed To Hold Classes .
    rooms_needed = max_classes_per_hour if max_classes_per_hour > 0 else 1

    return rooms_needed

def main():
    # Read In The Class Schedule From File .
    schedule = []
    path = f"{__file__}\\..\\class_schedule.txt"
    with open(path, "r") as file:
        for line in file:
            start, end = line.strip().split("..")
            schedule.append((int(start), int(end)))

    classes_per_hour = ClassesPerHour(schedule)

    rooms_needed = RoomsNeeded(classes_per_hour)

    # Welcome
    print(colored("\n===> Hello, Welcome To This Program <=== \n", "green", attrs=["dark"]))
    # Print Rooms Needed .
    print(colored(f"~.~ {rooms_needed} ~.~", "cyan"))
    # Developers
    print(colored("\nThank You For Choosing Us :)\n>>>Developed By Maryam Fakhraei & Amirhossein Naseri<<<", "magenta", attrs=["dark"]))

    # Plot A Line Graph Of The Number Of Classes Required In eEvery Hour Of The Day And Night .
    fig = plt.figure("Classes Per Hour")
    plt.plot(range(25), classes_per_hour, color = "b", linewidth = 1, linestyle = ":", marker = "*", markersize = 4)
    plt.xlabel("Time", color = "m")
    plt.xticks(range(25), color = "y")
    plt.ylabel("Number Of Classes", color = "m")
    plt.yticks(range(rooms_needed + 1), color = "y")
    plt.title("Maryam Fakhraei & Amirhossein Naseri", color = "g", fontstyle = "oblique" , loc= "left")
    plt.show()

if __name__ == "__main__":
    main()