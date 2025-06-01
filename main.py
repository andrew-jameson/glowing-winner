from dotenv import load_dotenv
from redis_client import push_job_to_stream
from scrapers import base_scraper
import sys

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

    sys.exit(1)
    return cleaned


if __name__ == "__main__":
    load_dotenv(".env")  # switch to .envdev for connection to railway redis
    jobs = base_scraper.linkedin_scraper()
    for _, row in jobs.iterrows():
        job_data = clean_job_row(row)
        print(job_data)
        push_job_to_stream(job_data)
