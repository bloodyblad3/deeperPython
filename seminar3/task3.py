def find_combinations(items, max_weight):
    def helper(i, current_combination, current_weight):
        if current_weight == 0 or i == len(items):
            combinations.append(current_combination)
            return

        if items[i][1] <= current_weight:
            helper(i + 1, current_combination + [items[i]], current_weight - items[i][1])

        helper(i + 1, current_combination, current_weight)

    combinations = []
    helper(0, [], max_weight)

    return combinations

items = [
    ("Item1", 2),
    ("Item2", 5),
    ("Item3", 3),
    ("Item4", 1)
]

max_weight = 6

valid_combinations = find_combinations(items, max_weight)
for combination in valid_combinations:
    print(combination)
