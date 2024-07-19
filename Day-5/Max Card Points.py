class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        current_score = sum(cardPoints[:k])
        max_score = current_score

        for i in range(1, k + 1):
            current_score = current_score - cardPoints[k - i] + cardPoints[-i]
            max_score = max(max_score, current_score)
            
        return max_score