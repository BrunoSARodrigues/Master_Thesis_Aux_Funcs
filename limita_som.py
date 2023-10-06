# last update: 6 October 2023

import numpy as np

def limita_som(palavra, WS=256, k1=0.001, k2m = 10):
# Takes as input a signal (numpy array) 
# May take the limits k1 and k2m, as well as
# WS, which will be the size of the frames in which the signal
# will be dicvided


    # Normalization
    palavra = palavra / np.max(np.abs(palavra))

    # Determination of power of excerpts
    potencias = np.zeros(int(len(palavra) / WS))
    for i in range(int(len(palavra) / WS)):
        excerto = palavra[i * WS:(i + 1) * WS]
        potencias[i] = np.sum(excerto ** 2) / WS

    # Define test values
    k2 = k2m * k1

    # Indices to limit the word
    indice_inf = 0
    indice_sup = 0

    # Flags to stop the process
    stop_inf = 0
    stop_sup = 0

    for i in range(len(potencias)):
        # Found the limits
        if stop_sup == 1 and stop_inf == 1:
            break

        # Lower Limit
        if potencias[i] > k1 and indice_inf == 0:
            indice_inf = i
        if indice_inf != 0 and stop_inf == 0:
            if potencias[i] < k1:
                indice_inf = 0
            elif potencias[i] > k2:
                stop_inf = 1

        # Upper Limit
        if potencias[len(potencias) - 1 - i] > k1 and indice_sup == 0:
            indice_sup = len(potencias) - 1 - i
        if indice_sup != 0 and stop_sup == 0:
            if potencias[len(potencias) - 1 - i] < k1:
                indice_sup = 0
            elif potencias[len(potencias) - 1 - i] > k2:
                stop_sup = 1

    palavra_limitada = palavra[(indice_inf - 1) * WS:indice_sup * WS]
    
    # Normalization
    palavra_limitada = palavra_limitada / np.max(np.abs(palavra_limitada))
    return palavra_limitada