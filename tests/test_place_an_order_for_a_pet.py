from endpoints.place_an_order_for_a_pet import PlaceAnOrderForAPet


class TestPlaceAnOrderForAPet:

    def test_place_an_order_for_a_pet(self):
        self.order_placer = PlaceAnOrderForAPet()
        self.order_placer.place_an_order_for_a_pet()