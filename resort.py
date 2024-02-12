import json


def create_skier(name: str, boot_size: float, skill: str, has_poles: bool) -> dict:
    return {
        "name": name,
        "boot_size": boot_size,
        "skill": skill,
        "has_poles": has_poles
    }

def create_snowboarder(name: str, boot_size: float, skill: str, is_goofy: bool) -> dict:
    return {
        "name": name,
        "boot_size": boot_size,
        "skill": skill,
        "is_goofy": is_goofy
    }

def create_green_circle(name: str, trees: str) -> dict:
    return {
        "name": name,
        "difficulty": "green circle",
        "trees": trees
    }

def create_blue_square(name: str, trees: str, has_moguls: bool) -> dict:
    return {
        "name": name,
        "difficulty": "blue square",
        "trees": trees,
        "has_moguls": has_moguls
    }

def create_black_diamond(name: str, trees: str, has_moguls: bool, has_cliffs: bool) -> dict:
    return {
        "name": name,
        "difficulty": "black diamond",
        "trees": trees,
        "has_moguls": has_moguls,
        "has_cliffs": has_cliffs
    }

def create_orange(name: str, num_rails: int, small_jumps: int, medium_jumps: int, large_jumps: int) -> dict:
    return {
        "name": name,
        "difficulty": "orange",
        "num_rails": num_rails,
        "small_jumps": small_jumps,
        "medium_jumps": medium_jumps,
        "large_jumps": large_jumps
    }

def create_resort(name: str, shredders: dict, runs: dict) -> dict:
    return {
        "name": name,
        "shredders": shredders,
        "runs": runs
    }


def main():
    # Resorts
    resorts = []

    # Park City

    # Shredders

    # Skiers
    skiers = []
    skiers.append(create_skier("Greg", 11.5, "intermediate", True))
    skiers.append(create_skier("Bailey", 8.0, "expert", False))

    # Snowboarders
    snowboarders = []
    snowboarders.append(create_snowboarder("Ryan", 10.5, "expert", False))
    snowboarders.append(create_snowboarder("Gabe", 13.0, "intermediate", True))

    shredders = {
        "skiers": skiers,
        "snowboarders": snowboarders
    }

    # Runs
    green_circle = []
    blue_square = []
    black_diamond = []
    orange = []

    green_circle.append(create_green_circle("Homerun", "none"))
    green_circle.append(create_green_circle("Rose Bud", "some"))

    blue_square.append(create_blue_square("Hawkeye", "some", False))
    blue_square.append(create_blue_square("Red Fox", "lots", True))

    black_diamond.append(create_black_diamond("Fool's Gold", "lots", False, True))
    black_diamond.append(create_black_diamond("Belmont", "lots", True, True))

    orange.append(create_orange("Giant Steps", 8, 6, 4, 1))

    runs = {
        "green_circle": green_circle,
        "blue_square": blue_square,
        "black_diamond": black_diamond,
        "orange": orange
    }

    resort = create_resort("Park City", shredders, runs)
    resorts.append(resort)
    resort_json = json.dumps(resort, indent=4)
    print(resort_json)

    with open("park_city.json", "w") as f:
        f.write(resort_json)



    # Brighton

    # Shredders

    # Skiers
    skiers = []
    skiers.append(create_skier("Izzy", 8.0, "expert", True))
    skiers.append(create_skier("Cooley", 10.5, "intermediate", True))

    # Snowboarders
    snowboarders = []
    snowboarders.append(create_snowboarder("Colby", 12.0, "intermediate", False))
    snowboarders.append(create_snowboarder("Mathew", 8.5, "intermediate", False))

    shredders = {
        "skiers": skiers,
        "snowboarders": snowboarders
    }

    # Runs
    green_circle = []
    blue_square = []
    black_diamond = []
    orange = []

    green_circle.append(create_green_circle("Deer Park", "none"))
    green_circle.append(create_green_circle("Sunshine", "some"))

    blue_square.append(create_blue_square("Ziggy", "some", False))
    blue_square.append(create_blue_square("Pine Martin", "lots", True))

    black_diamond.append(create_black_diamond("Doyle's Dive", "lots", False, True))
    black_diamond.append(create_black_diamond("Desperado", "lots", True, True))

    orange.append(create_orange("Park 1", 8, 6, 4, 1))

    runs = {
        "green_circle": green_circle,
        "blue_square": blue_square,
        "black_diamond": black_diamond,
        "orange": orange
    }

    resort = create_resort("Brighton", shredders, runs)
    resorts.append(resort)
    resort_json = json.dumps(resort, indent=4)
    print(resort_json)

    with open("brighton.json", "w") as f:
        f.write(resort_json)


    with open("resorts.json", "w") as f:
        f.write(json.dumps(resorts, indent=4))




if __name__ == "__main__":
    main()
