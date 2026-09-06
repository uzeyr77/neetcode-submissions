class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a car = [pos, speed]
        # mononotic stack using pos of the car
        # calculate the time, using the fomula... then the set() of the times is #
        # of fleets
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        # sort by position in increasing order
        
        # use a monotonic desc stack based on time to get # of unique fleets
        unique_fleets = []
        for p, s in sorted(cars)[::-1]:
            time = (target -p)/s
            unique_fleets.append(time)
            if len(unique_fleets) >= 2 and unique_fleets[-1] <= unique_fleets[-2]:
                unique_fleets.pop()
        
        return len(unique_fleets)

        



        

        

