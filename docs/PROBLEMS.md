# PROBLEMS — ishkarim-gis

> Mapy 3D offline — CesiumJS, PMTiles, cyfrowe bliźniaki bez chmury

## ✅ Co ten projekt rozwiązuje

- ✅ Lokalne renderowanie terenu 3D (quantized-mesh) bez płatnego Cesium Ion
- ✅ PMTiles → MapLibre pipeline działający offline (plik zamiast tile serwera)
- ✅ Integracja danych GBA/OSM z silnikiem gry (Godot 4)
- ✅ Cyfrowy bliźniak budynków z danych publicznych (Overture Maps)
- ✅ Minimalny ślad licencyjny — OSM/ODbL, bez płatnych API

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Real-time aktualizacje danych geograficznych
- ❌ Routing i nawigacja — tylko wizualizacja, nie pathfinding
- ❌ Indoor mapping — dane wewnętrzne budynków
- ❌ AR/VR integracja — planarna wizualizacja

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **Overture Maps 2026** — format i jakość danych zmienia się regularnie (breaking changes)
- ⚠️ **PMTiles generacja** dużych regionów zajmuje >30 min na CPU
- ⚠️ **CesiumJS 1.137** — breaking API w terrain providers względem 1.12x
- ⚠️ **Wysokości budynków GBA** — błąd ~2m w gęstej zabudowie miejskiej

---

## 🎯 Przypadki użycia

- 🎯 Symulacja środowiska miejskiego dla agentów autonomicznych
- 🎯 Demo dla klienta z lokalnym podglądem terenu bez kosztów API
- 🎯 Prototyp gry z prawdziwą geografią (open-world z OSM)
- 🎯 Aplikacja GIS offline dla terenów bez internetu (wojsko, katastrofy)

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
