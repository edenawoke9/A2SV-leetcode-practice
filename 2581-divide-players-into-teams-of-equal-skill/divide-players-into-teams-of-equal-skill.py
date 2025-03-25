class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        right=len(skill)-1
        divisions=len(skill)/2
        target=sum(skill)/divisions
        skill.sort()
        
        left=0
        chemistry =1
        while left<right:
            if skill[right]+skill[left]==target:
                chemistry+=skill[right]*skill[left]
                left+=1
                right-=1
            else:
                return -1
        return chemistry-1

        