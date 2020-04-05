class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = set()
        # name: city
        seen = defaultdict(list)
        for tran in transactions:
            name, time, amount, city = tran.split(',')
            time = int(time)
            if int(amount) > 1000:
                result.add(tran)

            for t, c, tr in seen[name]:
                if abs(t - time) <= 60 and c != city:
                    result.add(tran)
                    result.add(tr)
            seen[name].append((time, city, tran))
        print(seen)
        return list(result)
            
            
            
        