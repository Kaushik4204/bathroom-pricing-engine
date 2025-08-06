from pricing_logic.material_db import get_material_cost

def test_material_cost():
    assert get_material_cost("replace toilet")["cost"] == 80
    assert get_material_cost("install vanity")["cost"] == 100
