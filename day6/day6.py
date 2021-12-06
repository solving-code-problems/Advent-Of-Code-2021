def lantern_fish(target):
    day_counter = [0] * 9
    with open('input', 'r') as f:
        days = [int(x.strip()) for x in f.readlines()[0].split(",")]
        for day in days:
            day_counter[day] += 1

        for day in range(target):
            can_reproduce = day_counter[0]

            for i in range(1, len(day_counter)):
                day_counter[i - 1] = day_counter[i]
            day_counter[6] += can_reproduce
            day_counter[8] = can_reproduce
        return sum(day_counter)


print(f'Part one: {lantern_fish(80)}')
print(f'Part two: {lantern_fish(256)}')
