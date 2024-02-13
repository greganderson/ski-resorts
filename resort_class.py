from run import Run
from shredder import Shredder, Skier, Snowboarder


class Resort:
    def __init__(self, name: str, shredders: dict[Shredder], runs: dict[Run]):
        self.name = name
        self.shredders = shredders
        self.runs = runs
    
    def add_shredder(self, shredder: Shredder) -> None:
        if isinstance(shredder, Skier):
            self.shredders["skiers"].append(shredder)
        elif isinstance(shredder, Snowboarder):
            self.shredders["snowboarders"].append(shredder)

    def add_run(self, run: Run) -> None:
        self.runs[run.slope_rating.value].append(run)
    
    def get_shredder_lists(self) -> dict[str, Shredder]:
        return self.shredders.copy()
    
    def list_runs(self) -> list[Shredder]:
        return self.shredders.copy()
    
    def close_resort(self) -> None:
        self.shredders.clear()