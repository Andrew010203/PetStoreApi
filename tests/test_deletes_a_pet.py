from endpoints.deletes_a_pet import DeletesAPet


class TestDeletesAPet:

    def test_deletes_a_pet(self, add_a_new_pet_to_the_store):
        self.pet_deleter = DeletesAPet()
        self.pet_deleter.deletes_a_pet(add_a_new_pet_to_the_store)