from enum import Enum

class ServerState(Enum):
    DOWN = 0
    SLEEP = 1
    UP = 2

def string_to_select_entry(wanted_string_to_convert:str)-> str:
    return f"<option value={wanted_string_to_convert}> {wanted_string_to_convert}</option>\n"

def start_select_entry(select_name:str, select_id:str="")->str:
    if select_id == "":
        return f"<select value={select_name} id={select_name}>\n"
    return f"<select value={select_name} id={select_id}>\n"

def end_select_entry():
    return "</select>\n"
