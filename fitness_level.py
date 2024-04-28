import json

class FitnessIndicator:
    """ Create a FitnessIndicator object"""
    def __init__(self, file_location):
        """
        Inputs: push up, pull up, crunches, squats scores and 5km time
        Method: normalize and give a score
        """
    
        with open(file_location, 'r') as file:
            file = json.load(file)

        self.push_up = file["push_up"]
        self.pull_up = file["pull_up"]
        self.squats = file["squat"]
        self.fivekm_time = file["fivekm_time"]
        self.crunches = file["crunches"]

    def calculate_normalize_score(self, score, min_score, max_score):
        score = float(score)
        normalized_score = int(max(((score - min_score)/ \
                                      (max_score - min_score)), 0) * 100)
        return normalized_score
    

file_location = 'test/demo.json'
fitness_indicator = FitnessIndicator(file_location)
