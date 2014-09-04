CERoPath
--------


## Pipeline

Le pipeline de CERoPath a besoin des binaires suivant:

 * muscle : (lien vers le binaire : http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux32)
 * dnadist : http://evolution.genetics.washington.edu/phylip/getme.html
 * BIONJ : http://www.atgc-montpellier.fr/bionj/binaries.php
 * R : installer R-core et R-devel.

Muscle, dnadist et BIONJ sont fournit avec le projet mais en cas de problème de licence il faut aller chercher les binaires sur les sites correspondants.

Le pipeline demande l'installation de deux packages R::

    # R
    > install.packages('ape')
    > install.packages('RSVGTipsDevice')

Puis éditer le fichier `bin/nwk2svg.r` et remplacer dans la première ligne, le chemin absolute vers le répertoire `data/pipeline`