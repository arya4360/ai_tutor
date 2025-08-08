# AI Tutor

AI Tutor is a pet project designed to build a scalable, asynchronous backend using FastAPI. The project focuses on implementing features like user management, database integration, WebSocket communication, and observability while following best practices for modern backend development.

## Project Goals
- Build a robust backend using FastAPI.
- Implement asynchronous database operations with SQLAlchemy and PostgreSQL.
- Enable WebSocket communication for real-time features.
- Integrate observability tools like Prometheus and Grafana.
- Follow a structured 28-day learning and development plan.

## Features Implemented So Far
1. **FastAPI Setup**:
   - Basic FastAPI application with `/` and `/health` endpoints.
   - Modular structure for scalability.

2. **User Management**:
   - Pydantic models for request/response validation.
   - CRUD operations for users using SQLAlchemy.

3. **Database Integration**:
   - PostgreSQL database integration using SQLAlchemy (async).
   - Alembic for database migrations.

4. **Logging**:
   - Integrated Logfire for centralized logging.

5. **Environment Configuration**:
   - `.env` file for managing environment variables securely.

## Project Structure
```
ai_tutor/
├── app/
│   ├── api/                # API route definitions
│   │   └── user_routes.py  # User-related endpoints
│   ├── core/               # Core utilities and configurations
│   │   ├── config.py       # Application settings
│   │   ├── database.py     # Database setup and session management
│   │   └── logging.py      # Logfire logging setup
│   ├── models/             # Data models
│   │   ├── database_models.py  # SQLAlchemy models
│   │   └── user.py         # Pydantic models for user
│   ├── repositories/       # Data access layer
│   │   └── user_repository.py  # User repository for DB operations
│   ├── main.py             # FastAPI application entry point
│   └── .env                # Environment variables
├── alembic/                # Database migrations
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
└── README.md               # Project documentation
```

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai_tutor
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```env
   LOGFIRE_API_KEY=your_logfire_key
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_SERVER=localhost
   POSTGRES_PORT=5432
   POSTGRES_DB=your_database_name
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Next Steps
- Implement WebSocket communication for real-time features.
- Add JWT authentication for secure endpoints.
- Integrate Prometheus and Grafana for observability.
- Containerize the application using Docker.

## Learning Plan
The project follows a structured 28-day learning plan, focusing on different aspects of backend development each day. Refer to `ai_tutor_Backend_28Day_Prep_Plan.csv` for detailed steps and milestones.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.
