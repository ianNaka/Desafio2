def test_create_task(client):
    # Criar projeto para associar
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Tarefa"}
    ).json()

    response = client.post(
        "/tasks/",
        json={
            "title": "Tarefa Teste",
            "description": "Descrição tarefa",
            "project_id": proj["id"]
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Tarefa Teste"
    assert data["project_id"] == proj["id"]

def test_list_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_task_detail(client):
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Detalhe Tarefa"}
    ).json()

    task = client.post(
        "/tasks/",
        json={"title": "Tarefa Detalhe", "project_id": proj["id"]}
    ).json()

    response = client.get(f"/tasks/{task['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task["id"]

def test_update_task(client):
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Update Tarefa"}
    ).json()

    task = client.post(
        "/tasks/",
        json={"title": "Tarefa Antes", "project_id": proj["id"]}
    ).json()

    response = client.put(
        f"/tasks/{task['id']}",
        json={"title": "Tarefa Depois", "completed": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarefa Depois"
    assert data["completed"] is True

def test_delete_task(client):
    proj = client.post(
        "/projects/",
        json={"name": "Projeto Delete Tarefa"}
    ).json()

    task = client.post(
        "/tasks/",
        json={"title": "Tarefa Para Deletar", "project_id": proj["id"]}
    ).json()

    response = client.delete(f"/tasks/{task['id']}")
    assert response.status_code == 204

    response = client.get(f"/tasks/{task['id']}")
    assert response.status_code == 404