"""
This example defines three coroutines task1, task2, and task3 which simulate different types of tasks.

task1 is a task that takes 1 seconds to complete, with 3 sub-steps,
task2 takes 0.5 secs to start, 1 sec between each step, and 0.5 sec between the last step and done.
task3 takes 2 sec to complete

In the main function, we use asyncio.create_task to create tasks for each of the coroutines, and then use await to run them in the background.

When you run this code, you'll see the output of each task interleaved as they run in parallel.
"""

import asyncio


async def task1():
    print("Task 1: Starting")
    await asyncio.sleep(1)
    print("Task 1: 1")
    await asyncio.sleep(1)
    print("Task 1: 2")
    await asyncio.sleep(1)
    print("Task 1: 3")
    print("Task 1: Done")


async def task2():
    print("Task 2: Starting")
    await asyncio.sleep(0.5)
    print("Task 2: x")
    await asyncio.sleep(1)
    print("Task 2: X")
    await asyncio.sleep(0.5)
    print("Task 2: X-X")
    print("Task 2: Done")


async def task3():
    print("Task 3: Starting")
    await asyncio.sleep(2)
    print("Task 3: Done")


async def main():
    # Create tasks using asyncio.create_task
    task1_coroutine = asyncio.create_task(task1())
    task2_coroutine = asyncio.create_task(task2())
    task3_coroutine = asyncio.create_task(task3())

    # Run the tasks in the background using await
    await task1_coroutine
    await task2_coroutine
    await task3_coroutine


if __name__ == "__main__":
    asyncio.run(main())
