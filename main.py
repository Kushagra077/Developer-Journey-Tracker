from models import CodingSession
from manager import JournalManager
from datetime import date
from pydantic import ValidationError
from visualizer import plot_energy

manager = JournalManager()
manager.load_from_file()
try:
    duration_minutes = int(input("Enter duration of coding session in minutes: "))
    energy_level = int(input("Enter your energy level during the session (1-10): "))

    new_session = CodingSession(date=date.today(), duration_minutes=duration_minutes, energy_level=energy_level)

except (ValueError, ValidationError) as e:
    print(f"Invalid input: {e}")

else:
    manager.add_session(new_session)
    manager.save_to_file()

stats = manager.get_stats()
print(f"Total coding minutes: {stats['total_minutes']}")
print(f"Average energy level: {stats['average_energy']:.2f}")

show_graph = input("Would you like to see your energy trend? (y/n): ").lower()
if show_graph == 'y':
    plot_energy(manager.sessions)