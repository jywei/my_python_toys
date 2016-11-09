class Music:
    def notes(self, note):
        self.data = note

    def display(self):
        print(self.data)

x = Music()
y = Music()

x.notes("Damnnnnn")
y.notes("Rockkkkkk")

x.display()
y.display()

class Musician(Music):
    def display(self):
        print('The notes are "%s"' % self.data)

Ryan = Musician()
Ryan.notes("Folks, folk!")
Ryan.display()
