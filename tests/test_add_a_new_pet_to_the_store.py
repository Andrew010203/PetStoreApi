from endpoints.add_a_new_pet_to_the_store import AddANewPetToTheStore


class TestAddANewPetToTheStore:
    def test_add_a_new_pet_to_the_store(self):
        self.add_obj = AddANewPetToTheStore()
        self.add_obj.add_a_new_pet_to_the_store()