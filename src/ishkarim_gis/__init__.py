"""
ishkarim_gis — moduł z obszaru gis.

GIS i mapy 3D: CesiumJS, PMTiles, MapLibre, cyfrowe bliźniaki, Overture Maps.

Źródła: 10 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "gis"



MODULES: list[str] = [
    'AI for Generative Environments — Highlights',
    'Atrybucja OSM - GBA: dobre praktyki licencyjne',
    'Cesium: lokalny pokaz terenu quantized‑mesh',
    'CesiumJS\xa01.137\xa0+\xa0Blender\xa04.5.6\xa0LTS\xa0– duet do symulacji 3D',
    'Godot lokalna demonstracja 3D‑Tiles_04',
    'Lokalne pipeline’y 3D-twin (PMTiles-3D-Tiles)',
    'New open-source spatial  and 3D tools',
    'Nowe narzędzia do symulacji 3D',
    'Nowe wdrożenia: AI w środowiskach kreatywnych',
    'Offline’owy pipeline PMTiles → MapLibre z CityJSON',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "gis"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
