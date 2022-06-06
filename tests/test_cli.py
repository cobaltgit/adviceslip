from typer.testing import CliRunner

from adviceslip.cli import app

runner = CliRunner()


def test_cli_random():
    result = runner.invoke(app, ["random"])
    assert result.exit_code == 0


def test_cli_id():
    _id = 12
    result = runner.invoke(app, ["id", str(_id)])
    assert result.exit_code == 0 and "Always block trolls." in result.stdout


def test_cli_search():
    query = "good"
    result = runner.invoke(app, ["search", query])
    assert result.exit_code == 0 and all(query in result.lower() for result in result.stdout.splitlines())
