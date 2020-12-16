def photos_in_data_centers(data_centers):
    photos = 0

    while len(data_centers) != 1:
        data_centers.sort(reverse=True)

        if data_centers[-1] == 0:
            data_centers.pop()
            continue

        data_centers[0] -= 1
        data_centers[-1] -= 1
        photos += 1

    return photos


def main():
    data_centers_count = int(input())
    data_centers = [int(i) for i in input().split()]
    print(photos_in_data_centers(data_centers))


if __name__ == '__main__':
    main()
