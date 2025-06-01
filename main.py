# main.py
from jobspy import scrape_jobs
from dotenv import load_dotenv
from redis_client import push_job_to_stream

def run_scraper():
    jobs = scrape_jobs(
        search_term="Python Developer",
        location="Remote",
        results_wanted=20,
        country_indeed='us',
        hours_old=24
    )
    jobs.to_csv("results.csv", index=False)
    print(f"Scraped {len(jobs)} jobs")

    return jobs


def clean_job_row(row):
    return {
        "title": row['title'],
        "company": row['company_name'],
        "location": row['location'],
        "description": row['description'][:500],  # Truncate if needed
        "url": row['job_url'],
        "source": row['site'],
        "date_posted": str(row['date_posted']),
    }

if __name__ == "__main__":
    load_dotenv()
    jobs = run_scraper()
    for _, row in jobs.iterrows():
        job_data = clean_job_row(row)
        push_job_to_stream(job_data)
