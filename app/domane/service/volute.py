from abc import ABC, abstractmethod

from aiohttp import ClientSession

from app.core.config import settings

from app.domane.entity.volute import CurrentExchangeRate

class VoluteClientInterface(ABC):
    @abstractmethod
    async def actual_course():
        """метод возвращает курс валют"""
        raise NotImplementedError


class VoluteClient(VoluteClientInterface):
    _volute_data: str

    def __init__(self, volute_data) -> None:
        """
        Arguments:
            volute_data:str -- название валюты большими английскими буквами(тикер)
        """
        self._volute_data = volute_data

    async def actual_course(self) -> CurrentExchangeRate | None:
        """Возвращает курс валюты"""
        return await self._get_volute()

    async def _get_volute(self) -> CurrentExchangeRate | None:
        """Возвращает курс доллара"""
        volute_data = await self._request_volute()

        if volute_collection := volute_data.get('Valute', None):
            if request_volute := volute_collection.get(self._volute_data):
                return CurrentExchangeRate(
                    volute_name= request_volute.get("CharCode"),
                    value=str(request_volute.get("Value")),
                    date=volute_data.get("Date")
                )

    async def _request_volute(self) -> dict:
        """метод для запроса всей информации в json"""
        async with ClientSession() as session:
            async with session.get(settings.VOLUTE_URL) as request:
                return await request.json(content_type=None)
