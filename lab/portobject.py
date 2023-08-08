from . import linkobject

class Port:
    def __init__(self, apiOutput):
        for property in apiOutput:
            setattr(self, property, apiOutput[property])

    def addLinks(self, links):
        self.links = {}
        filteredLinks = [link for link in links
                         if self.id in [link["interface_a"], link["interface_b"]]]
        
        if len(filteredLinks) != 0:
            for link in filteredLinks:
                self.links[link["id"]] = linkobject.Link(link)
    
    def __str__(self):
        return f"{self.id}, {self.name}"