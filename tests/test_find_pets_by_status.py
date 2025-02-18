import pytest
from endpoints.find_pets_by_status import FindPetsByStatus


class TestFindPetsByStatus:

    @pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
    def test_find_pets_by_status(self, status):
        self.status_finder = FindPetsByStatus()
        self.status_finder.find_pets_by_status(status)