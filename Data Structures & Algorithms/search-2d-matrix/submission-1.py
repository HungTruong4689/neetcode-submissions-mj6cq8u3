class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,0
        m,n = len(matrix)-1, len(matrix[0])-1
        #print(m,n)
        while i <=m and j <=n:
            mid1= (i + m)//2
            mid2 = (j+n)//2
            midV = matrix[mid1][mid2]
            print(mid1, mid2)
            print(midV)
            if midV == target:
                return True
            elif midV > target:
                m = mid1 -1
                
            else:
                i = mid1 +1
               
        return False