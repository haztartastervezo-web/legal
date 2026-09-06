#!/usr/bin/env python3
"""Post-generation QA for Enila legal pages.

This tool intentionally does NOT generate legal language. The authoritative
/legal-docs workflow must first discover current app locales and build pages
from verified code facts + current official requirements. This validator then
checks structural/semantic invariants that must never regress.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ["clusters", "number_puzzle", "cryptogram", "magnet_grid", "household", "word_album"]
DOCS = ["privacy_policy", "manage_consent", "terms_of_use"]
DANGEROUS_EN = [
    r"By using (?:the )?(?:app|App).*agree to (?:this )?(?:privacy|Privacy)",
    r"decline.*(?:will|you'll).*non-personalized ads",
    r"must be at least 16.*use the app",
    r"Firebase Analytics.*anonymous",
    r"uninstall.*deletes all.*cloud",
]


def locales(folder: Path) -> set[str]:
    out = set()
    for p in folder.glob("privacy_policy.*.html"):
        out.add(p.name[len("privacy_policy.") : -len(".html")])
    return out


def main() -> int:
    failures: list[str] = []
    for app in ACTIVE:
        folder = ROOT / app
        if not folder.is_dir():
            failures.append(f"{app}: missing folder")
            continue
        locs = locales(folder)
        if not locs:
            failures.append(f"{app}: no localized privacy files")
            continue
        for loc in sorted(locs):
            paths = [folder / f"{doc}.{loc}.html" for doc in DOCS]
            missing = [str(p.relative_to(ROOT)) for p in paths if not p.exists()]
            if missing:
                failures.append(f"{app}/{loc}: missing {', '.join(missing)}")
                continue
            payloads = [p.read_bytes() for p in paths]
            if not (payloads[0] == payloads[1] == payloads[2]):
                failures.append(f"{app}/{loc}: Privacy/Consent/Terms canonical pages drifted")
            text = payloads[0].decode("utf-8", errors="replace")
            if "2026" not in text:
                failures.append(f"{app}/{loc}: missing update year")
            if "haztartastervezo@gmail.com" not in text:
                failures.append(f"{app}/{loc}: missing privacy contact")
            if loc == "en":
                for pattern in DANGEROUS_EN:
                    if re.search(pattern, text, flags=re.I | re.S):
                        failures.append(f"{app}/{loc}: dangerous legacy wording: {pattern}")
        for doc in DOCS:
            if not (folder / f"{doc}.html").exists():
                failures.append(f"{app}: missing default {doc}.html")

    if failures:
        print("LEGAL QA: FAIL")
        for item in failures:
            print(f"- {item}")
        return 1
    print("LEGAL QA: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
