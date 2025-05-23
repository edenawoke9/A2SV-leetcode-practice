class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float('inf')
        best_hour = 0
        
        # Precompute prefix sums of 'N's and suffix sums of 'Y's
        prefix_N = [0] * (n + 1)
        suffix_Y = [0] * (n + 1)
        
        # Calculate prefix_N: prefix_N[i] is the number of 'N's in the first i hours (0..i-1)
        for i in range(1, n + 1):
            prefix_N[i] = prefix_N[i - 1] + (1 if customers[i - 1] == 'N' else 0)
        
        # Calculate suffix_Y: suffix_Y[i] is the number of 'Y's from hour i to n-1
        for i in range(n - 1, -1, -1):
            suffix_Y[i] = suffix_Y[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        # Calculate penalty for each closing hour
        for hour in range(n + 1):
            penalty = prefix_N[hour] + suffix_Y[hour]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = hour
        
        return best_hour