#!/usr/bin/env python3
"""
demo.py — demo ishkarim-gis

Mapy 3D offline — CesiumJS, PMTiles, cyfrowe bliźniaki bez chmury

Uruchomienie:
    python projects/ishkarim-gis/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_gis as m

docs = m.load_knowledge_index()
cesium_docs  = [d for d in docs if "cesium" in d["name"].lower() or "3d" in d["name"].lower()]
pmtiles_docs = [d for d in docs if "pmtile" in d["name"].lower() or "maplibre" in d["name"].lower()]
osm_docs     = [d for d in docs if "osm" in d["name"].lower() or "overture" in d["name"].lower()]

print(f"GIS/Mapy 3D — {len(docs)} katalogów wiedzy")
print(f"  CesiumJS/3D:   {len(cesium_docs)}")
print(f"  PMTiles/MapLibre: {len(pmtiles_docs)}")
print(f"  OSM/Overture:  {len(osm_docs)}")
print()
for d in docs[:4]:
    print(f"  [{d['maturity']:8s}] {d['name'][:65]}")

