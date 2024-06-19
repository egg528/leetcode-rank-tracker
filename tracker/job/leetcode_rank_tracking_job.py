from tracker.service.leetcode_client import LeetCodeClient
from tracker.service.rank_handler import RankHandler
from tracker.service.ranking_graph_generator import RankingGraphGenerator
from tracker.utils.logger import Logger
from tracker.utils.date import get_now


class LeetCodeRankTrackingJob:
    def __init__(self, username: str):
        self.username = username
        self.ranking_graph_generator = RankingGraphGenerator(username=username)
        self.rank_handler = RankHandler(username=username)
        self.leetcode_client = LeetCodeClient(username=username)

    def run(self):
        # read
        now_rank = self.leetcode_client.get_rank()

        # process
        if self.rank_handler.is_new_rank(get_now(), now_rank) is False:
            Logger.info("no change in ranking")
            return

        self.rank_handler.upsert(get_now(), now_rank)
        recent_ranks = self.rank_handler.find_recent_ranking()

        # write
        self.ranking_graph_generator.generate(recent_ranks)
