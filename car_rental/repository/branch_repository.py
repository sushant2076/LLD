from typing import Dict, Optional

from car_rental.model.branch import Branch


class BranchRepository:
    def __init__(self):
        self._branch_map: Dict[str, Branch] = {}

    def add_branch(self, branch: Branch) -> None:
        self._branch_map[branch.id] = branch

    def get_branch(self, id: str) -> Optional[Branch]:
        return self._branch_map.get(id)
