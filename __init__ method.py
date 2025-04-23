class Computer:
    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram
    def Configuration(self):
        print(f"CPU is {self.cpu}, and ram is {self.ram} GB")

comp1= Computer("i5",8)

comp1.Configuration()

# Computer is the class
# comp1 is the object
# Comp1 has methods of class
# by default when we call config first the init method is called automatically
