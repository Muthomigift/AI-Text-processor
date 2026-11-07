# AI Text Processor

A small web app that sends text to Google's Gemini model and shows the response. Built with Flask and deployed on Render.

## Demo

**Live demo:** https://ai-text-processor-bm8b.onrender.com/

> The demo runs on Render's free tier, so it sleeps when idle. The first request after a break can take up to a minute to wake up.

## Features

- Simple one-page interface: type text, click Send, get an AI response
- REST API endpoint (`POST /api/process`) you can call from other apps
- Uses Gemini through its OpenAI-compatible endpoint
- API key kept out of the code via environment variables
- Error messages shown in the page instead of failing silently

## Tech Stack

- **Backend:** Python, Flask, Flask-CORS
- **AI:** Google Gemini via the `openai` Python library
- **Frontend:** HTML, CSS, vanilla JavaScript (`fetch`)
- **Hosting:** Render, served with Gunicorn

## Project Structure

```
.
├── app.py              # Flask app and API route
├── requirements.txt    # Python dependencies
├── .gitignore
└── templates/
    └── index.html      # Frontend page
```

## Run Locally

1. Clone the repository:

   ```
   git clone https://github.com/Muthomigift/AI-Text-processor.git
   cd YOUR-REPO
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac / Linux
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your_key_here
   ```

   Get a key from [Google AI Studio](https://aistudio.google.com/).

5. Start the app:

   ```
   python app.py
   ```

6. Open http://localhost:5000

## API Usage

**Endpoint:** `POST /api/process`

**Request body:**

```json
{ "text": "Summarize this paragraph..." }
```

**Success response:**

```json
{ "result": "The model's reply" }
```

**Error response:**

```json
{ "error": "Description of what went wrong" }
```

Example with curl:

```
curl -X POST https://ai-text-processor-bm8b.onrender.com/api/process \
  -H "Content-Type: application/json" \
  -d '{"text": "Say hello"}'
```

## Deploy to Render

1. Push the project to GitHub.
2. In Render, create a new **Web Service** and connect the repository.
3. Set the build command to `pip install -r requirements.txt`.
4. Set the start command to `gunicorn app:app`.
5. Add the environment variable `GEMINI_API_KEY` with your key.
6. Deploy.

## Notes

- Never commit your `.env` file. It is listed in `.gitignore`.
- Model names change over time. If the API returns a 404, update the `model=` value in `app.py` to a current Gemini model.

## Pricing

This project is available as a done-for-you service. Prices are in Kenyan shillings (KSh) and depend on the scope of the work.

Service	Price
Basic setup: this app deployed live with your own API key	KSh 6,500 - 20,000
Custom version: tailored to one task (email drafting, summarizing, rewriting, etc.) with your branding	KSh 20,000 - 65,000
Advanced version: adds user login, saved history, or a database	KSh 65,000 - 195,000+
Hosting and maintenance: always-on hosting, updates, and small fixes	KSh 1,500 - 6,500 / month

What's included: deployment, API key setup, and a short handover so you know how to use and update the app.

What's not included: your own AI API usage costs, which are billed directly by the provider.

Final quotes depend on the project. Get in touch to discuss what you need.

## Author

Built by Gift Muthomi. Feel free to reach out for custom versions of this project.
Contact: muthomigift@gmail.com