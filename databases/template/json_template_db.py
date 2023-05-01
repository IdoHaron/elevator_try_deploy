from databases.template.templates_db import TemplatesDB
from pathlib import Path
from json import load
from dacite import from_dict
from utils.data_types.single_line_design import LineDesign
from utils.data_types.template import Template
from databases.json_db import JsonDB


class JsonTemplatesDB(TemplatesDB, JsonDB):
    def __init__(self, path_to_db: Path):
        self._data = {}
        super().__init__(path_to_db)

    def _load_db(self):
        with self.database_path.open("r") as f:
            _data = load(f)
        print(self.database_path)
        self._data = _data
        # for template in _data:
        #     lines = []
        #     for line in template["lines"]:
        #         lines.append(from_dict(LineDesign, line))
        #     self._data[template] = Template(_data[template], lines)
        # self._data = _data

    def get_encoding(self, template_name: str) -> str:
        print(template_name)
        return self._data[template_name]


    def __dict__(self):
        self._data.copy()

    def get_all_templates(self):
        return self._data.keys()