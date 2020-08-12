# python3
# Parallel Processing

import heapq as hq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Jobs:
    def __init__(self, time_taken, processing_started=0):
        self.time_taken = time_taken
        self.processing_started = processing_started

    # Sorted by release time but if they are same then sorted using thread id i.e. their
    # time taken to accomplish the task.

    def __lt__(self, other):
        if self.processing_started == other.processing_started:
            return self.time_taken < other.time_taken
        return self.processing_started < other.processing_started

    def __gt__(self, other):
        if self.processing_started == other.processing_started:
            return self.time_taken > other.time_taken
        return self.processing_started > other.processing_started

def assign_jobs():
    # n_workers, jobs
    result = []
    queue_capacity = [Jobs(i) for i in range(n_workers)]

    for job in jobs_time:
        current_worker = hq.heappop(queue_capacity)

        result.append(AssignedJob(current_worker.time_taken, current_worker.processing_started))

        current_worker.processing_started += job

        hq.heappush(queue_capacity, current_worker)

    return result


n_workers, n_jobs = map(int, input().split())
jobs_time = list(map(int, input().split()))
assert len(jobs_time) == n_jobs

assigned_jobs = assign_jobs()

for job in assigned_jobs:
    print(job.worker, job.started_at)
