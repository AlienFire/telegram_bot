from pydantic import BaseModel
from datetime import datetime

class CurrentExchangeRate(BaseModel):
    volute_name: str
    value: str
    date: datetime

    def to_string(self)->str:
        return f'{self.date.strftime("%d-%m-%Y, %H:%M")}\n{self.volute_name}: {self.value}'
