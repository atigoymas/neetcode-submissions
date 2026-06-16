class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)))
        stack = []
        for i in range(len(pairs)-1, -1, -1):
            time = (target - pairs[i][0])/pairs[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
            
        return len(stack)

        