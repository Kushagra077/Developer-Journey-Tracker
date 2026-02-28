import pytest
from models import CodingSession
from manager import JournalManager
from visualizer import plot_energy
from datetime import date

def test_add_session():
    manager = JournalManager()
    session = CodingSession(date=date.today(), duration_minutes=60, energy_level=5)

    manager.add_session(session)

    assert len(manager.sessions) == 1
    assert manager.sessions[0].duration_minutes == 60
    assert manager.sessions[0].energy_level == 5

def test_get_stats_calculation():
    manager = JournalManager()
    manager.add_session(CodingSession(date=date.today(), duration_minutes=100, energy_level=10))
    manager.add_session(CodingSession(date=date.today(), duration_minutes=50, energy_level=6))

    stats = manager.get_stats()

    assert stats["total_minutes"] == 150
    assert stats["average_energy"] == 8.0

# def test_plot_energy():
#     manager = JournalManager()
#     manager.add_session(CodingSession(date=date.today(), duration_minutes=100, energy_level=10))
#     manager.add_session(CodingSession(date=date.today(), duration_minutes=50, energy_level=6))

#     plots = plot_energy(manager.sessions)

#     assert "duration_over_time" in plots
#     assert "energy_over_time" in plots
#     assert "duration_vs_energy" in plots