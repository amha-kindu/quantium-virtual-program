from app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)

def test_visualizer(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=100)
    


