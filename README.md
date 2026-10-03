![Lous Lagoon Desktop](assets/hero.png)

# Lous Lagoon Desktop

*Keep the lagoon on disk before a tide update.*

## Overview

**Lous Lagoon Desktop** is a desktop helper. A local helper for Lou's Lagoon island folders, lagoon shops, and watercolor photos.

Small cozy titles bury folders in Documents.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- Finds the lagoon data folder.
- Copies island and shop files.
- Lists photo albums.
- Writes a short keep report.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/joelallen85/lous-lagoon-desktop

MIT license. See `LICENSE`.
