# Movies API

This is a simple Django project that serves an API for managing movies and their reviews. The project uses Docker for containerization and can be easily set up using Docker Compose.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.9 or later.

### Running the Project

1. Clone the repository:

```sh
git clone https://github.com/Dpancha6/django-coding-challenge.git
cd coding_challenge
```

2. Build and start the Docker containers:

```sh
docker compose build
docker compose up
```

3. Run database migrations:

```sh
docker compose run --rm django python manage.py makemigrations
docker compose run --rm django python manage.py migrate
```

4. The API will be available at `http://localhost:8080`.

5. The project includes a List API for Movies at `localhost:8080/api/movies`.


### API Endpoints

- **List Movies**: `GET /api/movies/`
- **Create Movie**: `POST /api/movies/`
- **Detail Movie**: `GET /api/movies/<id>/`
- **Update Movie**: `PUT /api/movies/<id>/`
- **Partial Update Movie**: `PATCH /api/movies/<id>/`
- **Delete Movie**: `DELETE /api/movies/<id>/`
- **Create Review**: `POST /api/movies/reviews/`

6. **Added a Detail View for Movies**:
   - Querying `GET /api/movies/1` would return the Movie with `id: 1`.
   - Allow `PUT`, `PATCH`, `DELETE` on `/api/movies/<id>` as well.

7. **Added a New Field to the API: `runtime_formatted`**:
   - Returns the runtime as a string in the format `H:MM`.
   - A runtime of 142 minutes should have a `runtime_formatted` of `2:22`.

8. **Added a Second Model for Reviews**:
   - Many-to-one related to Movies.
   - Include fields for the reviewer's name and rating out of 5 stars.

9. **Added Reviews to Both the List and Detail Movie Views**:
   - Include the whole model, not just an ID reference.

10. **Added a New Field to the API: `avg_rating`**:
   - Returns the average rating of a movie by all the reviewers.
   - A Movie with 4 reviewers, who each gave the Movie 2, 2, 3, and 4 stars would result in an `avg_rating` of 2.75.

11. **Added Query Parameters to the List View**:
   - Allows filtering on the runtime.
   - It should be possible to filter for either longer or shorter than the input.

#### Example:
   
   - Movies with runtime greater than 120 minutes: `GET /api/movies/?runtime=>120`
   - Movies with runtime less than 150 minutes: `GET /api/movies/?runtime=<150`
