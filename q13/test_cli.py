import subprocess
import sys


def test_greet_normal_name():
    r = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "25020007016"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0
    assert "Hello, 25020007016!" in r.stdout


def test_blank_name_exits_2():
    r = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", " "],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 2
