from pathlib import Path
from dataclasses import dataclass
from typing import List
from utils.data_types.single_line_design import LineDesign

@dataclass()
class Template:
    path_to_template:Path
    Lines: List[LineDesign]

