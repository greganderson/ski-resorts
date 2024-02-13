from collections import defaultdict
import json

from run import Run, SlopeRating, TreeDensity, slope_rating_to_class, tree_density_to_enum
from resort_class import Resort
from shredder import Skill, Skier, Snowboarder, skill_to_enum


filename = "resorts.json"


def parse_skiers(skiers: list[dict]) -> list[Skier]:
    result = []
    for skier in skiers:
        skier["skill"] = skill_to_enum(skier["skill"])
        result.append(Skier(**skier))
    return result

def parse_snowboarders(snowboarders: list[dict]) -> list[Snowboarder]:
    result = []
    for snowboarder in snowboarders:
        snowboarder["skill"] = skill_to_enum(snowboarder["skill"])
        result.append(Snowboarder(**snowboarder))
    return result

def parse_runs(runs: dict) -> dict:
    result = defaultdict(list)
    for rating, run_list in runs.items():
        for run in run_list:
            run_info = {k: v for k, v in run.items() if k != "slope_rating"}
            
            # Orange doesn't have tree density
            if "tree_density" in run:
                tree_density = tree_density_to_enum(run["tree_density"])
                run_info["tree_density"] = tree_density

            run_class = slope_rating_to_class[rating]
            result[rating].append(run_class(**run_info))
    return result
    
def parse_resort(resort_dict: dict) -> Resort:
    skiers = parse_skiers(resort_dict["shredders"]["skiers"])
    snowboarders = parse_snowboarders(resort_dict["shredders"]["snowboarders"])

    shredders = {
        "skiers": skiers,
        "snowboarders": snowboarders
    }

    runs = parse_runs(resort_dict["runs"])

    return Resort(name=resort_dict["name"], shredders=shredders, runs=runs)

def main():
    print()
    with open(filename, "r") as f:
        resorts_list = json.loads(f.read())
    
    # This will hold all the resorts as classes
    resorts: list[Resort] = []

    print("Parsing resorts...")

    for resort_dict in resorts_list:
        resorts.append(parse_resort(resort_dict))
    
    print("Done parsing resorts")

    resorts[0].add_run(Run(name="Greg's Slope", slope_rating=SlopeRating.BLACK_DIAMOND, tree_density=TreeDensity.LOTS))
    resorts[0].add_shredder(Snowboarder(name="Dove", boot_size=9.5, skill=Skill.INTERMEDIATE, is_goofy=True))
    
    shredders = resorts[0].get_shredder_lists()
    for skier in shredders["skiers"]:
        print(skier)
    for snowboarder in shredders["snowboarders"]:
        print(snowboarder)

    resorts[0].close_resort()
    print(f"{resorts[0].name} is now closed")



if __name__ == "__main__":
    main()