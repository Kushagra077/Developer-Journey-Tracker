import matplotlib.pyplot as plt
from models import CodingSession

def plot_energy(sessions: list[CodingSession]):
    if not sessions:
        print("No data to plot!")
        return

    # 1. Sort sessions by date (essential for a chronological line)
    sorted_sessions = sorted(sessions, key=lambda s: s.date)
    
    # 2. Extract X and Y data
    dates = [s.date for s in sorted_sessions]
    energies = [s.energy_level for s in sorted_sessions]

    # 3. Create the visual
    plt.figure(figsize=(10, 5))
    plt.plot(dates, energies, marker='o', linestyle='-', color='#2ecc71', linewidth=2)
    
    # Formatting for professionalism
    plt.title("Developer Journey: Energy Levels", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Energy Level (1-10)")
    plt.ylim(0, 11) # Keep the scale consistent
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    print("This module defines the plot_energy function and is not meant to be run directly.")