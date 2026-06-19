# Job Matching #1

Let's build a matchmaking system that helps discover jobs for developers based on a number of factors.

One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we generally have a rough idea of the minimum salary we would be satisfied with.

Let's give this a try. We'll create a function match (job_matching in Python) which takes a candidate and a job, which will return a Boolean indicating whether the job is a valid match for the candidate.

A candidate will have a minimum salary, so it will look like this:

candidate = {
  'min_salary': 120000
}

A job will have a maximum salary, so it will look like this:

job = {
  'max_salary': 140000
}

If either the candidate's minimum salary or the job's maximum salary is not present, throw an error.

For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. However, let's also include 10% wiggle room (deducted from the candidate's minimum salary) in case the candidate is a rockstar who enjoys programming on Codewars in their spare time. The company offering the job may be able to work something out.

# Given Code

```{python}
def job_matching(candidate, job):
    #your code here
```

# My Solution

```{python}
def job_matching(candidate, job):
    # Check if either the candidate's minimum salary or the job's maximum salary is not present
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Candidate's minimum salary and job's maximum salary are required.")

    # Calculate the minimum acceptable salary for the candidate with a 10% wiggle room
    min_acceptable_salary = candidate['min_salary'] * 0.9

    # Check if the job's maximum salary is greater than or equal to the candidate's minimum acceptable salary
    if job['max_salary'] >= min_acceptable_salary:
        return True
    else:
        return False
```
