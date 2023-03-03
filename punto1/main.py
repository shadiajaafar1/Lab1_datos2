from arbol import TreeNode
import csv

def main():
    filename = 'User_track_data.csv'
    user_ids = read_user_ids_from_csv(filename)

    tree = TreeNode()
    tree.run_with_user_ids(user_ids)

def read_user_ids_from_csv(file_path):
    user_ids = []
    with open(file_path) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            try:
                user_id = int(row[0])
            except ValueError:
                user_id = sum([10**(len(row[0])-i-1)*(ord(c)-64) for i, c in enumerate(row[0])])  
            user_ids.append(user_id)
    return user_ids

# usamos ord(c)-64 el cual Convierte el valor ASCII del carácter c en un número entero comprendido entre 1 y 26. La parte -64 se utiliza para asignar el valor ASCII del carácter c a la cadena. La parte -64 se utiliza para asignar los códigos ASCII de las letras mayúsculas al intervalo 1-26

if __name__ == '__main__':
    main()








