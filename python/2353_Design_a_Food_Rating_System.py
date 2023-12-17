class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}

        self.cuisine_food_map = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating_map[food] = rating
            self.food_cuisine_map[food] = cuisine
            self.addToHeap(cuisine, rating, food)

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating_map[food] = newRating
        cuisine = self.food_cuisine_map[food]
        self.addToHeap(cuisine, newRating, food)

    def highestRated(self, cuisine: str) -> str:
        best_rating, best_food = self.getBestFood(cuisine)

        while self.food_rating_map[best_food] != best_rating:
            heappop(self.cuisine_food_map[cuisine])
            best_rating, best_food = self.getBestFood(cuisine)

        return best_food
        
    def addToHeap(self, cuisine, rating, food):
        heappush(self.cuisine_food_map[cuisine], (-rating, food))

    def getBestFood(self, cuisine):
        rating, food = self.cuisine_food_map[cuisine][0]
        return (-rating, food)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)