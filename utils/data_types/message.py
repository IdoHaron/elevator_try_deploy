from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    client_origin: str
    time_sent: datetime
