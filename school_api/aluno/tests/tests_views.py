from django.urls import reverse


def test_responsavel_list_status_code(db, client):
    response = client.get(reverse('responsavel-list'))
    assert response.status_code == 200


def test_aluno_list_status_code(db, client):
    response = client.get(reverse('aluno-list'))
    assert response.status_code == 200
