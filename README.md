# LeetCode Rank Tracker

## :heavy_check_mark: Problem

![leetcode_profile.jpg](docs/img/leetcode_profile.jpg)  
- LeetCode only provides the current ranking.
- I wanted to see the changes in my rank over time.
<br></br>

## :heavy_check_mark: Solution
- A Python-based job and GitHub Actions are used as a scheduler to collect the LeetCode rank every hour.
- Based on the collected ranks, a graph image showing the rank changes is generated.

<br></br>

## :heavy_check_mark: How to Use
1. Fork this repository.
2. Edit the LeetCode username in `.github/workflows/scheduler.yml` to your own username.
    ```yaml
    - name: run job
      run: |
        python3 -m tracker --username {username}
    ```
3. Check the rank changes in the files `tracker/output/{username}.csv` and `tracker/output/{username}.png`.
