# FiXiT 
Loom video: https://www.loom.com/share/4196048c3b4944fbad774d79f3e52784

FastAPI application for lead prioritization and call evaluation.

## How to Run Locally

### Prerequisites
- Python 3.11+
- pip

### Setup
```bash
pip install -r requirements.txt
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`

## How to Run via Docker

### Build the Docker image:
```bash
docker build -t fixit-genai-assignment .
```

### Run the container:
```bash
docker run -p 8000:8000 fixit-genai-assignment
```

## API Testing

### Interactive Documentation
Visit `http://localhost:8000/docs` for Swagger UI to test all endpoints.

### Example Commands

**Lead Priority:**
```bash
curl -X POST "http://localhost:8000/api/v1/lead-priority" \
  -H "Content-Type: application/json" \
  -d '[{
    "lead_id": "lead_001",
    "source": "website",
    "budget": 500000,
    "city": "Mumbai",
    "property_type": "apartment",
    "last_activity_minutes_ago": 30,
    "past_interactions": 2,
    "notes": "Interested in 2BHK",
    "status": "new"
  }]'
```

**Call Evaluation:**
```bash
curl -X POST "http://localhost:8000/call-eval" \
  -H "Content-Type: application/json" \
  -d '{
    "call_id": "call_001",
    "lead_id": "lead_001", 
    "transcript": "Hello, I am interested in buying a 2BHK apartment in Mumbai",
    "duration_seconds": 300
  }'
```

## Model Selection & Architecture

### Model Used: Mistral
- **Why**: Lightweight, fast inference, good for production deployment
- **Alternative**: OpenAI GPT models considered but require API keys and external dependencies

### Trade-offs Made

**Performance vs Accuracy:**
- Used rule-based scoring for lead prioritization (fast, predictable)
- Fallback responses for call evaluation when model unavailable
- Prioritized response time over complex ML models

**Simplicity vs Features:**
- Minimal dependencies (4 packages only)
- Basic error handling vs comprehensive validation
- Static scoring vs dynamic learning models

**Deployment vs Development:**
- Docker containerization for easy deployment
- No database persistence (stateless API)
- Environment-agnostic configuration
