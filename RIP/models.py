import json


class Cinephile:
    def __init__(self):
        try:
            with open("filmy.json", "r") as f:
                self.filmy = json.load(f)
        except FileNotFoundError:
            self.filmy = []

    def all(self):
        return self.filmy

    def get (self, id):
        give_film = [film for film in self.all() if film['id'] == id]
        if give_film:
            return give_film[0]
        return []

    def create(self, data):
        self.filmy.append(data)
        self.save_all()
    
    def save_all(self):
        with open("filmy.json", "w") as f:
            json.dump(self.filmy, f)

    def update(self, id, data):
        film = self.get(id)
        if film:
            index = self.filmy.index(film)
            self.filmy[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        film = self.get(id)
        if todo:
            self.filmy.remove(film)
            self.save_all()
            return True
        return False

kinofil = Cinephile()