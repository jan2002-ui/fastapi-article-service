FastAPI Article Service

1.Problem Understanding & Assumptions
Interpretation
The goal of this service is to aggregate article data from two distinct sources: a legacy SQLite database and an External REST API (JSONPlaceholder). The service provides a unified, validated interface for clients to perform CRUD operations using a high-performance PostgresSQL backend.

Use Case
"AI-Ready Content Aggregator": A backend service that centralizes content from multiple third-party providers, ensuring data is cleaned and validated for downstream consumption.

Assumptions
External API: The third-party service is public and does not require an API key for this assessment.

Data Migration: Ingestion is handled via a dedicated migrate.py script to ensure data is persistent in PostgresSQL before the API serves requests.

Security: As this is an engineering assessment, authentication (JWT) is omitted in favor of demonstrating core API architecture and database reliability.

2.Design Decisions
Database Schema
Used PostgresSQL with an asynchronous driver (asyncpg).

Table articles: Contains id (PK), title (indexed for search), and body.

Async SQLAlchemy: All DB operations are non-blocking to maximize FastAPI's performance.

Project Structure
Followed a Modular Layered Architecture:

app/main.py: API routing and status code management.

app/models.py: Database ORM definitions.

app/schemas.py: Pydantic models for strict Request/Response validation.

app/database.py: Session management and engine configuration.

Validation Logic
Used Pydantic to enforce data types and prevent malformed data from entering the database.

Implemented custom error handling to return 404 Not Found and 422 Unprocessable Entity where appropriate.

3.Solution Approach
Infrastructure: Orchestrated via Docker Compose to ensure the "it works on my machine" guarantee.

ETL Process: The migrate.py script extracts data from external sources, transforms it into internal models, and loads it into PostgresSQL.

REST API: Developed four endpoints (GET, POST, PUT, DELETE) following RESTful best practices.

3.Error Handling & Quality
Resilience: The service is designed to handle database connection delays during startup.

Code Quality: 100% PEP 8 compliance verified via Flake8.

Formatting: Code strictly formatted using Black.

5.How to Run
Setup Environment
Create a .env file based on .env.example:

Code snippet

POSTGRES_USER=postgres
PASSWORD=1234
POSTGRES_DB=article_db
POSTGRES_HOST=db
Execution
Start the containers:

Bash

docker compose up -d --build
Run Data Migration:

Bash

docker exec -it fastapi_app python migrate.py
Run Test Suite:

Bash

docker exec -it fastapi_app pytest test_api.py
Check Code Quality:

Bash

docker exec -it fastapi_app flake8 app --count --statistics
API Documentation
Once running, access the interactive Swagger documentation at: 👉 http://localhost:8000/docs

6.Testing
Integrated Pytest with HTTPX to perform integration tests on:

API Connectivity.

Keyword Search Logic.

Handling of empty result sets.

Final Project Status: Complete
[x] Exactly 4 Endpoints (POST, GET, PUT, DELETE)

[x] External API Integration

[x] PostgresSQL State Management

[x] Dockerized Environment

[x] PEP 8 Compliant