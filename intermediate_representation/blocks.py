"""
Used to define Minecraft blocks used in
the intermediate representation.
"""

class Blocks:

    # Done this way in case these need to have
    # specific values.
    REDSTONE_DUST = 0
    REDSTONE_TORCH = 1
    REDSTONE_REPEATER = 2
    REDSTONE_LAMP = 3
    LEVER = 4
    FILLER_BLOCK = 5
    AIR_BLOCK = 6

    BY_KEY = {
        "Redstone Dust":     REDSTONE_DUST,
        "Redstone Torch":    REDSTONE_TORCH,
        "Redstone Repeater": REDSTONE_REPEATER,
        "Redstone Lamp":     REDSTONE_LAMP,
        "Lever":             LEVER,
        "Filler Block":      FILLER_BLOCK,
        "Air Block":         AIR_BLOCK,
    }
