import numpy as np

def calculate(list):
    # Check if the LIST SIZE is different than 9 
    if len(list) != 9:
        # Raise an error if the list is different than 9 elements
        raise ValueError("List must contain nine numbers.")
    
    # Converts the list to a 3x3 NUMPY ARRAY, AKA MATRIZ
    # LIST ===> MATRIX (LIST TRANSFORMS INTO MATRIX)
    stores_value = np.array(list).reshape(3, 3)
    
    # Calculate statistics along both axis 
    # 0 = COLUMNS, 1 = ROWS and FLATTENED (OVERALL)
    # [FLATTENED] IS MATRIX ===> LIST (MATRIX TRANSFORMS INTO LIST)
    calculations = {
        # Calculates the mean for each column of the matrix, and the overall mean
        'mean': [stores_value.mean(axis=0).tolist(), stores_value.mean(axis=1).tolist(), stores_value.mean()],
        # Calculates the variance for each column of the matrix, and the overall variance
        'variance': [stores_value.var(axis=0).tolist(), stores_value.var(axis=1).tolist(), stores_value.var()],
        # Calculates the standard deviation for each column of the matrix, and the overall standard deviation
        'standard deviation': [stores_value.std(axis=0).tolist(), stores_value.std(axis=1).tolist(), stores_value.std()],
        # Calculates the maximum for each column of the matrix, and the overall maximum
        'max': [stores_value.max(axis=0).tolist(), stores_value.max(axis=1).tolist(), stores_value.max()],
        # Calculates the minimum for each column of the matrix, and the overall minimum
        'min': [stores_value.min(axis=0).tolist(), stores_value.min(axis=1).tolist(), stores_value.min()],
        # Calculates the sum for each column of the matrix, and the overall sum
        'sum': [stores_value.sum(axis=0).tolist(), stores_value.sum(axis=1).tolist(), stores_value.sum()]
    }
    
    # FUNÇÃO RETORNA VALORES CALCULADOS
    return calculations