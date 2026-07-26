# Mini Content Engine

A production-style content generation service built with FastAPI and React.

The application accepts a product name, description, and reference image, generates an AI prompt using Ollama, creates a background generation job, and exposes the job status through a REST API.

---

## Tech Stack

### Backend

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Background Tasks
- Repository Pattern
- Service Layer
- Provider-based AI Architecture

### Frontend

- React
- TypeScript
- Vite
- Axios

### AI

- Ollama
- Qwen2.5:3B (local LLM)

---

## Features

- Upload product image
- Generate AI prompt using Ollama
- Background job processing
- Job status polling
- Generated image endpoint
- Modular provider architecture
- Repository + Service pattern
- REST API
- Static image serving

---

## Project Structure

```
mini-content-engine/
│
├── backend/
│   ├── app/
│   ├── uploads/
│   └── requirements.txt
│
└── frontend/
    ├── src/
    └── package.json
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## API Endpoints

### Create Generation Job

```
POST /generate
```

Form Data

| Field | Type |
|--------|------|
| product_name | string |
| description | string |
| image | file |

Returns

```json
{
  "id": "...",
  "status": "pending"
}
```

---

### Get Job Status

```
GET /jobs/{id}
```

Returns

```json
{
  "id": "...",
  "product_name": "...",
  "status": "completed",
  "output_image": "/generated/xxxxx.png"
}
```

---

## Assignment Notes

- Prompt generation uses Ollama running locally.
- Image generation currently uses a mock provider that returns a placeholder image.
- The image provider can be replaced with ComfyUI, Stability AI, or another implementation without changing the application architecture.

---

## Author

Praveenkumar K