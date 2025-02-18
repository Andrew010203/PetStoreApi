from endpoints.find_purchase_order_by_id import FindPurchaseOrderById


class TestFindPurchaseOrderById:

    def test_find_purchase_order_by_id(self, place_an_order_for_a_pet):
        self.order_id_finder = FindPurchaseOrderById()
        self.order_id_finder.find_purchase_order_by_id(place_an_order_for_a_pet)