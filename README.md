# Install Python, 3.10.11 is the version in which the project was developed so it is also the recommended version:
>> https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

# Find the installation location, if you installed it in the default location it should be something like:
>> C:\Users\{your_user}\AppData\Local\Programs\Python\Python310

# Add Python to Path environment variables:
>> C:\Users\{your_user}\AppData\Local\Programs\Python\Python310\Scripts
>> C:\Users\{your_user}\AppData\Local\Programs\Python\Python310

# Install the virtualenv library using pip in a terminal.
>> pip install virtualenv

# In the terminal, run the code below:
>> python -m venv venv

# After installing the library, run:
>> venv\Scripts\activate
>> pip freeze > pip install -r requirements.txt

#(optional) Update the pip:
>> python.exe -m pip install --upgrade pip

# To start the server run:
>> python manage.py runserver

############################################################

Super user: admin
Super user password: admin123
