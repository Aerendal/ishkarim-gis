# ishkarim-gis

> GIS i mapy 3D: CesiumJS, PMTiles, MapLibre, cyfrowe bliźniaki, Overture Maps.

## Instalacja

```bash
pip install -e projects/ishkarim-gis
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-gis
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_gis as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **10 katalogów** obszaru `gis`:

- `AI for Generative Environments — Highlights`
- `Atrybucja OSM - GBA: dobre praktyki licencyjne`
- `Cesium: lokalny pokaz terenu quantized‑mesh`
- `CesiumJS 1.137 + Blender 4.5.6 LTS – duet do symulacji 3D`
- `Godot lokalna demonstracja 3D‑Tiles_04`
- `Lokalne pipeline’y 3D-twin (PMTiles-3D-Tiles)`
- `New open-source spatial  and 3D tools`
- `Nowe narzędzia do symulacji 3D`
- … i 2 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### AI for Generative Environments — Highlights

# WORK: AI for Generative Environments — Highlights
## 0-Metadane
- Katalog: AI for Generative Environments — Highlights
- Pliki: 12 (bez placeholderów, z 60 łącznie)
- Tagi: generative-environments, 3D, audio, lighting, DMX, Godot4, Python, offline-first, procedural, runtime

### Atrybucja OSM - GBA: dobre praktyki licencyjne

# Atrybucja OSM - GBA: dobre praktyki licencyjne
## 0-Metadane
- Pliki: 8
- Tagi: OSM, ODbL, GlobalBuildingAtlas, CC-BY-NC, licencjonowanie, GIS, atrybucja, JSON Schema, ASSET_LICENSE
- Status: done

### Cesium: lokalny pokaz terenu quantized‑mesh

# WORK: Cesium: lokalny pokaz terenu quantized‑mesh
## 0-Metadane
- Katalog: Cesium: lokalny pokaz terenu quantized‑mesh
- Pliki: 18
- Tagi: CesiumJS, quantized-mesh, GeoTIFF, terrain, offline, CTB, GDAL, Docker, LOD, tileset


## Struktura projektu

```
ishkarim-gis/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 10 katalogów-źródeł
├── src/
│   └── ishkarim_gis/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_gis.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-gis/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
