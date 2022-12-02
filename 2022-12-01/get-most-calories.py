
import bisect

max_calories = 0
calories = 0
elves = []

with open ('input-full.txt', 'r') as input:
    data = input.readlines()

calories = 0
for element in data:
    if element := element.rstrip():
        calories += int(element)
        print(f'adding {element} calories, total calories: {calories}')
    else:
        print('-' * 40)
        print(f'current calories {calories}')
        bisect.insort(elves, calories)  # insert into sorted list for part 2 - top 3
        if calories > max_calories:
            max_calories = calories
            print(f'new max calories {max_calories}')
        else:
            print(f'max calories remains {max_calories}')
        calories = 0

# cover for the last value as well
bisect.insort(elves, calories)
if calories > max_calories:
    max_calories = calories

elves.sort(reverse=True)
elves_top3 = elves[:3]
elves_top3_sum = sum(elves_top3)

print('='*40)
print(f'Last calories: {calories}')
print(f'Max calories found: {max_calories}')
print(f'top 3 elves: {elves[:3]}')
print(f'top 3 sum: {elves_top3_sum}')
