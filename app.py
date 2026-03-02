from flask import Flask, request
from manager import JournalManager
from models import CodingSession
from pydantic import ValidationError

app = Flask(__name__)

manager = JournalManager()

@app.route('/')
def welcome():
    return "Welcome to the Developer Journey Tracker."

@app.route('/stats')
def show_stats():
    stats = manager.get_stats()
    return stats

@app.route('/add', methods=['POST'])
def add_session():
    data = request.json
    try:
        new_session = CodingSession(**data)
        manager.add_session(new_session)
        return {"message": "Session added successfully."}, 201
    except ValidationError as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)