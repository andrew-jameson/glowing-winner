import redis
import os

def get_redis_client():
    return redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=True  # ensures string output
    )

def push_job_to_stream(job_data: dict):
    if job_data is None:
        print("[WARN]: received empty job, skipping.")
        return
    client = get_redis_client()
    stream = os.getenv("REDIS_STREAM_NAME", "jobs")
    client.xadd(stream, job_data)
