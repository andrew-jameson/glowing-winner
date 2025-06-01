from jobspy import scrape_jobs
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import sys

# GLOBAL vars
locations = [
    "Asheville, NC",
    "Hendersonville, NC",
    "Charlotte, NC"
    "Melbourne, FL",
    "Orlando, FL",
    "Boston, MA",
    "Salt Lake City, UT",
    "Ogden, UT",
    "SLC, UT"
]
class JobScraper(ABC):
    def __init__(self, search_term: str, location: Optional[str] = None, **kwargs):
        self.search_term = search_term
        self.location = location
        self.params = kwargs

    @abstractmethod
    def scrape(self) -> List[Dict]:
        """
        Implement this method in subclasses.
        Should return a list of job dicts.
        """
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(search_term='{self.search_term}', location='{self.location}')"

def run_scraper():
    jobs = {}
    for loc in locations:
        
        bogus=    scrape_jobs(
                site_name=["indeed"], # other job sites are erroring out, will need debug those but linkedin works
                search_term="Python Developer",
                location=loc,
                distance=100,
                is_remote=False,
                results_wanted=5,
                country_indeed='USA',
                hours_old=24
            )
        worthy_keys = [ 'title', 'company',
       'location',
       'min_amount', 'max_amount', 'is_remote', 'description']
        single_job = {}
        for key in worthy_keys:
            single_job[key] = bogus[key]
        print(f"{single_job}")  # getting gibberish here
        sys.exit(1)
        jobs.update()
    #jobs.to_csv("results.csv", index=False)
    print(f"Scraped {len(jobs)} jobs")
    print(jobs)
    sys.exit(1)
    return jobs

def linkedin_scraper():
    query = "Python Developer" # TODO: loop over dozens of such queries
    batch_size = 10
    iterations = 25
    total_results = iterations * batch_size
    jobs = []
    for offset in range(0, total_results, batch_size):
        jobs += scrape_jobs(
                site_name=["linkedin"],
                search_term=query,
                location="United States",       # human‐readable
                extra_params={"geoId": "103644278", "distance": "0"}, 
                is_remote=False,
                results_wanted=batch_size,
                hours_old=24,
                offset=offset,
                linkedin_fetch_description=True,
                job_type="fulltime",
            ).to_dict(orient="records")
    print(f"Scraped {len(jobs)} jobs")
    print(jobs)
    sys.exit(1)

    worthy_keys = [ 'title', 'company', 'location',
    'min_amount', 'max_amount', 'is_remote', 'description']
    single_job = {}
    filtered_jobs = {}

    for job in jobs:
        print(job)
        for key in worthy_keys:
            single_job[key] = job[key]
        print(single_job)
        filtered_jobs[job['id']] = single_job
    print("#"*90)
    print(filtered_jobs)
    sys.exit(1)
    return jobs
