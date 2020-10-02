from dataclasses import dataclass, field
from typing import List

from app.models.wohnung import Wohnung


@dataclass(unsafe_hash=True)
class Studentenwohnheim(object):
    wohnungen: List[Wohnung] = field(default_factory=lambda: list())

    def __iter__(self):
        return iter(self.wohnungen)
