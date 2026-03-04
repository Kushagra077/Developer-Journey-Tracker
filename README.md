# Developer Journey Tracker

A Python application for tracking and analyzing your coding sessions, energy levels, and productivity patterns.

## Overview

The Developer Journey Tracker helps you monitor your daily coding habits and well-being. Log your coding sessions with duration and energy levels, then visualize trends over time to understand your work patterns better.

## Features

- **Session Tracking**: Record coding sessions with date, duration (in minutes), and energy level (1-10)
- **Data Persistence**: Sessions are automatically saved to a JSON file for long-term tracking
- **Statistics**: View total coding minutes and average energy levels
- **Visualization**: Generate energy level trend charts to see patterns over time
- **Data Validation**: Input validation using Pydantic ensures data integrity
- **REST API**: Flask-based API for programmatic session management
- **CLI Interface**: User-friendly command-line interface for quick logging

## Project Structure

```
.
├── main.py           # CLI interface for logging sessions and viewing stats
├── app.py            # Flask REST API server
├── manager.py        # JournalManager class for session management
├── models.py         # CodingSession Pydantic model
├── visualizer.py     # Energy trend visualization
├── test_api.py       # Example API testing script
├── journal.json      # Data file (auto-generated)
└── tests/
    ├── __init__.py
    └── test_manager.py
```

## Installation

1. Clone or download the repository
2. Install required dependencies:
   ```bash
   pip install flask pydantic matplotlib requests
   ```

## Usage

### Command Line Interface

Run the CLI to log a new session:

```bash
python main.py
```

You'll be prompted to enter:
- Duration of coding session (in minutes)
- Energy level during the session (1-10)

The application will then display your statistics and offer to show an energy trend chart.

### REST API

Start the Flask API server:

```bash
python app.py
```

The API will run on `http://127.0.0.1:5000` with the following endpoints:

#### `GET /`
Welcome endpoint
```
http://127.0.0.1:5000/
```

#### `GET /stats`
Get aggregated statistics
```
http://127.0.0.1:5000/stats
```
Returns:
```json
{
  "total_minutes": 480,
  "average_energy": 7.5
}
```

#### `POST /add`
Add a new coding session
```
http://127.0.0.1:5000/add
```
Request body:
```json
{
  "date": "2026-03-04",
  "duration_minutes": 120,
  "energy_level": 8
}
```

### Data Models

**CodingSession**
- `date`: Session date (defaults to today)
- `duration_minutes`: Coding duration (must be > 0)
- `energy_level`: Energy level during session (1-10)

## Data Storage

Sessions are stored in `journal.json` in JSON format:

```json
[
    {
        "date": "2026-03-04",
        "duration_minutes": 120,
        "energy_level": 8
    },
    {
        "date": "2026-03-03",
        "duration_minutes": 90,
        "energy_level": 7
    }
]
```

## Testing

Run tests to verify functionality:

```bash
python -m pytest tests/
```

Example API testing:

```bash
python test_api.py
```

## Requirements

- Python
- flask
- pydantic
- matplotlib
- requests

## License

This project is open source and available for personal and educational use.

## Future Enhancements

- Database integration for better scalability
- Advanced analytics and insights
- Weekly/monthly goal tracking
- Productivity tips based on energy patterns
- Web UI dashboard
- Export functionality (CSV, PDF)
