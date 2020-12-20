import re

with open('input7', 'r') as file:
    data = file.read().splitlines()


bags = {}
bag_count = 0

for line in data:
    color = re.match(r"(.+?) bags contain", line)[1]
    bags[color] = re.findall(r"(\d+?) (.+?) bags?", line)


def has_shiny_gold(color):
    if color == "shiny gold":
        return True
    else:
        return any(has_shiny_gold(c) for _, c in bags[color])


def count_bags(bag_type):
    return 1 + sum(int(number)*count_bags(color) for number, color in bags[bag_type])


for bag in bags:
    if has_shiny_gold(bag):
        bag_count += 1

print("Part 1: " + str(bag_count - 1))
print("Part 2: " + str(count_bags("shiny gold")-1))
