"""Lous Lagoon Desktop — A local helper for Lou's Lagoon island folders, lagoon shops, and watercolor photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='lous_lagoon_desktop',
        description="A local helper for Lou's Lagoon island folders, lagoon shops, and watercolor photos.",
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Lous Lagoon Desktop')
    print('Keep the lagoon on disk before a tide update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
