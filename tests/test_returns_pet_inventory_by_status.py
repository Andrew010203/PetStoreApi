from endpoints.return_pet_inv_by_status import ReturnsPetInventoryByStatus


class TestReturnsPetInventoryByStatus:

    def test_returns_pet_inventory_by_status(self):
        self.inv_returner = ReturnsPetInventoryByStatus()
        self.inv_returner.returns_pet_inventory_by_status()