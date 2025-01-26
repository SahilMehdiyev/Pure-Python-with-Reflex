import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE) 
    
    def to_about_us(self):
        # print('clickeddddd-----------')
        return rx.redirect(routes.ABOUT_US_ROUTE) 