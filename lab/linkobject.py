class Link:
    def __init__(self, apiOutput):
        for property in apiOutput:
            setattr(self, property, apiOutput[property])
    
    def __str__(self):
        return f"{self.id}, {self.name}"