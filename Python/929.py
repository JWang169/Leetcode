class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """   
        results = set()
        for email in emails:
            local, domain = email.split('@')
            local = ''.join(local.split('+')[0].split('.'))
            results.add(local + '@' + domain)
        return len(results)