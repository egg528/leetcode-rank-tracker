import argparse

from tracker.utils.logger import Logger
from tracker.job.leetcode_rank_tracking_job import LeetCodeRankTrackingJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='LeetCode username')
    args = parser.parse_args()

    Logger.info("LeetCodeRankTrackingJob Start")
    LeetCodeRankTrackingJob(args.username).run()
    Logger.info("LeetCodeRankTrackingJob End")

