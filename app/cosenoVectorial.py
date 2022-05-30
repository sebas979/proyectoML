import numpy as np

def matrizNormal(matriz):
    matrizTran = np.transpose(matriz)
    matrizNormal = np.zeros((len(matrizTran),len(matrizTran[0])))
    i = j = 0
    # modulo = np.linalg.norm(matrizTran[i])
    while True:
        modulo = np.linalg.norm(matrizTran[i])
        matrizNormal[i][j] = matrizTran[i][j]/modulo
        j += 1
        if j == len(matrizNormal[0]):
            j = 0
            i += 1
        if i == len(matrizNormal):
            break
    return matrizNormal

def matrizDistacias(transpuesta):
    # transpuesta = np.transpose(matriz)
    matrizD = np.zeros((len(transpuesta),len(transpuesta)))
    for i in range(len(matrizD)):
        for j in range(len(matrizD[0])):
            if matrizD[i][j] == 0:
                matrizD[i][j] = matrizD[j][i] = round(np.dot(transpuesta[i],transpuesta[j]),2)
    return matrizD

# def matrizDistacias(transpuesta):
#     # transpuesta = np.transpose(matriz)
#     matrizD = np.zeros((len(transpuesta),len(transpuesta)))
#     i = j = 0
#     while True:
#         if matrizD[i][j] == 0:
#             matrizD[i][j] = matrizD[j][i] = round(np.dot(transpuesta[i],transpuesta[j]),2)
#         j += 1
#         if j == len(transpuesta):
#             j = 0
#             i += 1
#         if i == len(transpuesta):
#             break
#     return matrizD