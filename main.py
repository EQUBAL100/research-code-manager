
def calculate_average(values):
    if not values:
        raise ValueError("The list cannot be empty")

    return sum(values) / len(values)


def calculate_summary(values):
    if not values:
        raise ValueError("The list cannot be empty")

    return {
        "count": len(values),
        "average": calculate_average(values),
        "minimum": min(values),
        "maximum": max(values),
        "range": max(values) - min(values),
    }


if __name__ == "__main__":
    measurements = [10.2, 10.5, 9.8, 10.1, 10.4]

    summary = calculate_summary(measurements)

    print(f"Number of measurements: {summary['count']}")
    print(f"Average: {summary['average']:.2f}")
    print(f"Minimum: {summary['minimum']:.2f}")
    print(f"Maximum: {summary['maximum']:.2f}")
    print(f"Range: {summary['range']:.2f}")
