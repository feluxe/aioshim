import random
import asyncio as aio
from aioshim.itertools import chain, chain_from_iterable
from aioshim.builtins import aenumerate
import itertools


# TODO: This should get some improvements. ;)


async def produce_numbers(x, name='a'):
    await aio.sleep(random.uniform(0, 1))
    return [str(x) + name]


async def main():

    # Test async chain
    coros1 = (produce_numbers(i, 'a') for i in range(0, 3))
    coros2 = (produce_numbers(i, 'b') for i in range(0, 3))
    futs1 = aio.as_completed([f for f in coros1])
    futs2 = aio.as_completed([f for f in coros2])

    a_gen1 = (await i for i in futs1)
    a_gen2 = (await i for i in futs2)

    async for i in aenumerate(chain(a_gen1, a_gen2, range(10))):
        print(i)

    async for i in chain_from_iterable([range(10)]):
        print(i)


if __name__ == '__main__':
    loop = aio.get_event_loop()
    loop.run_until_complete(main())
