import subprocess
import sys

def test_blank_name_exits_2():
    # 当 name 只含空白字符时，main 应以 SystemExit(2) 结束
    r = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", " "],
        capture_output=True, text=True,
    )
    assert r.returncode == 2
