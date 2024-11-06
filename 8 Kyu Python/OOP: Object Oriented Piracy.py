class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    
    def is_worth_it(self):
        crew_weight = 1.5 * self.crew
        cargo_weight = self.draft - crew_weight
        return True if cargo_weight > 20 else False