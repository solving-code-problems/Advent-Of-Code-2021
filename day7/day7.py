def trechary_of_wales_pt1():
    with open('input', 'r') as f:
        numbers = [int(x) for x in f.readlines()[0].split(",")]
        sorted_numbers = sorted(numbers)
        median = sorted_numbers[len(numbers) // 2]

        distance = 0
        for i in numbers:
            distance += abs(median - i)
        return distance


def trechary_of_wales_pt2():



    def sum_series(n):
        return n * (n - 1) // 2

    with open('input', 'r') as f:
        numbers = [int(x) for x in f.readlines()[0].split(",")]
        average = round(sum(numbers) // len(numbers))
        total_distance = 0
        for number in numbers:
            cost = sum_series(abs(number - average) + 1)
            total_distance += cost
        return total_distance


print(f'Part one: {trechary_of_wales_pt1()}')
print(f'Part two: {trechary_of_wales_pt2()}')
