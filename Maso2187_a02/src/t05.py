"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""


# Imports

# Constants


found_length = float(input("Foundation length (m): "))
found_width = float(input("Foundation width (m): "))
found_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_rate = float(input("Cost of concrete ($/m^3): "))
bricks_rate = float(input("Cost of bricks ($/m^2): "))

concrete_for_foundation = found_length * found_width * found_height
cost_of_concrete = concrete_for_foundation * concrete_rate
bricks_for_walls = (found_length * wall_height * 2) + (found_width * wall_height * 2)
cost_of_bricks = bricks_for_walls * bricks_rate
total_cost = cost_of_concrete + cost_of_bricks

print()
print(f"Concrete needed for foundation (m^3): {concrete_for_foundation:.2f}")
print(f"Cost of concrete: ${cost_of_concrete:.2f}")
print(f"Bricks needed for walls (m^2): {bricks_for_walls:.2f}")
print(f"Cost of bricks: ${cost_of_bricks:.2f}")
print(f"Total cost: ${total_cost:.2f}")

