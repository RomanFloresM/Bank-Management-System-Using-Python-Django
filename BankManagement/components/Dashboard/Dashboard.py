from django_viewcomponent import component
from menu.models import BillUser

@component.register("Dashboard")
class Dashboard(component.Component):
    template_name = "Dashboard/Dashboard.html"

    def __init__(self, usr, usrname):
        self.usr = usr
        self.usrname = usrname

    def get_total_bill(self):
        return BillUser.objects.get(id=self.usr).wallet
    
    def abonar(self, amount):
        return BillUser.objects.get(id=self.usr).updateWallet(amount)