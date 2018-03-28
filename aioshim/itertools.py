import itertools
import types
import asyncio as aio


async def chain(*iterables):

    for iterable in iterables:
        if isinstance(iterable, types.AsyncGeneratorType):
            async for i in iterable:
                yield i
        else:
            for i in iterable:
                yield i


async def chain_from_iterable(iterable):

    if isinstance(iterable, types.AsyncGeneratorType):
        async for item in iterable:
            for i in item:
                yield i
    else:
        for item in iterable:
            for i in item:
                yield i
