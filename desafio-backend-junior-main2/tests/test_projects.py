import uuid

def test_create_project(client):
    response = client.post(
        "/projects/",
        json={"name": "Projeto Teste", "description": "Descrição teste"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Projeto Teste"
    assert "id" in data

def test_list_projects(client):
    response = client.get("/projects/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_project_detail(client):
    # Criar projeto
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Detalhe", "description": "Detalhe teste"}
    ).json()

    response = client.get(f"/projects/{proj['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == proj["id"]
    assert "tasks" in data

def test_update_project(client):
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Update", "description": "Antes"}
    ).json()

    response = client.put(
        f"/projects/{proj['id']}",
        json={"name": "Projeto Atualizado", "description": "Depois"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Projeto Atualizado"

def test_delete_project(client):
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Delete"}
    ).json()

    response = client.delete(f"/projects/{proj['id']}")
    assert response.status_code == 204

    response = client.get(f"/projects/{proj['id']}")
    assert response.status_code == 404