""" --- Day 11: Monkey in the Middle ---
--- Part One ---
https://adventofcode.com/2022/day/11
"""

monkeys = []


def main():
    with open('input') as input_observations:

        observations = []

        for line in input_observations:
            if line != '\n':
                observations.append(line)
            else:
                monkeys.append(parse_monkey(observations))
                observations = []
        # Otherwise last monkey will be lost
        monkeys.append(parse_monkey(observations))

        for i in range(20):
            for monkey in monkeys:
                monkey.inspect_inventory()

        inspect_scores = []
        for monkey in monkeys:
            inspect_scores.append(monkey.inspect_counter)
            print(monkey)

        inspect_scores.sort(reverse=True)
        print(inspect_scores)
        print(inspect_scores[0] * inspect_scores[1])


def parse_monkey(observations):
    name = observations[0].split(':')[0]
    items = [int(x) for x in eval('[' + observations[1].split(':')[1] + ']')]
    operation = observations[2].split('=')[1].strip()
    test = int(observations[3].split('by')[1].strip())
    if_pass = int(observations[4].split('monkey')[1].strip())
    if_fail = int(observations[5].split('monkey')[1].strip())
    return Monkey(name, items, operation, test, if_pass, if_fail)


class Monkey:

    def __init__(self, name, items, operation, test, if_pass, if_fail):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_pass = if_pass
        self.if_fail = if_fail
        self.inspect_counter = 0

    def inspect_inventory(self):
        while len(self.items) > 0:
            self.inspect_counter += 1
            old = self.items.pop(0)
            new = int(eval(self.operation) / 3)
            if new % self.test == 0:
                monkeys[self.if_pass].items.append(new)
            else:
                monkeys[self.if_fail].items.append(new)

    def __str__(self):
        return self.name + ' (Score: ' + str(self.inspect_counter) + ')\n' + \
            '  ' + str(self.items) + '\n' \
            '   Operation: ' + str(self.operation) + '\n' \
            '   Test: mod ' + str(self.test) + ': -> ' + str(self.if_pass) + ' | ' + str(self.if_fail)


if __name__ == "__main__":
    main()
