# job-ecosystem-scraper 🕷️

A modular job scraping engine designed to extract job listings from various platforms. Built for integration into a larger auto-application ecosystem. Uses [`jobspy`](https://github.com/speedyapply/JobSpy) for multi-site scraping and `pandas` for data handling. Hosted and deployed via [Railway](https://railway.app/).

---

## 🚀 Features

- 🔍 Scrape from LinkedIn, Indeed, Glassdoor, and more via `jobspy`
- 📦 Export to CSV, JSON, or direct API (WIP)
- ⚙️ Modular scraper setup for expansion
- 🧠 Clean, pandas-powered job normalization
- 🪄 CLI interface and async job runner (cron/job queue-ready)
- ☁️ Deploy-ready with Railway and Docker

---

## 🧱 Tech Stack

| Tool     | Role                          |
|----------|-------------------------------|
| Python   | Core language                  |
| JobSpy   | Scraping backend               |
| pandas   | Data manipulation              |
| Railway  | Hosting and background jobs    |
| Docker   | Containerization (optional)    |

---

## 🗂️ Project Structure
TBD

---

## 🛠️ Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/job-ecosystem-scraper.git
cd job-ecosystem-scraper
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**

```env
JOB_QUERY="software engineer"
LOCATION="remote"
RESULTS_PER_SITE=25
OUTPUT_FORMAT="csv"
```

4. **Run a scrape**

```bash
python main.py
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📦 Output

By default, scraped job listings are saved to `data/` as `.csv` or `.json`, and optionally returned via stdout.

---

## ☁️ Deployment (Railway)

1. Link this repo to [Railway](https://railway.app/)
2. Set your `.env` vars in the Railway dashboard
3. Add a Railway cron job or trigger the scraper on a schedule
4. (Optional) Connect to an external API or DB to send results

---

## 📌 Roadmap

- [ ] Add support for pushing results to central API
- [ ] Rate limiting / proxy rotation
- [ ] Retry failed jobs
- [ ] Add more site modules
- [ ] Dockerize for Railway jobs

---

**Built to feed the ecosystem. Automate your grind.**
