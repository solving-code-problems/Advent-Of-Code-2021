import math


def poly(steps):
    pair_count = {}
    rule_map = {}

    with open('input', 'r') as f:
        template, rules = f.read().split("\n\n")

        for rule in rules.split("\n"):
            pair, char = rule.split(" -> ")
            rule_map[pair] = char

        for i in range(len(template) - 1):
            pair = template[i] + template[i + 1]
            if pair not in pair_count:
                pair_count[pair] = 1
            else:
                pair_count[pair] += 1

        for step in range(steps):

            insertions = []
            for pair in pair_count:
                if pair in rule_map:
                    number_of = pair_count[pair]
                    char = rule_map[pair]
                    left = pair[0] + char
                    right = char + pair[1]

                    insertions.append((left, right, number_of))
                    pair_count[pair] -= number_of

            for i in insertions:
                left, right, number_of = i
                if left in pair_count:
                    pair_count[left] += number_of
                else:
                    pair_count[left] = number_of
                if right in pair_count:
                    pair_count[right] += number_of
                else:
                    pair_count[right] = number_of

        char_count = {}
        for key, val in pair_count.items():
            left, right = key[0], key[1]
            if left in char_count:
                char_count[left] += val
            else:
                char_count[left] = val
            if right in char_count:
                char_count[right] += val
            else:
                char_count[right] = val

        for key, val in char_count.items():
            char_count[key] = math.ceil(val / 2)

        max_n, min_n = -math.inf, math.inf
        for key, val in char_count.items():
            max_n = max(max_n, val)
            min_n = min(min_n, val)

        return max_n - min_n


print(f'Part one {poly(10)}')
print(f'Part two {poly(40)}')
