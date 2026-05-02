#!/usr/bin/env python3
"""Emit ``string_therapy/quint_specs/string_therapy_ui.qnt`` from ``appspecifications.ipynb``.

Edit the ``STRING_THERAPY_UI_QNT`` assignment in that notebook, then run::

    pixi run quint-export

or execute the notebook cell that calls ``write_quint_spec_file``.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NB = ROOT / "appspecifications.ipynb"
OUT = ROOT / "string_therapy" / "quint_specs" / "string_therapy_ui.qnt"

_PATTERN = re.compile(
    r"STRING_THERAPY_UI_QNT\s*=\s*(?:r)?\"\"\"(.*?)\"\"\"",
    re.DOTALL,
)


def main() -> None:
    raw = json.loads(NB.read_text(encoding="utf-8"))
    for cell in raw.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", []))
        m = _PATTERN.search(src)
        if not m:
            continue
        body = m.group(1).lstrip("\n").rstrip() + "\n"
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(body, encoding="utf-8")
        print(f"Wrote {OUT.relative_to(ROOT)} ({len(body)} bytes)")
        return
    print("No STRING_THERAPY_UI_QNT = r\"\"\"...\"\"\" in", NB, file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
