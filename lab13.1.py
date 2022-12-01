class APPLE():
    def __init__(self,sort,colour,mass,diameter):
         self.sort = sort
         self.colour = colour
         self.mass  = mass
         self.diameter = diameter
         
    def change_colour(self):
        new_colour = str(input("Введіть новий колір: "))
        self.colour = new_colour
        
    def show(self):
        print("Сорт:",self.sort,",колір:",self.colour ,",маса(г):",self.mass, ",діаметр(см):",self.diameter)
        
a = APPLE("чорний принц","червоний",200,5)
a.show()
a.change_colour()
a.show()