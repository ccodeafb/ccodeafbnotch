{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "915c689f-664e-4e5b-8816-bfd3aed8b317",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "marisa\n",
      "34\n",
      "9.76\n",
      "false\n"
     ]
    }
   ],
   "source": [
    "\"Reto 1\"\n",
    "\n",
    "\"Paso 1\"\n",
    "cadena = \"marisa\"\n",
    "\"Paso 2\"\n",
    "entero = 34\n",
    "\"Paso 3\"\n",
    "numfloat = 9.76\n",
    "\"Paso 4\"\n",
    "if numfloat > 34:\n",
    "    x = \"true\"\n",
    "else:\n",
    "    x = \"false\"\n",
    "\"Paso 5\"\n",
    "print(cadena)\n",
    "print(entero)\n",
    "print(numfloat)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1a2ddb93-4129-4be5-9247-9327dc68a357",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mesa', 'silla', 'pc', 'sofa', 'cama']\n",
      "cama\n",
      "m\n",
      "[23, 11, 2, 75, 234]\n",
      "true\n"
     ]
    }
   ],
   "source": [
    "\"Reto 2\"\n",
    "\n",
    "\"Paso 1\"\n",
    "nombres = [\"marisa\", \"pepe\", \"lola\", \"andrea\", \"lucas\"]\n",
    "ingredientes = [\"huevos\", \"apio\", \"coliflor\", \"cebolla\", \"tomate\"]\n",
    "muebles = [\"mesa\", \"silla\", \"pc\", \"sofa\", \"cama\"]\n",
    "\"Paso 2\"\n",
    "matriz = [nombres, ingredientes, muebles]\n",
    "\"Paso 3\"\n",
    "print(matriz[2])\n",
    "\"Paso 4\"\n",
    "print(matriz[2][4])\n",
    "\"Paso 5\"\n",
    "print (matriz [2][4][2])\n",
    "\"Paso 6\"\n",
    "matriz[2][0:5] = [23, 11, 2, 75, 234]\n",
    "\"Paso 7\"\n",
    "print(matriz[2])\n",
    "\"Paso 8\"\n",
    "matriz [1][3] = \"true\"\n",
    "\"Paso 9\"\n",
    "print(matriz[1][3])\n",
    "\"Paso 10\"\n",
    "nombres.append(\"fernando\")\n",
    "\"Paso 11\"\n",
    "nombres.pop(0)\n",
    "\"Paso 12\"\n",
    "ingredientes.pop(len(ingredientes) - 1)\n",
    "\"Paso 13\"\n",
    "ingredientes.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "3fec5987-8664-4a87-a916-b7a78bdb43ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alberto\n",
      "Jimenez\n",
      "Smith\n",
      "34971058F\n",
      "13/05/1990\n"
     ]
    }
   ],
   "source": [
    "\"Reto 3\"\n",
    "\n",
    "\"Paso 1\"\n",
    "tupla3 = (\"Alberto\", \"Jimenez\", \"Smith\", \"34971058F\", \"13/05/1990\")\n",
    "\"Paso 2\"\n",
    "nombre, apellido1, apellido2, dni, fecha = tupla3\n",
    "\"Paso 3\"\n",
    "print(nombre)\n",
    "print(apellido1)\n",
    "print(apellido2)\n",
    "print(dni)\n",
    "print(fecha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "593ae012-be8a-44e7-a0ed-356909a53b06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alberto\n",
      "Jimenez\n",
      "Smith\n",
      "34971058F\n",
      "13/05/1990\n",
      "['running', 'pintar', 'cocinar']\n",
      "dict_keys(['nombre', 'apellido1', 'apellido2', 'dni', 'fecha', 'aficiones'])\n",
      "dict_values(['Carlos', 'Romero', 'Benitez', '90163976U', '20/02/1973', ['running', 'pintar', 'cocinar']])\n"
     ]
    }
   ],
   "source": [
    "\"Reto 4\"\n",
    "\n",
    "\"Paso 1\"\n",
    "dicc = {\"nombre\": \"Carlos\", \"apellido1\": \"Romero\", \"apellido2\": \"Benitez\", \"dni\": \"90163976U\", \"fecha\": \"20/02/1973\", \"aficiones\": [\"running\", \"pintar\", \"cocinar\"]}\n",
    "\"Paso 2\"\n",
    "print(nombre)\n",
    "print(apellido1)\n",
    "print(apellido2)\n",
    "print(dni)\n",
    "print(fecha)\n",
    "print(aficiones)\n",
    "\"Paso 3\"\n",
    "print(dicc.keys())\n",
    "\"Paso 4\"\n",
    "print(dicc.values())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
