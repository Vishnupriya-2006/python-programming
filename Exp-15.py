def calculate_averages():
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0

    while True:
        num = float(input("Enter a number (-1 to stop): "))
        if num == -1:
            break
        elif num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1

    if positive_count > 0:
        positive_avg = round(positive_sum / positive_count, 2)
    else:
        positive_avg = None

    if negative_count > 0:
        negative_avg = round(negative_sum / negative_count, 2)
    else:
        negative_avg = None

    print(f"Average of positive numbers: {positive_avg if positive_avg is not None else 'No positive numbers entered'}")
    print(f"Average of negative numbers: {negative_avg if negative_avg is not None else 'No negative numbers entered'}")

# Run the program
calculate_averages()
