{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "432bcee3-7abe-4e94-a118-985fe49d0b0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mejor esperar\n"
     ]
    }
   ],
   "source": [
    "#Retos condicionales y excepciones\n",
    "\n",
    "#Reto 1\n",
    "seg_restantes = 20\n",
    "if seg_restantes < 25:\n",
    "    print(\"Mejor esperar\")\n",
    "else:\n",
    "    print(\"Adelante\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "70eed410-56bb-45ff-8e07-e5bd0ca32770",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "berenjena rellena\n"
     ]
    }
   ],
   "source": [
    "#Retos condicionales y excepciones\n",
    "\n",
    "#Reto 2\n",
    "ingrediente = \"berenjena\"\n",
    "try: \n",
    "    if ingrediente == \"pasta\":\n",
    "        print(\"pasta boloñesa\")\n",
    "    elif ingrediente == \"calamares\":\n",
    "        print(\"bocata de calamares\")\n",
    "    elif ingrediente == \"patata\":\n",
    "        print(\"tortilla de patatas\")\n",
    "    elif ingrediente == \"soja\":\n",
    "        print(\"sushi\")\n",
    "    elif ingrediente == \"curry\":\n",
    "        print(\"tikka masala\")\n",
    "    elif ingrediente == \"pan\":\n",
    "        print(\"tostadas\")\n",
    "    elif ingrediente == \"cerdo\":\n",
    "        print(\"orejas\")\n",
    "    elif ingrediente == \"proteinas\":\n",
    "        print(\"batido proteico\")\n",
    "    elif ingrediente == \"berenjena\":\n",
    "        print(\"berenjena rellena\")\n",
    "    elif ingrediente == \"alubias\":\n",
    "        print(\"cocido asturiano\")\n",
    "    else:\n",
    "        print(\"Imposible proponer receta\")\n",
    "except: \n",
    "    print(\"Error de ingrediente\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4d58c4dc-e6e1-44ef-8b54-30dd4977db03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El restaurante es valido\n",
      "Va a ser una celebracion fantastica\n"
     ]
    }
   ],
   "source": [
    "#Retos condicionales y excepciones\n",
    "\n",
    "#Reto 3\n",
    "platos = 4\n",
    "DJ = 0\n",
    "horas_barra = 3\n",
    "coctel = 3\n",
    "try:\n",
    "    if (platos >= 3 and DJ >= 1 and horas_barra >= 2) or (platos >= 2 and coctel >= 1 and horas_barra >= 2):\n",
    "        print(\"El restaurante es valido\")\n",
    "    else:\n",
    "        print(\"El restaurante no es valido\")\n",
    "except:\n",
    "    print(\"Error al introducir los datos\")\n",
    "finally:\n",
    "    print(\"Va a ser una celebracion fantastica\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "6f31ebe0-06a8-491f-9f64-bf21f1d6e0dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lucia\n",
      "73\n",
      "33\n",
      "72\n",
      "No hay mas datos relevantes en el grupo\n"
     ]
    }
   ],
   "source": [
    "#Retos condicionales y excepciones\n",
    "\n",
    "#Reto 4\n",
    "persona1 = {\"nombre\" : \"Alberto\",\n",
    "\"apellido\" : \"Diaz\",\n",
    "\"anyoNacimiento\" : 1950,\n",
    "\"aficiones\": (\"futbol\", \"cocina\"),\n",
    "\"dni\": { \"anyoExpedicion\" : 2010,\n",
    "\"lugarNacimento\": \"Albacete\"},\n",
    "\"colorPelo\" : \"pelirrojo\"}\n",
    "persona2 = {\"nombre\" : \"Lucia\",\n",
    "\"apellido\" : \"Hernan\",\n",
    "\"anyoNacimiento\" : 2002,\n",
    "\"aficiones\": (\"tenis\", \"cocina\"),\n",
    "\"dni\": { \"anyoExpedicion\" : 2022,\n",
    "\"lugarNacimento\": \"Tarragona\"},\n",
    "\"colorPelo\" : \"castaño\"}\n",
    "persona3 = {\"nombre\" : \"Julio\",\n",
    "\"apellido\" : \"Tomate\",\n",
    "\"anyoNacimiento\" : 1990,\n",
    "\"aficiones\": (\"futbol\", \"natacion\"),\n",
    "\"dni\": { \"anyoExpedicion\" : 2021,\n",
    "\"lugarNacimento\": \"Granada\"},\n",
    "\"colorPelo\" : \"rubio\"}\n",
    "persona4 = {\"nombre\" : \"Veronica\",\n",
    "\"apellido\" : \"Diaz\",\n",
    "\"anyoNacimiento\" : 1951,\n",
    "\"aficiones\": (\"ballet\", \"boxeo\"),\n",
    "\"dni\": { \"anyoExpedicion\" : 2011,\n",
    "\"lugarNacimento\": \"Albacete\"},\n",
    "\"colorPelo\" : \"pelirrojo\"}\n",
    "grupo = (persona1, persona2, persona3, persona4)\n",
    "try:\n",
    "    if persona1[\"colorPelo\"] == \"castaño\" :\n",
    "        print(persona1[\"nombre\"])\n",
    "    else: \"\"\n",
    "    if persona2[\"colorPelo\"] == \"castaño\" :\n",
    "        print(persona2[\"nombre\"])\n",
    "    else: \"\"\n",
    "    if persona3[\"colorPelo\"] == \"castaño\" :\n",
    "        print(persona3[\"nombre\"])\n",
    "    else: \"\"\n",
    "    if persona4[\"colorPelo\"] == \"castaño\" :\n",
    "        print(persona4[\"nombre\"])\n",
    "    else: \"\"\n",
    "    if 2023 - persona1[\"anyoNacimiento\"] > 30 :\n",
    "        print(2023 - persona1[\"anyoNacimiento\"])\n",
    "    else: \"\"\n",
    "    if 2023 - persona2[\"anyoNacimiento\"] > 30 :\n",
    "        print(2023 - persona2[\"anyoNacimiento\"])\n",
    "    else: \"\"\n",
    "    if 2023 - persona3[\"anyoNacimiento\"] > 30 :\n",
    "        print(2023 - persona3[\"anyoNacimiento\"])\n",
    "    else: \"\"\n",
    "    if 2023 - persona4[\"anyoNacimiento\"] > 30 :\n",
    "        print(2023 - persona4[\"anyoNacimiento\"])\n",
    "    else: \"\"\n",
    "except: print(\"Error de informacion\")\n",
    "finally: print(\"No hay mas datos relevantes en el grupo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3907683-c066-4674-ab36-a4b0c986b9de",
   "metadata": {},
   "outputs": [],
   "source": []
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
