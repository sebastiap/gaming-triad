# Sobre este proyecto

## Generales 

Proyecto Ludico y practica de JAVA.

## Funcionamiento
Este programa generara jsons para ser utilizados en apps y juegos que lo requieran.
Se puede generar con 2 metodos :
 * Leyendo un archivo "attributes.txt".
 * Ingresando a mano todas las categorias.

### Principales Clientes
 * Gaming Triad (Winter Come).
 * Bookflix-Web (Grilla + Interface Clasica).

Para completar cada categoria tambien hay 2 maneras:
* Utilizando un template precargado.
* Ingresando a mano cada atributo a ser rellenado.

## Buenas Practicas y practicas al fin

* Se utilizo log4j2 a traves de un XML.
* Se utilizo este proyecto como caso practico de ***herencia***.
  
### Algunas reglas basicas para mantener las buenas practicas

#### Clases e Interfases
 * Los nombres comienzan con mayúsculas, se usan sustantivos o adjetivos.
 * Los nombres deben de ser descriptivos y no muy largos, con la primera letra de cada palabra que lo forma en mayúsculas.
 * Se han definido una serie de sufijos que deberán utilizarse en función del tipo de clase implementada:
 * Los nombres de clases serán simples y descriptivos, se utilizarán palabras completas y se evitarán acrónimos y abreviaturas.

#### Métodos
* En general se utilizarán verbos para nombrar a los métodos, describiendo la acción que realizan. 
* Se permite la utilización de get y set para capturar o establecer atributos de las mismas.
* Se utiliza camelCase.

#### Variables
 * Nombres cortos y descriptivos, normalmente sustantivos.
 * Se utiliza siempre el singular (excepto variables que almacenen un conjunto de elementos).
 * Las variables se nombran en minúsculas, en el caso de contener mas de una palabra, con la primera letra de las palabras en mayúscula exceptuando la primera.
 * Los nombres de variables no deben empezar con caracteres como subrayado "_" o "$".
   
#### Constantes
 * Las constantes deben nombrarse todas en mayúsculas. Se agregara "_" si contiene mas de una palabra.
