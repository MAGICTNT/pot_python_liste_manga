class Livre:
    nom = ""
    volume = 0
    style = 0

    def __int__(self, nom, volume, style):
        self.nom = nom
        self.volume = volume
        self.style = style

    def get_nom(self):
        return self.nom

    def set_nom(self, new_nom):
        self.nom = new_nom

    def get_volume(self):
        return self.volume

    def set_volume(self, new_volume):
        self.volume = new_volume

    def get_style(self):
        return self.style

    def set_style(self, new_style):
        self.style = new_style

    def to_string(self):
        return self.nom, self.volume, self.style
