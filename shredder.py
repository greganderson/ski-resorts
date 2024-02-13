from abc import ABC
from enum import Enum


class Skill(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"


class Shredder(ABC):
    def __init__(self, name: str, boot_size: int, skill: Skill):
        self.name = name
        self.boot_size = boot_size
        self.skill = skill


class Skier(Shredder):
    def __init__(self, name: str, boot_size: int, skill: Skill, has_poles: bool):
        super().__init__(name=name, boot_size=boot_size, skill=skill)
        self.has_poles = has_poles
    
    def __str__(self) -> str:
        skill = f"a {self.skill.name.lower()}" if self.skill == Skill.BEGINNER else f"an {self.skill.name.lower()}"
        uses_poles_str = "uses poles" if self.has_poles else "doesn't use poles"
        return f"{self.name} the skier is {skill} that {uses_poles_str}"

class Snowboarder(Shredder):
    def __init__(self, name: str, boot_size: int, skill: Skill, is_goofy: bool):
        super().__init__(name=name, boot_size=boot_size, skill=skill)
        self.is_goofy = is_goofy

    def __str__(self) -> str:
        skill = f"a {self.skill.name.lower()}" if self.skill == Skill.BEGINNER else f"an {self.skill.name.lower()}"
        is_goofy_str = f"is goofy" if self.is_goofy else "regulary"
        return f"{self.name} the snowboarder is {skill} that {is_goofy_str}"


def skill_to_enum(skill_str: str) -> Skill:
    return list(filter(lambda skill: skill.value == skill_str, Skill))[0]