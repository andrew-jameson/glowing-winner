# main.py
from jobspy import scrape_jobs
from dotenv import load_dotenv
from redis_client import push_job_to_stream


def run_scraper():
    jobs = scrape_jobs(
        site_name="linkedin", # other job sites are erroring out, will need debug those but linkedin works
        search_term="Python Developer",
        location="Remote",
        results_wanted=256,
        country_indeed='us',
        hours_old=24
    )
    print(jobs.keys())
    #jobs.to_csv("results.csv", index=False)
    print(f"Scraped {len(jobs)} jobs")

    return jobs


def clean_job_row(row: dict) -> dict | None:
    '''
    Row should look a little something like this:
            "title": row['title'],
            "company": row['company'],
            "location": row['location'],
            "description": row['description'][:500],  # Truncate if needed
            "url": row['job_url'],
            "source": row['site'],
            "date_posted": str(row['date_posted']),
    '''

    cleaned = {}
    for key in row:
        if key is None: continue
        value = str(row.get(key, "Empty")).strip()
        if value is not None:
            cleaned[str(key)] = value

    return cleaned


if __name__ == "__main__":
    load_dotenv(".envdev")
    jobs = run_scraper()
    for _, row in jobs.iterrows():
        job_data = clean_job_row(row)
        push_job_to_stream(job_data)
