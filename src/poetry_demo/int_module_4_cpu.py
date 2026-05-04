from concurrent.futures import ThreadPoolExecutor


def square(n):
    return n * n


with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square, range(10)))
    print(results)
