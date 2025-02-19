import pytest
import random

from endpoints.delete_purchase_order_by_id import DeletePurchaseOrderById


class TestDeletePurchaseOrderById:

    def test_delete_purchase_order_by_id(self, place_an_order_for_a_pet):
        self.order_id_deleter = DeletePurchaseOrderById()
        self.order_id_deleter.delete_purchase_order_by_id(place_an_order_for_a_pet)