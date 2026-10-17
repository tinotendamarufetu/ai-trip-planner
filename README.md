# ✈️ EndaNeni AI — Multi-Agent Travel Planner with LangGraph

An AI-powered travel planning application that transforms natural-language requests into personalized travel plans, including flight research, hotel suggestions, and day-by-day itineraries.

Built with **LangGraph, LangChain, Groq, and FastAPI**, the application uses a multi-agent workflow to break down travel requests into smaller tasks and combine the results into a structured travel plan.

# Live Demo: https://endaneni-trip-planner.onrender.com/
*** Note: Hosted on a free cloud tier, please allow up to 30 seconds for the initial server spin-up. ***



## 🚀 Why This Project?

Planning a trip often involves switching between flight search engines, hotel websites, travel guides, and spreadsheets.

TripMate AI explores how **multi-agent AI systems can simplify travel planning** by coordinating specialized agents through a single application.

Instead of relying on one general-purpose AI response, the workflow separates the planning process into distinct responsibilities:

- ✈️ **Flight Research Agent** — Retrieves flight-related information using AviationStack.
- 🏨 **Hotel Research Agent** — Searches the web for accommodation options using Tavily.
- 🗺️ **Itinerary Planning Agent** — Organizes destination research and travel preferences into a day-by-day itinerary.
- 🧠 **Response Agent** — Combines the available information into a clear, structured travel plan.

LangGraph orchestrates the workflow, allowing the application to coordinate the agents and manage the flow of information between them.

## ✨ Features

- **Multi-agent orchestration:** Coordinates specialized travel-planning agents using LangGraph.
- **Flight research:** Integrates with AviationStack to retrieve available flight-related data.
- **Hotel discovery:** Uses Tavily search to research accommodation options.
- **Personalized itineraries:** Generates travel plans based on user requests, destinations, duration, and budget.
- **Natural-language interaction:** Allows users to describe their travel requirements in plain English.
- **FastAPI backend:** Exposes endpoints for travel requests and application health checks.
- **Web interface:** Provides a simple frontend built with HTML, CSS, JavaScript, and Jinja2 templates.
- **Conversation persistence:** Uses PostgreSQL to support persistent conversation state.
- **LLM-powered reasoning:** Uses Groq-hosted language models to support agent reasoning and response generation.

> **Note:** Flight information, accommodation suggestions, prices, and availability depend on the underlying APIs and search results. The application provides research and planning assistance; it does not guarantee real-time availability or complete bookings unless booking functionality is implemented separately.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core application language |
| FastAPI | Backend API and web application |
| LangGraph | Multi-agent workflow orchestration |
| LangChain | LLM and tool integration |
| Groq | Language model inference |
| PostgreSQL | Database and conversation persistence |
| Tavily API | Web search and hotel research |
| AviationStack API | Flight-related data |
| Jinja2 | HTML template rendering |
| HTML, CSS, JavaScript | Frontend interface |

## 🏗️ Project Structure

```text
.
├── app.py              # FastAPI application entry point
├── backend.py          # LangGraph travel-planning workflow
├── requirements.txt    # Python dependencies
├── static/             # Frontend assets
├── templates/          # Jinja2 HTML templates
└── tools/              # Flight and web search integrations
```

## ⚙️ Prerequisites

Before running the application, make sure you have:

- Python 3.10 or newer
- PostgreSQL installed and running
- A Groq API key
- A Tavily API key
- An AviationStack API key

You will need to configure the API credentials and database connection before starting the application.

## 🔐 Environment Variables

Create a `.env` file in the project root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DEFAULT_ORIGIN_IATA=DAC
```

Replace the example values with your actual credentials and database connection details.

`DEFAULT_ORIGIN_IATA` specifies the default departure airport using its IATA code. The example `DAC` refers to Dhaka, Bangladesh; change it to your preferred default departure airport.

**Security:** Never commit your `.env` file or expose API keys in your source code. Add `.env` to your `.gitignore` file.

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the repository URL and directory with your actual GitHub repository details.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows — PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure the environment

Create your `.env` file, add the required API keys, and confirm that PostgreSQL is accessible using the configured `DATABASE_URL`.

Make sure any database tables or initialization steps required by your application have been completed.

## ▶️ Running the Application

Start the application:

```bash
python app.py
```

If `app.py` does not start the server directly, use the appropriate Uvicorn command for your FastAPI application, for example:

```bash
uvicorn app:app --reload
```

Then open your browser at:

**http://127.0.0.1:8000/**

The interactive API documentation may also be available at:

**http://127.0.0.1:8000/docs**

The documentation URL depends on your FastAPI configuration.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Checks application health |
| `POST` | `/api/travel` | Submits a natural-language travel request |

### Example: Submit a Travel Request

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

This example asks the application to plan a three-day trip to Tokyo within a stated budget.

The exact response structure depends on how the API endpoint and agent workflow are implemented.

## 🔄 How the Multi-Agent Workflow Works

The application separates travel planning into specialized tasks coordinated by LangGraph.

1. **User input:** The traveler submits a request describing their destination, duration, budget, and preferences.
2. **Flight research:** The flight agent gathers relevant flight information through the AviationStack integration.
3. **Accommodation research:** The hotel agent uses Tavily to search for relevant accommodation information.
4. **Itinerary planning:** The itinerary agent organizes the available information into a practical day-by-day plan.
5. **Response generation:** The final response agent combines the outputs into a readable travel plan.
6. **State persistence:** PostgreSQL supports conversation persistence where configured in the application.

The workflow is designed to separate responsibilities, making the system easier to extend with additional tools, agents, and travel-planning capabilities.

## 🧠 Key Learning Objectives

This project provides a practical opportunity to explore:

- Designing multi-agent AI applications.
- Orchestrating agent workflows with LangGraph.
- Connecting language models to external APIs and search tools.
- Building API-driven AI applications with FastAPI.
- Managing application configuration and API credentials.
- Integrating PostgreSQL for persistent application state.
- Transforming natural-language requests into structured outputs.

## 🔮 Potential Future Improvements

Possible enhancements include:

- Adding additional flight and accommodation data providers.
- Improving budget allocation across flights, hotels, meals, and activities.
- Supporting currency conversion and estimated trip costs.
- Introducing user preferences and personalized recommendations.
- Adding itinerary editing and regeneration.
- Improving error handling, retries, and API rate-limit management.
- Adding automated tests and workflow observability.
- Integrating booking providers where supported.
- Deploying the application with a production-ready database and hosting setup.

These are potential extensions rather than claims about currently implemented functionality.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Implement and test your changes.
4. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

5. Push your branch and open a pull request.

Please describe the changes you made and include relevant testing details.

## 🙏 Acknowledgments

This project builds on the Python AI ecosystem and the tools provided by LangGraph, LangChain, Groq, FastAPI, Tavily, AviationStack, and PostgreSQL.

It demonstrates an approach to building a travel-planning application in which specialized AI agents collaborate to transform a natural-language request into a structured travel plan.

---

**Built to explore the possibilities of multi-agent AI for smarter travel planning.**