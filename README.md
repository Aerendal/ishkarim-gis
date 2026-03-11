# ishkarim-gis

> **Mapy 3D offline — CesiumJS, PMTiles, cyfrowe bliźniaki bez chmury**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Lokalne renderowanie terenu 3D (quantized-mesh) bez płatnego Cesium Ion
- PMTiles → MapLibre pipeline działający offline (plik zamiast tile serwera)
- Integracja danych GBA/OSM z silnikiem gry (Godot 4)

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-gis

# Demo (10 sekund)
python projects/ishkarim-gis/demo.py
```

## Użycie w kodzie

```python
import ishkarim_gis as m

# Wszystkie 10 katalogi wiedzy obszaru 'gis'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_gis.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Symulacja środowiska miejskiego dla agentów autonomicznych
- Demo dla klienta z lokalnym podglądem terenu bez kosztów API
- Prototyp gry z prawdziwą geografią (open-world z OSM)

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 10 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_gis.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_gis_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_gis.py --quick
```

## Struktura projektu

```
ishkarim-gis/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 10 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_gis/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_gis.py         ← testy jednostkowe
│   └── test_gis_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_gis.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 10 katalogów wiedzy obszaru `gis`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
