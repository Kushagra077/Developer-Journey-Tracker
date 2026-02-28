import json
from pydantic import BaseModel, Field
from datetime import date

class CodingSession(BaseModel):
        date : date
        duration_minutes : int = Field(gt=0)
        energy_level : int = Field(ge=1, le=10)


if __name__ == "__main__":
       print("This module defines the CodingSession model and is not meant to be run directly.")