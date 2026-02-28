import json
from pydantic import BaseModel, Field
from models import CodingSession

class JournalManager(BaseModel):
        sessions : list[CodingSession]  = Field(default_factory=list)

        def add_session(self, new_session : CodingSession):
            self.sessions.append(new_session)

        def save_to_file(self, filename : str = 'journal.json'):
            data_to_save = [session.model_dump(mode="json") for session in self.sessions]
            with open(filename, 'w') as f:
                  json.dump(data_to_save , f, indent=4)

        def load_from_file(self, filename : str = 'journal.json'):
            try:
                with open(filename, 'r') as f:
                    raw_data = json.load(f)
                    self.sessions = [CodingSession(**item) for item in raw_data]
            except FileNotFoundError:
                 print("No existing journal found. Starting with an empty journal.")

        def get_stats(self) -> dict:
            if not self.sessions:
                return {"total_minutes": 0, "average_energy": 0}
            total_minutes = sum(session.duration_minutes for session in self.sessions)
            average_energy = sum(session.energy_level for session in self.sessions) / len(self.sessions)
            return {
                "total_minutes": total_minutes,
                "average_energy": average_energy
            }
        
if __name__ == "__main__":
       print("This module defines the JournalManager model and is not meant to be run directly.")