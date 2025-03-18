from django_viewcomponent import component

@component.register("iconsMenu")
class iconsMenu(component.Component):
    template_name = "iconsMenu/iconsMenu.html"
    def __init__(self, ico, tittle, url):
        self.ico = ico
        self.tittle = tittle
        self.url = url
    