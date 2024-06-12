## Installation

# Clone the repository

git clone <repository_url>
cd <repository_directory>

# Setup virtual env

python3 -m venv env
source env/bin/activate

# Install packages
pip install -r requirements.txt


### Application usage

# To run the application and start server
python app.py

# Interatct and send requests manually from cmd or postman

# POST      
curl -X POST -H "Content-Type: application/json" -u admin:password -d '{"username": "john_doe", "email": "john@example.com", "password": "securepassword"}' http://localhost:5000/users

# GET       
curl -u admin:password http://localhost:5000/users/1

# PUT       
curl -X PUT -H "Content-Type: application/json" -u admin:password -d '{"email": "john_new@example.com", "password": "newpassword"}' http://localhost:5000/users/1

# DELETE   
curl -X DELETE -u admin:password http://localhost:5000/users/1


### Automate testing files

# Install pytest
pip install pytest

# Run tests
pytest

