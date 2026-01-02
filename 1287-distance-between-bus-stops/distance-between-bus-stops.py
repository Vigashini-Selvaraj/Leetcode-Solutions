class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start,destination=destination,start
        clock=sum(distance[start:destination])
        total=sum(distance)
        anti=total-clock
        return min(clock,anti)
        

        