def convert_number_list_to_decimal(number_list):
    number = 0
    for index, bit in enumerate(reversed(number_list)):
        number += bit << index
    return number


def binary_diagnostic_pt1():
    with open('input.txt', 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
        number_of_lines = len(lines)
        bits = len(lines[0])
        gama = [0] * bits
        epsilon = [0] * bits
        for index in range(bits):
            zeros = 0
            for line in lines:
                if line[index] == '0':
                    zeros += 1
            if zeros > number_of_lines // 2:
                gama[index] = 0
                epsilon[index] = 1
            else:
                gama[index] = 1
                epsilon[index] = 0

        return convert_number_list_to_decimal(gama) * convert_number_list_to_decimal(epsilon)


def binary_diagnostic_pt2():
    with open('input.txt', 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]
        co2_ratings = lines[:]
        oxy_ratings = lines[:]

        def zeros_or_ones_at_position(index, ratings):
            zero_count = 0
            for rating in ratings:
                if rating[index] == '0':
                    zero_count += 1
            return zero_count, len(ratings) - zero_count

        position = 0
        while len(oxy_ratings) != 1:
            zeros, ones = zeros_or_ones_at_position(position, oxy_ratings)
            if zeros > ones:
                oxy_ratings = list(filter(lambda rating: rating[position] == '0', oxy_ratings))
            else:
                oxy_ratings = list(filter(lambda rating: rating[position] == '1', oxy_ratings))
            position += 1

        position = 0
        while len(co2_ratings) != 1:
            zeros, ones = zeros_or_ones_at_position(position, co2_ratings)
            if zeros > ones:
                co2_ratings = list(filter(lambda rating: rating[position] == '1', co2_ratings))
            else:
                co2_ratings = list(filter(lambda rating: rating[position] == '0', co2_ratings))
            position += 1

        oxy_rating_binary_number = [int(char) for char in oxy_ratings[0]]
        co2_rating_binary_number = [int(char) for char in co2_ratings[0]]

        return convert_number_list_to_decimal(oxy_rating_binary_number) * convert_number_list_to_decimal(
            co2_rating_binary_number)


print(f'Part one: {binary_diagnostic_pt1()}')
print(f'Part one: {binary_diagnostic_pt2()}')
