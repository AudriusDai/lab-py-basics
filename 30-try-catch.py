import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)

    dates = []
    colors = []

    for row in readCSV:
        print(row)
        dates.append(row[0])
        colors.append(row[3])

    print(dates)
    print(colors)

    try:
        color = input('for what color to find date?')

        if color in colors:
            coldex = colors.index(color.lower())
            print('date is: ', dates[coldex])
        else:
            print('Color not found: ', color)

    # except Exception, e: py 2.xp
    except Exception as e:  # this is for py 3.x
        print(e)

    print('program did not crash')
