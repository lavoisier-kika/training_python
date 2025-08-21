
print(" *")
print(" * *")
print(" * *")
print(" * *")
print("*** ***")
print(" * *")
print(" * *")
print(" *****")
# Minimiser le nombre d'appels à la fonction print() En insérant la séquence \n dans les chaînes de caractères.
print( " * \n * * \n * *\n * *\n *** ***\n * *\n * *\n *****")
#Agrandir la flèche deux fois plus Tout en conservant les proportions.
print( " * \n * * \n * *\n * *\n", 2 *( "*** *** "), ("\n * *\n * *\n *****"))
#Dupliquer la flèche
print( " * \n * * \n * *\n * *\n",2*(2 *( "*** *** ")), ("\n * *\n * *\n *****"))
#Supprimer certains guillemetsObservez attentivement la réponse de Python. Portez une attention particulière à l'endroit où Python
#détecte une erreur ‒ est-ce bien l'endroit où l'erreur se trouve réellement ?
print(  * \n * * \n * *\n * *\n,2*(2 *( "*** *** ")), ("\n * *\n * *\n *****"))
#SyntaxError: unexpected character after line continuation character
print(  * \n * * \n * *\n * *\n,2*(2 *( "*** *** ")), ("\n * *\n * *\n *****"))
#Faire de même avec certaines parenthèses Supprimez-en quelques-unes et observez ce qu'il se passe.
print( " * \n * * \n * *\n * *\n",2*(2 * "*** *** "), ("\n * *\n * *\n *****"))
#SyntaxError: unexpected character after line continuation character
#Changer les mots print en autre chose Modifiez uniquement la casse (par exemple, Print) ‒ que se passe-t-il maintenant ?
pow( " * \n * * \n * *\n * *\n",2*(2 *( "*** *** ")), ("\n * *\n * *\n *****"))
#SyntaxError: unexpected character after line continuation character
#Remplacer certains guillemets par des apostrophes Regardez attentivement le comportement de Python.
print( ' * \n * * \n * *\n * *\n *** ***\n * *\n * *\n *****')
#SyntaxError: unexpected character after line continuation character
#de part mon observation python detecte les erreurs des syntax