# main.py
from jobspy import scrape_jobs

def run_scraper():
    jobs = scrape_jobs(
        site_name="indeed",
        search_term="Python Developer",
        location="Remote",
        results_wanted=20,
        country_indeed='us',
        hours_old=24
    )
    jobs.to_csv("results.csv", index=False)
    print("Scraped and saved jobs.")

if __name__ == "__main__":
    run_scraper()
