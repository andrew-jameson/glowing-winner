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
Get [Docker](https://docs.docker.com/desktop/setup/install/mac-install/)

Will assume you have python 3.10+ and brew.
```zsh
pip install -r requirements.txt
brew install redis
```

3. **Create a `.env` file**

```env
REDIS_STREAM_NAME=jobs
REDIS_HOST=localhost
REDIS_PORT="6379"
REDIS_PASSWORD="redis"
```

4. **Run a scrape**

```bash
docker run -d --name redis-local -p 6379:6379 redis --requirepass redis
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
