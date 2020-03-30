class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes or not votes[0]:
            return ""
        n = len(votes[0])
        
        # rankings['A'] = {0: 5, 1: 3, 2: 1}
        rankings = collections.defaultdict(dict)
        for vote in votes:
            for rank, team in enumerate(vote):
                rankings[team][rank] = rankings[team].get(rank, 0)
                rankings[team][rank] += 1 
        
        heap = []
        for team, voteDict in rankings.items():
            item = []
            for i in range(n):
                if i in voteDict:
                    item.append(-voteDict[i])
                else:
                    item.append(0)
            item.append(team)
            heapq.heappush(heap, item)
            
        seen = set()
        result = ""
        while heap:
            best = heapq.heappop(heap)
            if best[-1] not in seen:
                result += best[-1]
                seen.add(best[-1])
            if result == n:
                return result
        return result
        