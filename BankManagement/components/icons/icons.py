from django_viewcomponent import component

@component.register("icons")
class icons(component.Component):
    template_name = "icons/icons.html"
    def __init__(self, ico, tittle, url):
        self.ico = ico
        self.tittle = tittle
        self.url = url
    