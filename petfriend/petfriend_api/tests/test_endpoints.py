import pytest
from petfriend_api.models import Pet, PetFriendUser


@pytest.mark.django_db
def test_create_pet(client):
    response = client.get('/pet_api/pet_detail/1/')
    assert response.status_code == 201
    pet = Pet.objects.filter(pk=1)
    assert response.data.name == pet.name