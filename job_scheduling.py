"""
Members:
Arzaga, Jemieryn (Coin Change Problem)
Bautista, Mark Anthony (Menu system, integration & Testing)
Bermas, Estella Mae (Huffman Coding)
Santos, Jaymee (Fractional Knapsack)
Sibal, Nicole Margareth (Job Scheduling with Deadlines)
February, 2026
"""

# THIS MODULE SOLVES JOB SEQUENCING WITH DEADLINES FOR MAX PROFIT.


def _input_int(prompt, min_val=None):
    # KEEP ASKING UNTIL THE USER ENTERS A VALID INTEGER.
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"ENTER AN INTEGER >= {min_val}.")
                continue
            return value
        except ValueError:
            print("PLEASE ENTER A VALID INTEGER.")


def _input_float(prompt):
    # KEEP ASKING UNTIL THE USER ENTERS A VALID NUMBER.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER.")


def job_sequencing(jobs):
    jobs_sorted = sorted(jobs, key=lambda job: job[2], reverse=True)
    max_deadline = max((deadline for (_, deadline, _) in jobs_sorted), default=0)
    schedule = [None] * (max_deadline + 1)
    total_profit = 0
    scheduled_jobs = []

    for job_id, deadline, profit in jobs_sorted:
        slot = deadline
        while slot > 0:
            if schedule[slot] is None:
                schedule[slot] = (job_id, profit)
                total_profit += profit
                scheduled_jobs.append((slot, job_id, profit))
                break
            slot -= 1

    scheduled_jobs.sort()
    return total_profit, scheduled_jobs


def read_jobs():
    count = _input_int("Number of jobs: ", 1)
    jobs = []
    for index in range(count):
        job_id = input(f"Job id (default J{index + 1}): ") or f"J{index + 1}"
        deadline = _input_int("  deadline (positive integer): ", 1)
        profit = _input_float("  profit: ")
        jobs.append((job_id, deadline, profit))
    return jobs
