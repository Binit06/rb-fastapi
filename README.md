# Project Title

FastAPI Project with MongoDB performing CRUD || Multi-Query Using Data Pipeline

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Examples](#examples)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

* Python 3.x
* Virtualenv (optional)
* Docker

### Installation

A step by step series of examples that tell you how to get a development env running:

1. Clone the repository:

```bash
git clone https://github.com/Binit06/FastAPI.git
```

2. Navigate to the project directory:

```bash
cd FastAPI
```

3. Create a virtual environment (optional):

```bash
python -m venv myvenv
source myvenv/Scripts/activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

5. Setting up Database in Docker:

```bash
docker-compose up
```

## Usage

1. Run the Project:

```bash
uvicorn app.main:app --reload
```

Now you are free to use the APIs

### Examples

1. Register a new user: POST
```
http://127.0.0.1:8000/user/register/
```
Body
```
{
    "username": "Binit",
    "email": "binittrial@gmail.com",
    "hashed_password": "anyrandompassword"
}
```

Response:
```
{
    "message": "User registered Succesfully",
    "user_id": str
}
```

2. Link an ID with the existing user: POST
```
http://127.0.0.1:8000/user/link-id/
```
Body:
```
{
    "user_id": {user_id}
    "linked_id": "https://github.com/Binit06"
}
```

Response:
```
{
    "message": "ID Linked Succesfully"
}
```

3. Authentication of an User: GET
```
http://127.0.0.1:8000/auth/login/?email={email}&password={password}
```

Response:
```
{
    "message": "Login Successful",
    "user_id": str
}
```

4. Creating a Post: POST

```
http://127.0.0.0:8000/post/add/{some_user_id}/
```
Body:
```
{
    "title": "This will be the title of the Post",
    "content": "This will be the content of the Post"
}
```

Response:
```
{
    "message": "Post created successfully",
    "post_id": str
}
```

5. Get all details about the User: GET
```
http://127.0.0.1:8000/join/joined-data/{user_id}/
```

Response: 
```
{
    _id: ObjectId,
    username: str,
    email: str,
    user_posts: Array[],
    linked_data: Array[]
}
```

6. Remove Each and Every detail about the User: DELETE
```
http://127.0.0.1:8000/delete/users/{user_id}/
```

Response:
```
{
    "message": str
}
```

7. Get an user by UserId: GET
```
URL: http://127.0.0.1:8000/user/user/{user_id}/
```

8. Get an user by Email: GET
```
URL: http://127.0.0.1:8000/user/user_email/?email={email}/
```

9. Get all Users: GET
```
URL: http://127.0.0.1:8000/user/all_users/
```

10. Get a post By PostId: GET
```
URL: http://127.0.0.1:8000/post/{post_id}/
```
