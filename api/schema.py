# api/schema.py
from pydantic import BaseModel

class InputData(BaseModel):
    CreditScore: int
    Geography: int  # e.g., encoded as 0=France, 1=Spain, etc.
    Gender: int      # e.g., 0=Male, 1=Female
    Age: int
    Balance: float
