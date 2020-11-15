# Cassidy Fairey
# CS 2300 002
# Project 3
# This program will intake a set of two basis vectors and a candidate vector. It will then determine
# if candidate vector if in the subspace spanned by the two vectors.

def vector_handler(file):
    """
    This method will receive the file input then sort through the basis vectors and candidate vectors
    :param file: file contianing complete vector sets for a problem
    :return:
    """
    vector_file = open(file)
    vector_sets = vector_file.readlines()
    basisA = vector_sets[0]
    basisB = vector_sets[1]
    candidate = vector_sets[2]
    cross_vector = cross_product(basisA.split(), basisB.split())

    # Send cross_vector and candidate vector to dot_product function to check if they are a subspace
    dot_result = dot_product(candidate.split(), cross_vector)
    if dot_result == 0:
        print("Yes, the vector [" + candidate.rstrip("\n") + "] is in the subspace spanned by ["
        + basisA.rstrip("\n") + "] and [" + basisB.rstrip("\n"))
    else:
        print("No, the vector [" + candidate.rstrip("\n") + "] is not in the subspace spanned by ["
              + basisA.rstrip("\n") + "] and [" + basisB.rstrip("\n"))


def cross_product(a, b):
    """
    This method takes in two vectors (for uniformity it will be the two basis vectors). It will then perform the cross
    product function on the vectors and return the vector product for further use
    :param a: basisA from read_vectors
    :param b: basisB from read_vectors
    :return: cross product resulting vector
    """
    vector_u = []
    vector_u.append((float(a[1]) * float(b[2])) - (float(a[2]) * float(b[1])))
    vector_u.append((float(a[2]) * float(b[0])) - (float(a[0]) * float(b[2])))
    vector_u.append((float(a[0]) * float(b[1])) - (float(a[1]) * float(b[0])))
    vector_u = [round(num, 2) for num in vector_u]

    # check vector
    if dot_product(a, vector_u) == 0 and dot_product(b, vector_u) == 0:
        return vector_u
    else:
        print('Error checking cross product result')


def dot_product(a, b):
    """
    This method takes in two vectors and uses them to perform a dot product function
    :param a: some vector
    :param b: some vector
    :return: The result of the dot product
    """
    dot_result = ((float(a[0]) * float(b[0])) + (float(a[1]) * float(b[1])) + (float(a[2]) * float(b[2])))
    return dot_result


if __name__ == '__main__':
    print("Per the rubric: Cassidy Fairey, Project 3")

    # Read in and sort the vectors
    vector_handler('vectorsA.txt')
    vector_handler('vectorsB.txt')
    vector_handler('vectorsC.txt')
    vector_handler('vectorsD.txt')
