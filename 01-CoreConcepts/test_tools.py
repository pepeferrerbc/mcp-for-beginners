"""Script simple para probar las herramientas MCP"""

# Importamos la clase con las herramientas
from mcp_server import WeatherTools

# Creamos una instancia
tools = WeatherTools()

print("=" * 70)
print("🧪 PROBANDO HERRAMIENTAS MCP")
print("=" * 70)

# PRUEBA 1: Clima actual
print("\n📍 PRUEBA 1: Obtener clima actual de Barcelona")
print("-" * 70)
resultado = tools.get_current_weather("Barcelona")
print(f"✅ Resultado: {resultado}")

# PRUEBA 2: Pronóstico de 3 días
print("\n📍 PRUEBA 2: Pronóstico de 3 días para Madrid")
print("-" * 70)
resultado = tools.get_forecast("Madrid", days=3)
print(f"✅ Resultado: {resultado}")

# PRUEBA 3: Pronóstico de 7 días (máximo permitido)
print("\n📍 PRUEBA 3: Pronóstico de 7 días para Valencia")
print("-" * 70)
resultado = tools.get_forecast("Valencia", days=7)
print(f"✅ Resultado: {resultado}")

# PRUEBA 4: Intentar con días inválidos (debe dar error)
print("\n📍 PRUEBA 4: Intentar pronóstico de 10 días (debe fallar)")
print("-" * 70)
resultado = tools.get_forecast("Sevilla", days=10)
print(f"❌ Resultado: {resultado}")

print("\n" + "=" * 70)
print("✅ TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 70)
