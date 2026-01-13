print("🚗 LV MOBILITY - SACHIN BACKEND LIVE!")
print("=" * 40)
vehicles = [
    {"id": 1, "name": "Innova BL01AB1234", "fuel": 75},
    {"id": 2, "name": "Honda BL02CD5678", "fuel": 92}, 
    {"id": 3, "name": "Etios BL03EF9012", "fuel": 45},
    {"id": 4, "name": "Creta BL04GH3456", "fuel": 88},
    {"id": 5, "name": "Swift BL05IJ7890", "fuel": 12}
]
for v in vehicles:
    status = "✅ ONLINE" if v['fuel'] > 20 else "⚠️ CRITICAL"
    print(f"#{v['id']:2d} {v['name']:<16} ⛽{v['fuel']:3d}% {status}")