class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mVal = 0
        b,w = 0, 0
        l,r = 0,0
        while r <k:
            if blocks[r] == "W":
                w +=1
            if blocks[r] == "B":
                b +=1
            r +=1
        mVal = w
        while r < len(blocks):
            if blocks[r] == "W" and blocks[l] == "B":
                w +=1
                b -=1
            if blocks[r] == "B" and blocks[l] == "W":
                w -=1
                b +=1
            mVal = min(mVal,w)
            r+=1
            l+=1
        return mVal