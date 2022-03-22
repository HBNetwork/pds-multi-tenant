def test_index_with_tenant(client):
    response = client.get('/tenant/')
    assert response.status_code == 200
    assert response.context['request'].tenant_name == 'tenant'