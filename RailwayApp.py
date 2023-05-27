class RailwayForm:
    fromtype = "RailwayForm"
    def display(self):
        print("Name is ",self.name)
        print("Train is ",self.train)
        
Application = RailwayForm()
Application.name = "Akash"
Application.train = "Rajdhani Express"
Application.display()
