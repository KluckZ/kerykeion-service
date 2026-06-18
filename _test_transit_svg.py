"""Smoke test del endpoint /generate-transit-svg. Correr con el server arriba en :8000."""
import requests

payload = {
    "natal": {"name": "Test", "year": 1990, "month": 5, "day": 15, "hour": 14, "minute": 30,
              "latitude": 4.61, "longitude": -74.08, "city": "Bogota", "timezone": "America/Bogota"},
    "transit": {"year": 2026, "month": 6, "day": 18, "hour": 12, "minute": 0,
                "latitude": 4.61, "longitude": -74.08, "city": "Bogota", "timezone": "America/Bogota"},
}
r = requests.post("http://localhost:8000/generate-transit-svg", json=payload, timeout=30)
print("status", r.status_code)
data = r.json()
assert data["success"] is True, data
assert data["svg"].lstrip().startswith("<svg") or "<svg" in data["svg"][:200], data["svg"][:200]
print("SVG bytes:", len(data["svg"]))
print("OK")
