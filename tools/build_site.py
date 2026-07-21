from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="构建 study 古诗诵读 MkDocs 站点")
    parser.add_argument("--strict", action="store_true", help="将 MkDocs 警告视为错误")
    args = parser.parse_args()

    command = [
        sys.executable,
        "-m",
        "mkdocs",
        "build",
        "--config-file",
        str(ROOT / "mkdocs.yml"),
    ]
    if args.strict:
        command.append("--strict")
    return subprocess.call(command, cwd=ROOT)


if __name__ == "__main__":
    raise SystemExit(main())