# todoApplication
basic task tracking application




``` bash
# Install django (only the first time)
pip install django

# Make migrations 
python manage.py makemigrations

# Migrate applications database
python manage.py migrate app
python manage.py migrate user

# Run the server with the following command
python manage.py runserver