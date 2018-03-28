
# aioshim


## Description

The main purpose of this lib is to provide *asyncio* compatible versions of the functions in the standard library. E.g. `itertools.chain()` doesn't work with `async_generators`, etc.

I'm sure the stdlib will catch up with this sooner or later. This lib is for those who need a shim as soon as possible. 



## Requirements

aioshim requires Python `>= 3.6`


## Install

    pip install aioshim

or

    pipenv install aioshim


## Development

Just clone the repo and run:

    pipenv install --dev

This project uses [yapf](https://github.com/google/yapf) formatter.


# Library Documentation


## builtins

### `aenumerate`

Async version of: [enumerate](https://docs.python.org/3.6/library/functions.html#enumerate)

Example:

```python

async for i in aenumerate(chain(a_gen, range(10))):
    print(i)

```

## itertools


### `itertools.chain(*iterables)`

Async version of: [chain](https://docs.python.org/3.6/library/itertools.html#itertools.chain)

This function can handle `AsyncGeneratorType`.

Example:

```python
# Use with async_generator:
async for i in chain(my_async_gen1, my_async_gen2):
    print(i)

# Allows for mixing normal generators with async generators:
async for i in chain(my_async_gen, range(10)):
    print(i)
```


### `itertools.chain_from_iterable(iterable)`

Async version of: [from_iterable](https://docs.python.org/3.6/library/itertools.html#itertools.chain.from_iterable)

This function can handle `AsyncGeneratorType`.

Example:

```python
# Use with async_generator:
async for i in chain_from_iterable(my_async_generator):
    print(i)

# Works with normal items as well:
async for i in chain_from_iterable([range(10)]):
    print(i)
```


## More items to come

Pull requests appreciated!



