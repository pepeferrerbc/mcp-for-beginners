import asyncio
from mcp.server.fastmcp import FastMCP

# Crear el servidor MCP
mcp = FastMCP(name="Weather MCP Server")


class WeatherTools:
    """Herramientas relacionadas con el clima"""

    @mcp.tool()
    def get_current_weather(self, location: str) -> dict:
        """Obtiene el clima actual de una ubicación específica.

        Args:
            # location: Nombre de la ciudad o ubicación

        Returns:
            Diccionario con temperatura y condiciones actuales
        """
        return {
            "location": location,
            "temperature": 22.5,
            "conditions": "Soleado",
            "humidity": 65,
            "wind_speed": 10,
        }

    @mcp.tool()
    def get_forecast(self, location: str, days: int = 3) -> dict:
        """Obtiene el pronóstico del clima para varios días.

        Args:
            location: Nombre de la ciudad o ubicación
            days: Número de días del pronóstico (1-7)

        Returns:
            Diccionario con el pronóstico por días
        """
        if days < 1 or days > 7:
            return {"error": "Los días deben estar entre 1 y 7"}

        return {
            "location": location,
            "forecast": [
                {
                    "day": i + 1,
                    "date": f"2025-11-{13 + i}",
                    "temperature_max": 24 + i,
                    "temperature_min": 15 + i,
                    "conditions": "Parcialmente nublado" if i % 2 == 0 else "Soleado",
                    "precipitation_chance": 20 + (i * 10),
                }
                for i in range(days)
            ],
        }


# Registrar las herramientas
weather_tools = WeatherTools()

# Iniciar el servidor
if __name__ == "__main__":
    # En fastmcp 2.x, se usa mcp.run() en lugar de serve_stdio
    mcp.run()
