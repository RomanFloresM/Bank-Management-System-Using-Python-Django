from django_viewcomponent import component

@component.register("Sidebar")
class SidebarComponent(component.Component):
    template_name = "Sidebar/sidebar.html"
    