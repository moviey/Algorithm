class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result, bowl = 0, capacity
        for i,plant in enumerate(plants):            
            if bowl >= plant :
                bowl -= plant
            else :
                result += (2*i)
                bowl = capacity
                bowl -= plant
        return result + len(plants)