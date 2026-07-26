# 🤖 Prompt Engineering Platform (PEP)

A **production-ready Prompt Engineering Platform** that combines prompt management, AI model integration, analytics, testing, authentication, and deployment into one comprehensive web application.

## 🚀 Features

### 🧠 Multi-AI Integration
- OpenAI GPT-4o, GPT-4o-mini, GPT-4 Turbo, GPT-3.5 Turbo
- Extensible architecture for adding more providers

### 📝 Prompt Management
- Create, edit, delete, duplicate, and organize prompts
- Categories: Coding, Marketing, Education, Writing, Summarization, Translation, and more
- Tagging and favoriting system
- Template library

### 🔄 Version Control
- Git-like version history for prompts
- Compare versions with diff visualization
- Restore previous versions

### 📊 Analytics Dashboard
- Daily usage charts
- Model usage distribution
- Most used prompts
- Token consumption breakdown
- Success rate tracking
- Cost trends

### 💰 Cost Tracker
- Real-time cost monitoring
- Cost breakdown by model
- Daily/weekly/monthly/lifetime costs
- Cost estimator tool
- Model pricing reference

### ⚖ A/B Testing
- Compare two prompts side-by-side
- Scoring based on response quality
- Latency and cost comparison
- Test history and results

### 🔐 Authentication
- JWT-based authentication
- Signup/Login with password hashing
- Role-based access (Admin/User)
- Secure password storage (bcrypt)

### 📤 Export Options
- Export prompts as CSV or JSON
- Export analytics as CSV
- Export history as CSV, JSON, or Markdown

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite (dev) / PostgreSQL (prod) |
| ORM | SQLAlchemy |
| Auth | JWT + bcrypt |
| AI APIs | OpenAI |
| Charts | Plotly |
| Deployment | Docker / Docker Compose |

## 📋 Prerequisites

- Python 3.9+
- OpenAI API Key (optional - can be set per user)

## 🏗 Installation

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/prompt-engineering-platform.git
cd prompt-engineering-platform
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Start the backend**
```bash
uvicorn backend.main:app --reload --port 8000
```

6. **Start the frontend** (in a new terminal)
```bash
streamlit run frontend/app.py --server.port=8501
```

7. **Open the application**
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run individual services
docker build -t pep-backend . --target backend
docker build -t pep-frontend . --target frontend
```

## 📁 Project Structure

```
PromptEngineeringPlatform/
│
├── frontend/               # Streamlit frontend
│   ├── app.py              # Main entry point with auth & navigation
│   ├── pages/
│   │   ├── dashboard.py    # Home dashboard with KPIs
│   │   ├── prompt_builder.py    # Create/edit prompts
│   │   ├── prompt_library.py    # Browse & manage prompts
│   │   ├── analytics.py    # Usage analytics & charts
│   │   ├── cost_tracker.py # Cost monitoring & estimation
│   │   ├── ab_testing.py   # A/B test runner
│   │   ├── history.py      # API call history
│   │   └── settings.py     # User settings & API keys
│   ├── components/         # Reusable UI components
│   └── assets/             # Static assets
│
├── backend/                # FastAPI backend
│   ├── main.py             # FastAPI app entry point
│   ├── database.py         # SQLAlchemy database setup
│   ├── models.py           # Database models
│   ├── auth.py             # JWT authentication
│   ├── api_routes.py       # All API endpoints
│   ├── ai_gateway.py       # OpenAI integration
│   ├── prompt_manager.py   # Prompt CRUD operations
│   ├── version_control.py  # Version management
│   ├── analytics.py        # Usage analytics
│   └── cost_tracker.py     # Cost calculation
│
├── tests/                  # API tests
│   └── test_api.py
│
├── docker/
│   └── start.sh            # Multi-service startup script
│
├── requirements.txt        # Python dependencies
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker orchestration
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/signup` | Register new user |
| POST | `/api/v1/login` | Login user |
| GET | `/api/v1/me` | Get current user |
| PUT | `/api/v1/me` | Update user settings |

### Prompts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/prompts` | List all prompts |
| POST | `/api/v1/prompts` | Create prompt |
| GET | `/api/v1/prompts/{id}` | Get prompt details |
| PUT | `/api/v1/prompts/{id}` | Update prompt |
| DELETE | `/api/v1/prompts/{id}` | Delete prompt |
| POST | `/api/v1/prompts/{id}/favorite` | Toggle favorite |
| POST | `/api/v1/prompts/{id}/duplicate` | Duplicate prompt |

### Versions
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/prompts/{id}/versions` | Get version history |
| POST | `/api/v1/prompts/{id}/versions/{v}/restore` | Restore version |

### AI Generation
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/generate` | Generate AI response |

### Analytics & Cost
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/analytics/summary` | Summary statistics |
| GET | `/api/v1/analytics/daily` | Daily usage data |
| GET | `/api/v1/analytics/models` | Model usage breakdown |
| GET | `/api/v1/analytics/popular` | Most used prompts |
| GET | `/api/v1/analytics/tokens` | Token consumption |
| GET | `/api/v1/cost/summary` | Cost summary |
| GET | `/api/v1/cost/breakdown` | Cost by period |
| GET | `/api/v1/cost/models` | Model pricing |

### A/B Testing
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/ab-tests` | Create and run A/B test |
| GET | `/api/v1/ab-tests` | List test history |

### History
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/history` | API call history |

## 🌐 Deployment

### Docker (Recommended)
```bash
docker-compose up -d --build
```

### AWS EC2
1. Launch an EC2 instance (Ubuntu 22.04)
2. Install Docker and Docker Compose
3. Clone the repository
4. Run `docker-compose up -d`
5. Configure security groups (ports 8000, 8501)

### Google Cloud Run
1. Build the Docker image
2. Push to Google Container Registry
3. Deploy to Cloud Run

### Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./pep.db` |
| `SECRET_KEY` | JWT signing secret | (required) |
| `OPENAI_API_KEY` | Default OpenAI API key | (optional) |
| `PORT` | Backend server port | `8000` |

## 📊 Database Schema

### Users
- `id`, `name`, `email`, `hashed_password`, `role`, `openai_api_key`, `created_at`

### Prompts
- `id`, `title`, `description`, `content`, `category`, `tags`, `variables`
- `system_prompt`, `temperature`, `max_tokens`, `top_p`, `output_format`
- `is_favorite`, `is_template`, `is_shared`, `user_id`, `created_at`, `updated_at`

### Prompt Versions
- `id`, `prompt_id`, `version`, `content`, `description`, `created_at`

### API Logs
- `id`, `user_id`, `prompt_id`, `model`, `prompt_text`, `response_text`
- `input_tokens`, `output_tokens`, `total_tokens`, `latency_ms`, `cost`
- `success`, `error_message`, `timestamp`

### A/B Tests
- `id`, `user_id`, `name`, `prompt_a_id`, `prompt_b_id`, `test_input`
- `response_a`, `response_b`, `score_a`, `score_b`, `winner`
- `metrics_a`, `metrics_b`, `status`, `created_at`, `completed_at`

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_api.py -v

# Run with coverage
pytest --cov=backend tests/ -v
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for the GPT API
- Streamlit for the amazing frontend framework
- FastAPI for the high-performance backend
- All open-source contributors

---

Built with ❤️ for prompt engineers everywhere.

