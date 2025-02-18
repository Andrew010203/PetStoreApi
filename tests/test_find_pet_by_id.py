from endpoints.find_pet_by_id import FindPetsById


class TestFindPetsById:

    def test_find_pets_by_id(self, add_a_new_pet_to_the_store):
        self.pet_id_finder = FindPetsById()
        self.pet_id_finder.find_pets_by_id(add_a_new_pet_to_the_store)