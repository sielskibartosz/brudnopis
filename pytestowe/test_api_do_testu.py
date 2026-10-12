
import pytest

from python_ex.api_do_testu import WeatherService, WeatherApiClient


class Test_WeatherAPI():


    def test_is_warm(self, mocker):
        #data preparation
        mock_weather_api_client = mocker.Mock()
        mock_weather_api_client.get_temperature.return_value = 25.0


        service = WeatherService(mock_weather_api_client)
        print(service.is_warm("wroclaw"))


    def test_is_city_known_value_error(self,mocker):
        api_client = mocker.Mock()
        api_client.get_temperature.side_effect = ValueError("Unknown city")

        service=WeatherService(api_client)
        assert False == service.is_city_known("Breslau")

    def test_is_city_known_no_exception(self,mocker):
        mocker.patch.object(WeatherApiClient, 'get_temperature', return_value=True)
        service = WeatherService(WeatherApiClient)
        assert True == service.is_city_known("Wroclaw")



