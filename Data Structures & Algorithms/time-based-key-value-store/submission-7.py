class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            self.keys[key].append([timestamp,value])
        else:
            self.keys[key]=[[timestamp,value]]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        r = len(self.keys[key])-1
        if self.keys[key][r][0]<=timestamp:
            return self.keys[key][r][1]
        l=0
        mid = l +(r-l)//2
        while(l<r):
            mid = l +(r-l)//2
            if(self.keys[key][mid][0]<=timestamp):
                l=mid+1              
            else:
                r = mid
        if l==0:
            return ""
        return self.keys[key][l-1][1]
            








        
