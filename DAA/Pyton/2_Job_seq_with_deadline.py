class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    result = [-1] * (max_deadline + 1)
    total_profit = 0
    job_sequence = []
    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if result[t] == -1:
                result[t] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break
    return job_sequence, total_profit

if __name__ == "__main__":
    n = int(input("Enter number of jobs: "))
    jobs = []
    for i in range(n):
        job_id = input(f"\nEnter Job ID for Job {i+1}: ")
        deadline = int(input(f"Enter deadline for Job {job_id}: "))
        profit = int(input(f"Enter profit for Job {job_id}: "))
        jobs.append(Job(job_id, deadline, profit))
    sequence, profit = job_sequencing(jobs)
    print("\n--- Job Sequencing Result ---")
    print("Job Sequence:", sequence)
    print("Total Profit:", profit)
