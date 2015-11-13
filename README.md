# Ceropath

This README outlines the details of collaborating on this Ember application.
A short introduction of this app could easily go here.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Node.js](http://nodejs.org/) (with NPM)
* [Bower](http://bower.io/)
* [Ember CLI](http://www.ember-cli.com/)
* [PhantomJS](http://phantomjs.org/)

## Installation

* `git clone <repository-url>` this repository
* change into the new directory
* `npm install`
* `bower install`


## Running / Development

* `node backend`
* `npm start` (in another terminal)
* Visit your app at [http://localhost:4200](http://localhost:4200).


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


### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Deploying

* create a file named `secret.json` with the following structure:

    {
        "secret": "a-secret-string",
        "email": "email@tocontact.com"
    }

* `eureka dockerize`
* `docker-compose up


