# last update: 6 October 2023

import parselmouth
from parselmouth.praat import call
import numpy as np

def meus_params(nome_ficheiro):

    # Retorna: meanF0, stddevF0
    # localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter
    # localShimmer, localdbShimmer, apq3Shimmer, apq5Shimmer, apq11Shimmer, ddaShimmer

    sound = parselmouth.Sound(nome_ficheiro) # Carregar o sinal audio
    f0min = 75 # Freq Min para o Pitch
    f0max = 400 # Freq Max para o Pitch
    unidade = "Hertz" # Unidade
    inicio = 0.0 # Onde, no sinal, se inicia o processo (0,0 segundos) 

    # PITCH
    pitch = call(sound, "To Pitch", inicio, f0min, f0max) # Objecto Pitch do Praat
    # 0, 0 significa que é visto no sinal todo
    meanF0 = call(pitch, "Get mean", 0, 0, unidade) # Pitch médio
    stdevF0 = call(pitch, "Get standard deviation", 0 ,0, unidade) # Desvio padrão do Pitch
    
    pitch_out = np.hstack((meanF0, stdevF0))

    # range_F = [0.01, 75] # gama de frequencias
    # range_H = [0.1, 1.0] # gama de harmonicidade
    # harmonicity = call(sound, "To Harmonicity (cc)", range_F[0], range_F[1], range_H[0], range_H[1])
    # hnr = call(harmonicity, "Get mean", 0, 0)

    # "periodic", instructs Praat to create a PointProcess object based on the periodicity of the waveform 
    # "cc" and using the cepstral peak prominence method for peak picking.
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)

    # JITTER
    # 0, 0: The first two arguments refer to the minimum and maximum values of the pitch periods to be included
    # in the analysis. In this case, both values are set to 0, indicating that all pitch periods should be considered.
    # 0.0001: The third argument specifies the maximum tolerated error in pitch period detection, in seconds. A smaller
    # value indicates a higher level of precision in pitch period detection.
    # 0.02: The fourth argument specifies the analysis window size, in seconds. The analysis window is a sliding window
    # that is moved over the pitch period sequence to compute the jitter values
    # 1.3: The fifth argument specifies the maximum period factor, which is used to exclude pitch periods that are considered
    # to be too long or too short compared to the average pitch period. A higher value indicates a wider tolerance for
    # variations in pitch period length.
    # measurement of the variation of the time intervals between consecutive pitch periods, expressed as a percentage of the
    # average pitch period
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    # This is the absolute jitter measure, expressed in seconds. It represents the absolute difference between consecutive pitch
    # periods, reflecting the degree of instability or irregularity in the pitch period sequence
    localabsoluteJitter = call(pointProcess, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
    # This is the relative average perturbation jitter measure, expressed as a percentage of the average pitch period.
    # It represents the average difference between consecutive pitch periods, normalized by the average pitch period
    rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    # This is the pitch period perturbation quotient jitter measure, expressed as a percentage of the average pitch period.
    # It represents the degree of perturbation in the pitch period sequence, calculated as the 5th percentile of the
    # distribution of the differences between consecutive pitch periods
    ppq5Jitter = call(pointProcess, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
    # This is the dysphonia severity index jitter measure, expressed in seconds. It represents the degree of perturbation in the
    # pitch period sequence, calculated as the difference between the absolute differences of consecutive pitch periods
    ddpJitter = call(pointProcess, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
    
    jitter_out = np.hstack((localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter))

    # SHIMMER
    # 0, 0: Starting and end point for calculating the local shimmer value, usually set to 0.
    # 0.0001: This is the time step for the calculation, in seconds. 
    # It determines the accuracy of the calculation and is typically set to a very small value.
    # This is the window length, in seconds, over which the shimmer value is calculated. 
    # It determines the resolution of the shimmer calculation and is typically set to a value that captures the
    # variability in the pitch periods of the sound. Geralmente usado 0.02
    janela = 0.03
    # 1.3: e 1.6: This is the minimum and maximum threshold for the amplitude of the peaks in the shimmer calculation. 
    # Peaks below the min or above the max threshold are ignored.
    # Absolute shimmer value calculated over short time intervals, typically between 1 and 5 milliseconds.
    # It reflects the high-frequency spectral modulation in the speech signal and is measured as the average difference
    # in amplitude between consecutive glottal cycles.
    localShimmer =  call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, janela, 1.3, 1.6)
    # similar to the localShimmer, but it is calculated in decibels (dB) 
    localdbShimmer = call([sound, pointProcess], "Get shimmer (local_dB)", 0, 0, 0.0001, janela, 1.3, 1.6)
    # This is the Amplitude Perturbation Quotient (APQ) for shimmer calculated over three consecutive glottal cycles.
    # It is a measure of the cycle-to-cycle variation in amplitude, with higher values indicating greater variability.
    apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, janela, 1.3, 1.6)
    # This is the APQ for shimmer calculated over five consecutive glottal cycles. Like apq3Shimmer
    # it measures cycle-to-cycle variation in amplitude.
    apq5Shimmer = call([sound, pointProcess], "Get shimmer (apq5)", 0, 0, 0.0001, janela, 1.3, 1.6)
    # This is the APQ for shimmer calculated over eleven consecutive glottal cycles
    apq11Shimmer =  call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, janela, 1.3, 1.6)
    # This is the Dynamic Variation Index (DVI) for shimmer, also known as the Delta Amplitude Variability Index (DAVI). 
    # It measures the average absolute difference between the amplitudes of consecutive glottal cycles, 
    # normalized by the total amplitude range.
    ddaShimmer = call([sound, pointProcess], "Get shimmer (dda)", 0, 0, 0.0001, janela, 1.3, 1.6)    
    
    shimmer_out = np.hstack((localShimmer, localdbShimmer, apq3Shimmer, apq5Shimmer, apq11Shimmer, ddaShimmer))
    
    # HARMONICITY
    harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
    hnr = call(harmonicity, "Get mean", 0, 0)
    # harmon_out = np.hstack((harmonicity, hnr))
    
    return pitch_out, jitter_out, shimmer_out, hnr
