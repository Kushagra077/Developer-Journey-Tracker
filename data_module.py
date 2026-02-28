import json
from pydantic import BaseModel, Field
from datetime import date

class CodingSession(BaseModel):
        date : date
        duration_minutes : int = Field(gt=0)
        energy_level : int = Field(ge=1, le=10)

class JournalManager(BaseModel):
        sessions : list[CodingSession]  = Field(default_factory=list)

        def add_session(self, new_session : CodingSession):
            self.sessions.append(new_session)

        def save_to_file(self, filename : str = 'journal.json'):
            data_to_save = [session.model_dump(mode="json") for session in self.sessions]
            with open(filename, 'w') as f:
                  json.dump(data_to_save , f, indent=4)


if __name__ == "__main__":
       manager = JournalManager()
       session1 = CodingSession(date = date.today() , duration_minutes = 120, energy_level = 10)
       manager.add_session(session1)
       print(manager.sessions)
       manager.save_to_file()