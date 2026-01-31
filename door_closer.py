# Generates all of the commands needed to make a Slab Door close.

# Gathers all needed information and modifies it

bottom_corner = input("What are the coordinates for the bottom corner? ")
top_corner = input("What are the coordinates for the top corner? ")
file = input("What is the file to edit to? ")

bottom_x, bottom_y, bottom_z = bottom_corner.split(" ")
top_x, top_y, top_z = top_corner.split(" ")

bottom_x = int(bottom_x)
bottom_y = int(bottom_y)
bottom_z = int(bottom_z)
top_x = int(top_x)
top_y = int(top_y)
top_z = int(top_z)

# Generates all of the commands and writes them to the given file.
center_coords = f"{(bottom_x + top_x) // 2} {(bottom_y + top_y) // 2} {(bottom_z + top_z) // 2}"
sound_string = f"execute positioned {center_coords} run playsound minecraft:block.piston.extend block @p ~ ~ ~ 2"

with open(file, 'w') as file:
    for i in range(6):
        file.write(f"{sound_string}\n")

        if i == 0:
            coords_2 = f"{bottom_x} {top_y} {bottom_z} {top_x} {top_y} {top_z}"
            # file.write(f"fill {bottom_x} {bottom_y} {bottom_z} {top_x} {bottom_y + 1} {top_z} barrier\n")
            # Commented this line out, could potentially be useful for some maps if left uncommented
        elif i == 1:
            coords_1 = f"{bottom_x} {top_y} {bottom_z} {top_x} {top_y} {top_z}"
            coords_2 = f"{bottom_x} {top_y - 1} {bottom_z} {top_x} {top_y - 1} {top_z}"
        elif i == 3:
            coords_1 = f"{bottom_x} {top_y - 1} {bottom_z} {top_x} {top_y} {top_z}"
            coords_2 = f"{bottom_x} {bottom_y} {bottom_z} {top_x} {bottom_y} {top_z}"
        elif i == 5:
            coords_1 = f"{bottom_x} {bottom_y} {bottom_z} {top_x} {top_y} {top_z}"

        if i > 0:
            file.write(f"fill {coords_1} ")
            if i % 2 == 0:
                file.write("red_sandstone\n")
            else:
                file.write("iron_block\n")

        if i % 2 == 0:
            file.write(f"fill {coords_2} red_sandstone_slab[type=top]\n")

        if i != 5:
            file.write("\n")