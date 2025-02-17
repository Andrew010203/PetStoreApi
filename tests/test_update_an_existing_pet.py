from endpoints.update_an_existing_pet import UpdateAnExistingPet


class TestUpdateAnExistingPet:
    def test_update_an_existing_pet(self, add_a_new_pet_to_the_store):
        self.pet_updater = UpdateAnExistingPet()
        self.pet_updater.update_an_existing_pet()