# DataPulse

DataPulse is a data quality monitoring tool that allows users to upload CSV/JSON files, define validation rules, run quality checks that produce a quality score (0-100), generate quality reports, and track quality trends over time through a dashboard.

## Features

- **File Upload:** Upload CSV and JSON data files for validation.
- **Validation Engine:** Define rules (null checks, data type checks, range checks, uniqueness checks).
- **Quality Score:** Computes score as % of rows passing all defined rules.
- **Reporting:** Detailed report generation with per-rule findings.
- **Trend Dashboard:** Visualize aggregate quality metrics over time.
- **Auth System:** JWT-based authentication and authorization.

## Tech Stack

- **Backend:** Python 3.11+ / FastAPI / SQLAlchemy / PostgreSQL / Pydantic
- **Data Processing:** Pandas
- **Testing:** pytest
- **Infrastructure:** Docker / Docker Compose / GitHub Actions CI/CD

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd DataPulse
   ```

2. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the API:**
   - Swagger Documentation: `http://localhost:8000/docs`
   - Root Endpoint: `http://localhost:8000/`

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml` and includes:

- **Linting:** Code style check with `ruff`.
- **Testing:** Automated unit and integration tests with `pytest`.
- **Building:** Docker image build verification.

## Project Structure

- `backend/`: FastAPI application code, models, routers, and business logic.
- `data-engineering/`: Schema definitions, pipelines, and sample data.
- `devops/`: Deployment scripts and environment configurations.
- `qa/`: Test plans, automated test suites, and validation logic.
