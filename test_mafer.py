def count_trues(array):
    #Arrays in which we are going to save the results for the output
    indexes = []
    lengths = []
    counter = 0 

    for index, is_true in enumerate(array):  #We use enumerate so we can get the index directly
        if is_true:  #and we store is_true as the True/False value we get from the array. 
            counter += 1 #Every time we find a True, we increase the counter
            if counter == 2: #if the counter is equal to 2 we already have two in a row so we can save the previous index
                indexes.append(index-1) 
                lengths.append(2)
            elif counter > 2:
                lengths[-1] += 1 #We increase the size of the length array
        else:
            counter = 0 #We reset the counter to start the process again with the following true
    
    print(f'indexes_output = {indexes} \n', f'lengths_output = {lengths}')


lista = [True, False, True, True, False, True, True, True, False, True]

count_trues(lista)
