# Master_Thesis_Aux_Funcs
Repo with some of the aux functions in Python used in my Master Thesis

These functions were implemented in Python (v3.X)

If you use the recolhe_Sinais or the limita_som, either as are or adapted, please quote the following article:

***B. Rodrigues, H. Cordeiro and G. Marques, "Spectral energy bands for laryngeal pathologies discrimination in speech signals : Healthy and unhealthy voices discrimination, and pathology discrimination," 2023 18th Iberian Conference on Information Systems and Technologies (CISTI), Aveiro, Portugal, 2023, pp. 1-6, doi: 10.23919/CISTI58278.2023.10212052.***

## Function: recolhe_Sinais

This is a function used to extract the speech signals, as well as some information about them, from the São Paulo Voice Database

The speech signals are extracted into numpy arrays. No pre-processing, other than normalization (the values will range between -1 and 1), is applied.

The São Paulo Voice Database database contains speech signals from speakers of both genders, healthy and with diagnosed pathologies. 
The speech signals were obtained from 15 healthy speakers, 15 speakers diagnosed with nodules, 17 speakers diagnosed with Reinke's edema, and 14 speakers diagnosed with pathologies of neurological origin, totaling 61 speakers, aged between 21 and 90 years old, from both genders.
The signals consist in the sustained vowel /a/, with a minimum duration of 2 seconds. The speech signals from speakers diagnosed with phisiological pathologies (Reinke's Edema and Vocal Nodules) also contain the sustained vowels /e/ and /i/.
The speech signals in the DB are stored in monochannel .wav files, with a sampling frequency of 22050 Hz and PCM of 16 bits per sample.

The function recolhe_Sinais extracts the signals into a Python Dict, also returning the sample rate of the last file analyzed.
Example of usage:

```
sinais, fs = recolhe_Sinais()

X = sinais['sinal_A'] # numpy arrays containing the speech signal from the sustained /a/ .wav file. 
y = sinais['classe']
```

In order to work propperly, the Database folder must have a specific structure, as well as the location of the running code.

## Function: limita_som

This is a function used to limit the speech signal to the parts where it actually contains speech, deleting the beginning and ending silences, when they exist (and they exist in the São Paulo Voice Database).

It takes as input argument the speech signal (np array).
It can also take as input arguments the size, in samples, of the frames in which the signal will be divided, as well as the limits used in the function.

The process is as follows:
- The function divides de signal into frames
- The power in each frame is calculated
- If the power of a frame is bigger than the k1 limit, and the power of the following frame is bigger than the limit k2, then it's assumed that the speech signal starts in that frame, discarding the previous ones
- The same process is made, from the end into the beginning

That way only the frames containing the speech signal are analyzed in the following steps
The limited signal is normalized, so that its values are contained between -1 and 1

## Function: meus_params

This is a function used to extract some acoustic parameters from the speech signals
Takes as argument the pathname of the speecch file

Returns:
- meanF0, stddevF0
- localJitter, localabsoluteJitter, rapJitter, ppq5Jitter, ddpJitter
- localShimmer, localdbShimmer, apq3Shimmer, apq5Shimmer, apq11Shimmer, ddaShimmer
- HNR

Example of usage, in conjunction with recolhe_Sinais:

```
sinais, fs = recolhe_Sinais()

X = sinais['sinal_A']
y = sinais['classe']

nomes = sinais['nome']

pitch = np.zeros((len(nomes), 2))
jitter = np.zeros((len(nomes), 5))
shimmer = np.zeros((len(nomes), 6))
harmonn = np.zeros((len(nomes)))

for i in range(len(nomes)):
    pitch[i,:], jitter[i,:], shimmer[i,:], harmonn[i] = meus_params(nomes[i])
```

where 'nomes' is a list containing the pathnames of the different signals

This function uses Praat, as well a the Parselmouth library.
So please, don't forget to cite Praat:

**Boersma, P., & Weenink, D. (2021). Praat: doing phonetics by computer [Computer program]. Version 6.1.38, retrieved 2 January 2021 from http://www.praat.org/**

As well as Parselmouth:

**Jadoul, Y., Thompson, B., & de Boer, B. (2018). Introducing Parselmouth: A Python interface to Praat. Journal of Phonetics, 71, 1-15. https://doi.org/10.1016/j.wocn.2018.07.001**
