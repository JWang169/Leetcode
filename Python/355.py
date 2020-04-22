class User:
    def __init__(self, userId):
        self.userId = userId 
        self.tweets = []
        self.followings = set()
        self.followers = set()
        self.newsFeed = []


class Twitter(object):

    def __init__(self):
        self.graph = dict()
        self.time = 0 
        

    def postTweet(self, userId, tweetId):
        if userId not in self.graph:
            newUser = User(userId)
            self.graph[userId] = newUser
        theUser = self.graph[userId]
        theUser.tweets.append((self.time,  tweetId))
        theUser.newsFeed.append((self.time,  tweetId))
        followers = theUser.followers 
        for followerId in followers:
            person = self.graph[followerId]
            person.newsFeed.append((self.time,  tweetId))
        
        self.time += 1 
        return tweetId
    
    
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.graph:
            return []
        newsFeed = self.graph[userId].newsFeed
        res = []
        n = len(newsFeed) - 1
        count = 0
        while n >= 0 and count < 10:
            res.append(newsFeed[n][1])
            count += 1 
            n -= 1 
        return res 
        

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return 
            
        if followerId not in self.graph:
            self.graph[followerId] = User(followerId)
        if followeeId not in self.graph:
            self.graph[followeeId] = User(followeeId)
        
        follower = self.graph[followerId]
        followee = self.graph[followeeId]
        if followerId in followee.followers:
            return 
        follower.followings.add(followeeId)
        followee.followers.add(followerId)
        tweets = followee.tweets
        follower.newsFeed += tweets
        follower.newsFeed.sort()

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        
        if followerId not in self.graph:
            self.graph[followerId] = User(followerId)
        if followeeId not in self.graph:
            self.graph[followeeId] = User(followeeId)
            
        followee = self.graph[followeeId]
        follower = self.graph[followerId]  
        oldTweets = set()
        for time, tweet in followee.tweets:
            oldTweets.add(tweet)
        
        if followeeId in follower.followings:
            follower.followings.remove(followeeId)
        if followerId in followee.followers:
            followee.followers.remove(followerId)
            
        replaceNewsFeed = []
        for time, news in follower.newsFeed:
            if news in oldTweets:
                continue 
            else:
                replaceNewsFeed.append((time, news))
        follower.newsFeed = replaceNewsFeed
        
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)