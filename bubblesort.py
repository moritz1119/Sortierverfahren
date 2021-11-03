def bubblesort(unsortierte_Liste):
    print(unsortierte_Liste)
    for j in range(len(unsortierte_Liste)):
        for i in range(len(unsortierte_Liste)-(j+1)):
            if unsortierte_Liste[i] > unsortierte_Liste[i+1]:
                temp = unsortierte_Liste[i]
                unsortierte_Liste[i] = unsortierte_Liste[i+1]
                unsortierte_Liste[i+1] = temp
                print(unsortierte_Liste)
    return unsortierte_Liste
