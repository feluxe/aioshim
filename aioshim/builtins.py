from collections import abc


class aenumerate(abc.AsyncIterator):

    def __init__(self, aiterable, start=0):
        self._ait = aiterable
        self._i = start - 1

    async def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self._ait.__anext__()
        self._i += 1

        return self._i, val
