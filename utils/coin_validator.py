from pydantic import BaseModel
from typing import List, Tuple


class WeeklyData(BaseModel):
    """Classs for storing Weekly high and low coin"""

    weekly_high: List[int]
    weekly_low: List[int]
