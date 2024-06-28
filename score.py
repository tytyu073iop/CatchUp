import json
import os
import copy

class Score:
    def __init__(self, members, filename = ''):
        self.members = members
        self.score = {}
        self.scores = []
        for member in members:
            self.score[member] = 0
        if filename != '':
            self.filename = filename
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    file.write('[]')
                    print('creating file')
            self.loadFromFile(filename)
    def increase(self, n, member):
        self.score[member] += n
    def save(self):
        self.scores.append(copy.deepcopy(self.score))
    def saveToFile(self, filename = ''):
        with open(filename if filename != '' else self.filename, 'w') as file:
            json.dump(self.scores, file)
    def loadFromFile(self, filename = ''):
        with open(filename if filename != '' else self.filename, 'r') as file:
            self.scores = json.load(file)

