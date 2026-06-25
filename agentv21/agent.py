import time
import uuid
from google.adk.agents.llm_agent import Agent


MODEL_NAME = "openai/gpt-4.1-nano"

jobs = {}


def submit_long_running_job(task: str) -> dict:
    """
    Submit a long-running async job.

    Use this tool when the user asks to start, submit, run, launch,
    deploy, train, analyze, or execute a long-running task.
    """
    job_id = str(uuid.uuid4())[:8]

    jobs[job_id] = {
        "task": task,
        "status": "RUNNING",
        "created_at": time.time(),
        "duration_seconds": 65,
        "result": None,
    }

    return {
        "job_id": job_id,
        "status": "RUNNING",
        "message": "Job submitted. Use check_job_status with this job_id.",
    }


def check_job_status(job_id: str) -> dict:
    """
    Check status of a submitted async job.

    Use this tool when the user asks for job status, progress,
    or whether a job has completed.
    """
    if job_id not in jobs:
        return {
            "status": "NOT_FOUND",
            "message": f"No job found with id {job_id}",
        }

    job = jobs[job_id]
    elapsed = time.time() - job["created_at"]

    if elapsed >= job["duration_seconds"]:
        job["status"] = "COMPLETED"
        job["result"] = {
            "summary": f"Completed task: {job['task']}",
            "output": [
                "Step 1 completed",
                "Step 2 completed",
                "Step 3 completed",
            ],
        }

    return {
        "job_id": job_id,
        "status": job["status"],
        "elapsed_seconds": round(elapsed, 2),
        "result": job["result"],
    }


def list_jobs() -> dict:
    """
    List all submitted jobs and their current status.
    """
    return jobs


root_agent = Agent(
    name="agentv21",
    model=MODEL_NAME,
    description="Async long-running job agent.",
    instruction="""
You are Agent V21.

You manage long-running async jobs.

Rules:
- If user asks to start/run/launch/deploy/train/analyze a long-running task, call submit_long_running_job.
- If user asks for status, progress, or result, call check_job_status.
- If user asks to list jobs, call list_jobs.
- Never pretend a job completed without checking status.
- Keep responses concise.
""",
    tools=[
        submit_long_running_job,
        check_job_status,
        list_jobs,
    ],
)
