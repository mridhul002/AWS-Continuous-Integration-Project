from simple_python_app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_home_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Simple Calculator" in r.data

def test_add_post(client):
    r = client.post("/", data={"a":"2", "b":"3", "operation":"add"})
    assert r.status_code == 200
    assert b"Result: 5.0" in r.data or b"Result: 5" in r.data

def test_metrics_includes_counter(client):
    # hit an endpoint to generate metrics
    client.get("/")
    r = client.get("/metrics")
    assert r.status_code == 200
    assert b"http_requests_total" in r.data

