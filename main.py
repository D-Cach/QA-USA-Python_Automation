import data
import helpers
from data import URBAN_ROUTES_URL
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Add in S8
    def test_set_route(self):

        print("function created for set route")

        pass

    # Add in S8
    def test_select_plan(self):

        print("function created for select plan")

        pass

    # Add in S8
    def test_fill_phone_number(self):

        print("function created for fill phone number")

        pass

    # Add in S8
    def test_fill_card(self):

        print("function created for fill card")

        pass

    # Add in S8
    def test_comment_for_driver(self):

        print("function created for comment for driver")

        pass

    # Add in S8
    def test_order_blanket_and_handkerchiefs(self):

        print("function created for order blanket and handkerchiefs")

        pass

    # Add in S8
    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            pass

        print("function created for order 2 ice creams")
        pass

    # Add in S8
    def test_car_search_model_appears(self):

        print("function created for car search model appears")

        pass
