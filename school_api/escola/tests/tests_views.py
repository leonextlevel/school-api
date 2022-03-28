from django.urls import reverse


def test_escola_list_view_status_code(db, client):
    response = client.get(reverse('escola-list'))
    assert response.status_code == 200


def test_escola_list_result(client, escola):
    response = client.get(reverse('escola-list'))
    assert response.data['results'] == [
        {
            "id": escola.id,
            "nome": escola.nome,
            "endereco": escola.endereco
        }
    ]


def test_escola_create(db, client):
    data = {
        "nome": "Teste",
        "endereco": "Rua Teste"
    }
    response = client.post(
        reverse('escola-list'),
        data=data
    )
    assert response.status_code == 201


def test_turma_list_status_code(db, client):
    response = client.get(reverse('turma-list'))
    assert response.status_code == 200


def test_professor_list_status_code(db, client):
    response = client.get(reverse('professor-list'))
    assert response.status_code == 200


def test_disciplina_list_status_code(db, client):
    response = client.get(reverse('disciplina-list'))
    assert response.status_code == 200
