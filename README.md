# simple-Chat-App-using-django 
Simple Chat App using Django
This is a simple chat application built with Django. Users can sign up, log in, view conversations, and chat with other users.

# Features
User registration and authentication
Home page displaying a list of conversations
Chat functionality between users
User profiles with the ability to edit bio and profile picture
# Installation
Clone the repository:


git clone https://github.com/sachin-chaudhray/simple-Chat-App-using-django.git
Navigate to the project directory:


cd simple-Chat-App-using-django
Install the required dependencies. It is recommended to use a virtual environment:

# Create a virtual environment (optional)
python -m venv venv

# Activate the virtual environment
# (Windows)
venv\Scripts\activate
# (Unix or Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
Apply database migrations:

python manage.py migrate
Start the development server:


python manage.py runserver
Open your web browser and visit http://localhost:8000 to access the application.

# Usage
Sign up with a unique username, email, and password.
Log in using your credentials.
On the home page, you can see a list of conversations with other users.
Click on a conversation to enter the chat.
In the chat view, you can see the messages exchanged with the selected user and send new messages.
Navigate to the profile page to view and edit your user profile.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.


# Acknowledgments
The project was inspired by the need for a simple chat application using Django.
Thanks to the Django community for providing excellent documentation and resources.
