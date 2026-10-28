from modelos_biblioteca import agregar_categoria, registrar_libro, registrar_usuario, prestar_libro

if __name__ == "__main__":
    mis_categorias = {"Fantasía", "Historia"}
    mi_inventario = {}
    mis_usuarios = {}
    
    mis_categorias = agregar_categoria(mis_categorias, "Ciencia Ficción")
    print("Categorías:", mis_categorias)
    mi_inventario, mis_categorias = registrar_libro(mi_inventario, "111", "El Hobbit", "Tolkien", "Fantasía", mis_categorias)
    mi_inventario, mis_categorias = registrar_libro(mi_inventario, "222", "Dune", "Herbert", "Ciencia Ficción", mis_categorias)
    print("Inventario inicial:", mi_inventario)
    mis_usuarios = registrar_usuario(mis_usuarios, "U01", "Carlos")
    print("Usuarios iniciales:", mis_usuarios)
    mis_usuarios = prestar_libro("111", "U01", mi_inventario, mis_usuarios)
    
    print("\n--- Resultados después del préstamo ---")
    print("Usuario con su libro prestado:", mis_usuarios)
    print("Inventario (el libro 111 ya no está disponible):", mi_inventario)
