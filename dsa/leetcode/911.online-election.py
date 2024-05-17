#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
import bisect
import collections


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lead_at_time = []
        count = collections.defaultdict(int)
        leader = -1

        for person in persons:
            count[person] += 1
            if count[person] >= count.get(leader, 0):
                # idea to extend to multiple leaders: maintain a heap size n here, and update
                leader = person
            self.lead_at_time.append(leader)

    def q(self, t: int) -> int:
        return self.lead_at_time[bisect.bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end
