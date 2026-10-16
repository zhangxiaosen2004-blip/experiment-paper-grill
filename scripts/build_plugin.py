"""Build a skills-only plugin ZIP using Python's standard library."""

import json
from pathlib import Path
import zipfile


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    required = [
        "plugin.json",
        "LICENSE",
        "README.md",
        "README_CN.md",
        "WEB_SETUP_CN.md",
        "assets/icon.svg",
        "skills/experiment-paper-grill/SKILL.md",
    ]
    for relative in required:
        if not (root / relative).is_file():
            raise SystemExit(f"Missing package file: {relative}")
    if manifest["name"] != "experiment-paper-grill":
        raise SystemExit("Unexpected plugin identity")

    paths = {root / relative for relative in required}
    for folder in ("skills", "examples"):
        paths.update(
            path
            for path in (root / folder).rglob("*")
            if path.is_file()
            and not path.is_symlink()
            and "__pycache__" not in path.parts
        )

    output = root.parent / "plugin-packages" / (
        f"{manifest['name']}-plugin-{manifest['version']}.zip"
    )
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(paths):
            archive.write(path, path.relative_to(root).as_posix())

    with zipfile.ZipFile(output) as archive:
        failed = archive.testzip()
        if failed:
            raise SystemExit(f"ZIP integrity error: {failed}")
        assert "plugin.json" in archive.namelist()
        print(f"Created {output} ({len(archive.namelist())} files)")


if __name__ == "__main__":
    main()
