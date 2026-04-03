class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target-position) / 2
        speed_of_cars = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)
        fleet = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if len(fleet) == 0:
                fleet.append(time)

            if time > fleet[-1]:
                fleet.append(time)

        return len(fleet)
