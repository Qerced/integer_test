def search_of_black(balls: list, count: int):
    for i in range(count-1):
        if balls[i] == 'black':
            return i
    return -1


if __name__ == '__main__':
    import argparse
    from random import sample

    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int, help='Количество шаров')
    parser.add_argument('--black', action='store_true', help='Добавить черный')
    args = parser.parse_args()
    print(
       search_of_black(sample(
            ['white', 'black'],
            counts=[args.count - args.black, args.black],
            k=args.count
        ), args.count)
    )
