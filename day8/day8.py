def seven_segment_search_pt1():
    with open('input', 'r') as f:
        unique_length = 0
        for line in f.readlines():
            output = line.split("|")[1].strip().split(" ")
            for part in output:
                if len(part) in [2, 4, 3, 7]:
                    unique_length += 1
        return unique_length


def seven_segment_search_pt2():
    digit_lookup = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    sum_of_numbers = 0
    with open("input", 'r') as f:
        for line in f.readlines():
            segments, output = line.split("|")
            lookup = {}
            result = {}
            for part in segments.split(" "):
                if len(part) in [2, 3, 4, 7]:
                    lookup[digit_lookup[len(part)]] = part
                    result[part] = digit_lookup[len(part)]

            for part in segments.split(" "):
                if len(part) == 5:
                    overlaps_with_one = len(set(part).intersection(lookup[1]))
                    overlaps_with_4 = len(set(part).intersection(lookup[4]))
                    if overlaps_with_one == 2:
                        result[part] = 3
                    if overlaps_with_4 == 2:
                        result[part] = 2
                    if overlaps_with_4 == 3 and overlaps_with_one == 1:
                        result[part] = 5

                if len(part) == 6:
                    overlaps_with_one = len(set(part).intersection(lookup[1]))
                    overlaps_with_4 = len(set(part).intersection(lookup[4]))
                    if overlaps_with_one == 1:
                        result[part] = 6
                    elif overlaps_with_4 == 4:
                        result[part] = 9
                    elif overlaps_with_4 == 3 and overlaps_with_one == 2:
                        result[part] = 0
            numbers = []

            for out in output.strip().split(" "):
                for k, v in result.items():
                    if len(k) == len(out):
                        if len(set(k).intersection(set(out))) == len(out):
                            numbers.append(str(v))
                            break

            sum_of_numbers += int("".join(numbers))
    return sum_of_numbers


print(f'Part one: {seven_segment_search_pt1()}')
print(f'Part two: {seven_segment_search_pt2()}')
