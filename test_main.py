
import main

def test_soma():
	app = main.app.test_client()
	res = app.get("/soma/5/8")
	assert res.data == b"13"
