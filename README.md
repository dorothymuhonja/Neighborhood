# Neighborhood

### By Dorothy Muhonja

## Description
An app that keeps the users on the loop about what is going on in their neighborhood

### Set Up Instruction
* Python 3.6 and above
* Editor
* Virtual environment (optional)
*  Django
* SQLAlchemy (Postgres)

## Technologies used
* Python3
* Django
* css3
* html5
* Javascript
* Bootstrap


## Installation and setup
 Clone this repo
 ```
 git clone https://github.com/dorothymuhonja/Neighborhood.git
 ```

 ### Create and activate a virtual environment
 
    virtualenv venv --python=python3

    source venv/bin/activate

### Install django
    pip install django (and other dependencies required)

### Copy environment variable
    cp env.sample .env

### Load/refresh .environment variables
    source .env

### Running the app
```
python3 manage.py runserver
```
## Behaviour Driven Development (BDD)
#### User
* Register an account and log in.
* Choose a neighborhood
* Post news on chosen neighborhod
* Post a business
* Set up your own profile

* Note: A user can only join one neighborhood

#### System Admin
* Can add, change or delete the users and neighborhood admins

### Neighborhood admin
* Can add a business
* Can add content

### Future development
* Add comment for posts



## Email Address
dorothymuhonja7@gmail.com

## License and Copyright

Copyright (c) 2021 Dorothy Muhonja

[MIT License](LICENSE)