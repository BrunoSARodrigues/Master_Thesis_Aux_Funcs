# last update: 6 October 2023

import numpy as np
import soundfile as sf
import os

def recolhe_Sinais():
# returns a dictionary with various information relating the Sao Paulo Voice Database
# the signals themselves will be stored in numpy arrays
# please check 'descricao'
# also returns the samplerate of the last file analyzed 
# (works because all the data files have the same samplerate (22050 Hz)

    # Introduzir descricao (depois)
    descricao = """Dicionario com os sinais de fala
    sinal_A (sustained 'a' signal)
    sinal_E e sinal_I - quando aplicavel (classes 1 e 3)
    Classe:
    0 - Saudaveis (Healthy)
    1 - Reinke
    2 - Neuro
    3 - Nodulos
    genero (gender)
    idade (age)
    nome (pathname)"""
    
    # beware of the folder structure
    # the DB is in a folder called BD/Banco vozes_HCordeiro_21_11_12
    # my scripts are in folders named code/parcelXX
    # so it's needed to go up 2 folders and then enter de DB folder
    nome = os.path.join('..', '..', 'BDs', 'Banco vozes_HCordeiro_21_11_12')
    
    nome0 = 'saudaveis1_16_2seg'
    genero0 = ['M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'M']
    idade0 = [39, 21, 41, 22, 35, 23, 23, 21, 36, 24, 45, 38, 27, 21, 42]
    classe0 = np.zeros(len(idade0))
    
    nome1 = 'EdemaReinke_16'
    genero1 = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    idade1 = [45, 36, 38, 38, 40, 41, 48, 34, 28, 33, 40, 29, 38, 34, 42, 45, 46]
    classe1 = np.ones(len(idade1))
    
    nome2 = 'Neurologica_14_Parte1'
    genero2 = ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
    idade2 = [90, 52, 77, 60, 80, 53, 59, 42, 40, 22, 65, 70, 70, 39]
    classe2 = np.ones(len(idade2))*2
    
    nome3 = 'nodulos_15_Parte1'
    genero3 = ['F', 'F', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    idade3 = [28, 33, 45, 26, 44, 42, 38, 31, 29, 35, 48, 37, 32, 45, 25]
    classe3 = np.ones(len(idade3))*3
    
       
    # Chaves do Dicionario
    chaves = ['sinal_A', 'sinal_E', 'sinal_I', 'classe', 'genero', 'idade', 'DESCR', 'nome']
    genero = genero0 + genero1 + genero2 + genero3
    idade = idade0 + idade1 + idade2 + idade3
    classe = np.hstack((classe0, classe1, classe2, classe3))
    
    # sinais = {key: None for key in chaves}
    
    # Inicializar listas
    
    lista_temp_A = []
    lista_temp_E = []
    lista_temp_I = []   
    lista_nome = [] 
    
    # Vozes saudaveis

    fN = nome + '\\' + nome0 + '\\'
    lista_files = os.listdir(fN)
    
    for temp in lista_files:   
        fN_temp = fN + temp
        data, samplerate = sf.read(fN_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_A.append(data)
        lista_temp_E.append(0)
        lista_temp_I.append(0)
        lista_nome.append(fN_temp)

    # Reinke

    fN = nome + '\\' + nome1 + '\\'
    lista_files = os.listdir(fN)
    
    for temp in lista_files: 
        fN_temp = fN + temp + '\\'
        lista_files_in = os.listdir(fN_temp)
        fN_temp_temp = fN_temp + lista_files_in[0]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_A.append(data)
        lista_nome.append(fN_temp_temp)
        fN_temp_temp = fN_temp + lista_files_in[1]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_E.append(data)
        fN_temp_temp = fN_temp + lista_files_in[2]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_I.append(data)
        
        
        
    # Neuro

    fN = nome + '\\' + nome2 + '\\'
    lista_files = os.listdir(fN)
    
    for temp in lista_files: 
        fN_temp = fN + temp + '\\'
        lista_files_in = os.listdir(fN_temp)
        fN_temp_temp = fN_temp + lista_files_in[0]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_A.append(data)
        lista_temp_E.append(0)
        lista_temp_I.append(0)
        lista_nome.append(fN_temp_temp)
        
        
    # Nodulos

    fN = nome + '\\' + nome3 + '\\'
    lista_files = os.listdir(fN)
    
    for temp in lista_files: 
        fN_temp = fN + temp + '\\'
        lista_files_in = os.listdir(fN_temp)
        fN_temp_temp = fN_temp + lista_files_in[0]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_A.append(data)
        lista_nome.append(fN_temp_temp)
        fN_temp_temp = fN_temp + lista_files_in[1]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_E.append(data)
        fN_temp_temp = fN_temp + lista_files_in[2]
        data, samplerate = sf.read(fN_temp_temp)
        data = data/np.max(np.absolute(data))
        lista_temp_I.append(data)
        
    # Inicializar Dicionario
    
    sinais = {
        chaves[0]: lista_temp_A,
        chaves[1]: lista_temp_E,
        chaves[2]: lista_temp_I,
        chaves[3]: classe,
        chaves[4]: genero,
        chaves[5]: idade,
        chaves[6]: descricao,   
        chaves[7]: lista_nome,        
    }
    
    return sinais, samplerate
    