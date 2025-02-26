from django_viewcomponent import component
from django_viewcomponent.fields import RendersManyField

@component.register("Sidebar")
class SidebarComponent(component.Component):
    Element = RendersManyField(required= True, component='icons')
    template_name = "Sidebar/sidebar.html"