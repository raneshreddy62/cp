class Solution:
    def maxWidthOfVerticalArea(self,points:list[list[int]]) ->int:
        points.sort(key=itemgetter(0))
        cricket=0
        for i in range(len(points)-1):
            p1,p2=points[i][0],points[i+1][0]
            diff=p2-p1
            if diff>cricket:
                cricket=diff
        return cricket
