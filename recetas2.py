recetas = {
    "Ensalada Caribeña": {
        "Ingredientes": {"1 lechuga romana", "1 manzana Red", "100g de arandano","50g de nuez","100g de queso panela","1 lata de durazno en almibar","ajonjoli"},
        "Procedimiento": [
            "Lava la lechuga, la manzana, el arandano,.",
            "Pica la lechuga y la nuez en pedazos pequeños.",
            "Pica en cuadritos el queso panela.",
            "En rodajas, pica la manzana para que salgan trozos pequeños",
            "Mezcla todo en un bowl y agrega el ajonjili con el durazno.",
            "LISTO, YA TIENES TU ENSALADA CARIBEÑA :).",
        ]
    },
    "Chilaquiles rojos": {
        "Ingredientes": {"1 bolsa de totopos", "4 jitomates", "2 chiles guajillos", "2 ajos", "sal", "1/4 de cebolla", "Aceite de oliva", "2 ramas de epazote"},
        "Procedimiento": [
            "Tosta la bola de totopos en una olla.",
            "Lava los jitomates, la cebolla y el epazote.",
            "Licua los jitomates con el ajo y los chiles guajillos.",
            "Agrega la salsa en la olla donde ya estan los totopos y ponle una cucharada de aceite de oliva.",
            "Para finalizar, agrega una pisca de sal de mesa y vacia el epazote.",
            "LISTO, DISFRUTA TUS CHILAQUILES ROJOS :)).",
        ]
    },
    "Tinga de pollo": {
        "Ingredientes": {"1 pechuga de pollo", "4 jitomates", "sal", "1 ramo de laurel", "1 paquete de tostadas", "1 vaso de crema", "1 ajo", "1 lata de chiles chipotles"},
        "Procedimiento": [
            "Lava el pollo, los jitomates y el laurel.",
            "Calienta el pollo en una olla por 3/4 de hora.",
            "Licua los jitomates con el ajo y vacia la lata de chipotles tambien en la licuadora.",
            "Desmunuza el pollo y despues vacialo en una cazuela.",
            "Agrega la salsa en la cazuela y vacia el laurel.",
            "Ponle una pisca de sal.",
            "LISTO, GOZA DE TU TINGA DE POLLO :))).",
        ]
    }
}

print("=== PROGRAMA DE RECETAS ===\n")
ingredientes_usuario = set()

print("Ingresa los ingredientes que tienes:. <Escribe 'fin' para terminar>. ")
while True:
    ingr = input("> ").lower()
    if ingr == "fin":
        break
    ingredientes_usuario.add(ingr)

recetas_disponibles = []

for nombre, info in recetas.items():
    coincidencias = len(info["Ingredientes"].intersection(ingredientes_usuario))

    if coincidencias >= 2:
        recetas_disponibles.append(nombre)

if not recetas_disponibles:
    print("\n No tienes ingredientes suficientes para las recetas registradas. <Minimo 2 condiciones>.")
else:
    print("\n Con tus ingredientes puedes preparar o intentar:")
    for i, receta in enumerate(recetas_disponibles, 1):
        print(f"{i}. {receta}")

    opcion = int(input("\n¿Qué receta deseas ver? Selecciona el número: "))
    seleccion = recetas_disponibles[opcion - 1]

    print(f"\n Procedimiento para preparar **{seleccion}**:\n")

    pasos = recetas[seleccion]["Procedimiento"]
    for num, paso in enumerate(pasos, 1):
        print(f"Paso {num}: {paso}")

print("\nGracias por usar el programa de recetas :)).")