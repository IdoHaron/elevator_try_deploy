from dataclasses import dataclass
from utils.data_types.fonts import Fonts
from typing import Tuple


@dataclass()
class LineDesign:
    font: Fonts
    Size: int
    color: Tuple[int, int, int]
    cords: Tuple[int, int]

 #TODO(Ido): decide if cords in LineDesign or in Template