from django_viewcomponent import component
from django_viewcomponent.fields import RendersManyField

@component.register("Sidebar")
class SidebarComponent(component.Component):
    Element = RendersManyField(required= True, component='iconsMenu')
    template_name = "Sidebar/sidebar.html"
    usuario = ""

    def __init__(self, usuario):
        self.usuario = usuario