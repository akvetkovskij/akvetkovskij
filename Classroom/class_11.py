import asyncio


async def foo(i):
    for _ in range(10):
        await asyncio.sleep(1)
        print(i)


async def main():
    tasks = [asyncio.create_task(foo(j)) for j in range(10)]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
