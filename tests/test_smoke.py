from main import discover_tools


def test_example_tool_is_discovered():
    names = [module.APP_NAME for module in discover_tools()]
    assert "Input Validation Example" in names
