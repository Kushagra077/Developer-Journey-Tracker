from pydantic import BaseModel, Field
from datetime import date

class CodingSession(BaseModel):
        date : date
        duration_minutes : int = Field(gt=0)
        energy_level : int = Field(ge=1, le=10)

class JournalManager(BaseModel):
        sessions : list[CodingSession]  = Field(default_factory=list)

        def add_sessions(self, new_session : CodingSession):
            self.sessions.append(new_session)
                
if __name__ == "__main__":
       manager = JournalManager()
       session1 = CodingSession(date = date.today() , duration_minutes = 120, energy_level = 10)
       manager.add_sessions(session1)
       print(manager.sessions)