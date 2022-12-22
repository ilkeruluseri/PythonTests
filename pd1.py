liste1 = [3, 15, 12, 4, 6, 34, 23, 21, 18]


print(liste1)


def sort(liste):
    n = len(liste)
    for i in range(n-1):
        if liste[i] > liste[i+1]:
            x = liste1[i]
            liste[i] = liste[i+1]
            liste[i + 1] = x
            sort(liste)
    return liste


liste1 = sort(liste1)
print(liste1)
