def calculate_average(values):
    if not values:
        raise ValueError("The list cannot be empty")

    return sum(values) / len(values)


if __name__ == "__main__":
    measurements = [10.2, 10.5, 9.8, 10.1, 10.4]
    average = calculate_average(measurements)
    print(f"Average measurement: {average:.2f}")