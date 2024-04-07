import random

def random_walk(start, moves):
    position = start
    for x in range(moves):
        step = random.choice([-1, 1])
        position += step
        yield position

# Example:
for position in random_walk(0, 100):
    final_position = position
print(f"Final position after 100 moves:", final_position)