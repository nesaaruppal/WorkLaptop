import random


class FoodChain:
    def __init__(self):
        self.food_chain = ["Big Fish", "Small Fish",]

    def get_random_organisms(self):
        organism1 = random.choice(self.food_chain)
        organism2 = random.choice(self.food_chain)
        while organism1 == organism2:
            organism2 = random.choice(self.food_chain)
        return organism1, organism2

    def find_links(self, organism1, organism2):
        links = []
        current_organism = organism1
        while current_organism != organism2:
            links.append(current_organism)
            next_organism_index = self.food_chain.index(current_organism) + 1
            if next_organism_index >= len(self.food_chain):
                next_organism_index = 0
            current_organism = self.food_chain[next_organism_index]
        return links

    def compare_positions(self, organism1, organism2):
        links = self.find_links(organism1, organism2)
        if links:
            print(
                f"A link between {organism1} and {organism2} was found. You lose!")
        else:
            print(
                f"{organism1} is higher in the food chain than {organism2}. You win!")


food_chain = FoodChain()
organism1, organism2 = food_chain.get_random_organisms()
print(food_chain.compare_positions(organism1, organism2))
