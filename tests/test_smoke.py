import main
from main import discover_tools


def test_example_tool_is_discovered():
    names = [module.APP_NAME for module in discover_tools()]
    assert "Example Tool" in names


def test_help_option_keeps_tool_menu_visible(monkeypatch, capsys):
    choices = iter(["h", "0"])
    prompts = []
    monkeypatch.setattr("builtins.input", lambda prompt: (prompts.append(prompt), next(choices))[1])

    main.main()

    output = capsys.readouterr().out
    assert output.count("Expected input: H for help, a tool number to run it, or 0 to exit.") == 1
    assert "Example Tool" in output
    assert output.count("H. Help / Instructions") == 2
    assert output.index("H. Help / Instructions") < output.index("1. Example Tool")
    assert "Tools are discovered from modules in tools/" in output
    assert prompts == ["Choose a tool: ", "Choose a tool: "]


def test_help_is_available_when_no_tools(monkeypatch, capsys):
    monkeypatch.setattr(main, "discover_tools", lambda: [])
    choices = iter(["help", "0"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(choices))

    main.main()

    output = capsys.readouterr().out
    assert "Expected input: H for help, a tool number to run it, or 0 to exit." in output
    assert "No tools are available yet." in output
    assert output.count("H. Help / Instructions") == 2
    assert "Enter H (or type `help`)" in output
