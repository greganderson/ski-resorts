from abc import ABC
from enum import Enum


class TreeDensity(Enum):
    NONE = "none"
    SOME = "some"
    LOTS = "lots"

class SlopeRating(Enum):
    GREEN_CIRCLE = "green_circle"
    BLUE_SQUARE = "blue_square"
    BLACK_DIAMOND = "black_diamond"
    ORANGE = "orange"


class Run(ABC):
    def __init__(self, name: str, slope_rating: SlopeRating, tree_density: TreeDensity):
        self.name = name
        self.slope_rating = slope_rating
        self.tree_density = tree_density
    
    def __str__(self) -> str:
        return f"The {self.name} slope has a rating of {' '.join(self.slope_rating.value.split('_'))} with a tree density of {self.tree_density.value}"


class GreenCircle(Run):
    def __init__(self, name: str, tree_density: TreeDensity):
        super().__init__(name=name, slope_rating=SlopeRating.GREEN_CIRCLE, tree_density=tree_density)

class BlueSquare(Run):
    def __init__(self, name: str, tree_density: TreeDensity, has_moguls: bool):
        super().__init__(name=name, slope_rating=SlopeRating.BLUE_SQUARE, tree_density=tree_density)
        self.has_moguls = has_moguls

class BlackDiamond(Run):
    def __init__(self, name: str, tree_density: TreeDensity, has_moguls: bool, has_cliffs: bool):
        super().__init__(name=name, slope_rating=SlopeRating.BLUE_SQUARE, tree_density=tree_density)
        self.has_moguls = has_moguls
        self.has_cliffs = has_cliffs

class Orange(Run):
    def __init__(self, name: str, num_rails: int, small_jumps: int, medium_jumps: int, large_jumps: int):
        super().__init__(name=name, slope_rating=SlopeRating.ORANGE, tree_density=TreeDensity.NONE)
        self.num_rails = num_rails
        self.small_jumps = small_jumps
        self.medium_jumps = medium_jumps
        self.large_jumps = large_jumps


slope_rating_to_class: dict[SlopeRating, Run] = {
    SlopeRating.GREEN_CIRCLE.value: GreenCircle,
    SlopeRating.BLUE_SQUARE.value: BlueSquare,
    SlopeRating.BLACK_DIAMOND.value: BlackDiamond,
    SlopeRating.ORANGE.value: Orange,
}

def tree_density_to_enum(tree_density_str: str) -> TreeDensity:
    return list(filter(lambda density: density.value == tree_density_str, TreeDensity))[0]