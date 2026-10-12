# weather_service.py
class WeatherApiClient:
    def get_temperature(self, city: str) -> float:
        """
        Udaje zewnętrzne API (np. HTTP)
        """
        raise NotImplementedError


class WeatherService:
    def __init__(self, api_client: WeatherApiClient):
        self.api_client = api_client

    def is_warm(self, city: str) -> bool:
        """
        Zwraca True jeśli temperatura >= 20 stopni
        """
        temperature = self.api_client.get_temperature(city)
        return temperature >= 20

    def is_city_known(self, city: str) -> bool:
        try:
            self.api_client.get_temperature(city)
            return True
        except ValueError:
            return False
