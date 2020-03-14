class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0
            
        # pages per person
        left, right = max(pages), sum(pages) 
        while left + 1 < right:
            countPeople = 1
            mid = (left + right ) // 2
            curPage = mid
            for page in pages:
                if page <= curPage:
                    curPage -= page 
                else:
                    countPeople += 1 
                    curPage = mid - page 
            print(countPeople)
            if countPeople <= k:
                right = mid 
            else:
                left = mid

        
        curPage = left
        count = 1
        for page in pages:
            if curPage >= page:
                curPage -= page 
            else:
                count += 1 
                curPage = left - page 
                
        if count <= k:
            return left 
            
        return right 