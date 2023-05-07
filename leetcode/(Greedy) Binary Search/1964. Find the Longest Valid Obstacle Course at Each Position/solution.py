class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = n*[1]
        h_list = []

        for i, height in enumerate(obstacles):
            pos = bisect_right(h_list, height)
            if pos == len(h_list):
                h_list.append(height)
            else:
                h_list[pos] = height
            ans[i] = pos + 1

        return ans