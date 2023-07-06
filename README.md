# Social Networking Application RESTful API

This is a simple RESTful API for a social networking application built within FastAPI. It allows users to authenticate, register, create, edit, delete, and view posts, as well as like or dislike other users' posts.

## Getting Started

To get started with the API, follow these instructions.

### Prerequisites

Make sure you have the following software installed on your machine:

- preferable OS - Linux
- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone {<url>}
```
2. Create an ```.env``` file based on your environment and set the required environment variables.



3. Build and run the Docker containers
```bash
docker-compose build --no-cache
docker-compose up
```

These commands will build the FastAPI application container, PostgreSQL database container, and Redis cache container.

4. Wait for the containers to start up. You can check the logs to monitor the progress:
```bash
docker-compose logs -f
```

5. Once the containers are up and running, you can access the API documentation by visiting ```http://<host>:<port>/docs``` in your web browser.


6. To run unit tests, use the following command:
```bash
python -m pytest -s -rP
```

## Usage

### Authentication and Registration

To authenticate or register a user, you can use the following endpoints:

- `POST /register` - Register a new user
- `POST /login` - Authenticate and retrieve a JWT token

### Posts

To manage posts, you can use the following endpoints:

- `GET /posts/{post_id}` - Get a specific post by ID
- `POST /posts` - Create a new post
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post


### Likes and Dislikes

To like or dislike a post, you can use the following endpoints:

- `POST /posts/{post_id}/like` - Like a post
- `POST /posts/{post_id}/dislike` - Dislike a post

Please note that you cannot like or dislike your own posts.

## Technologies Used

- **FastAPI** - Web framework for building the API
- **PostgreSQL** - Relational database for storing user and post data
- **Redis** - In-memory data store for caching
- **Docker** - Containerization platform for easy deployment
- **Docker-Compose** - Tool for defining and running multi-container Docker applications