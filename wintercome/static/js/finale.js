// set up text to print, each item in array is new line
var aText = new Array(
"Logras escapar del centro comercial Fimbulvetr.",
"......",
"El frio parece haber retrocedido...",
"a medida que te alejas, puedes sentir que la tempertura aumenta...",
"fuera del mall, el ambiente parece normalizado.",
"Te preguntas que produjo aquel extraño suceso...",
"......",
"Muchas preguntas ocupan tu mente mientras vuelves a casa.",
"que sera de la gente que sigue atrapada ahi adentro?",
"que eran esos extraños animales y criaturas de hielo?",
"¿Eso paso en la vida real o fue solo una fantasia?",
"Hundido en tus pensamientos, te vas a dormir.",
"......",
"Al dia siguiente,todos los canales cubren la misma noticia",
"tanto en el mall, como en el resto del mundo",
"...El invierno ha llegado...",
"",
"",
"<a href='/newgame'>New Game + ?</a>"
);

var iSpeed = 90; // time delay of print out
var iIndex = 0; // start printing array at this posision
var iArrLength = aText[0].length; // the length of the text array
var iScrollAt = 20; // start scrolling up at this many lines

var iTextPos = 0; // initialise text position
var sContents = ''; // initialise contents variable
var iRow; // initialise current row

function typewriter()
{
 sContents =  ' ';
 iRow = Math.max(0, iIndex-iScrollAt);
 var destination = document.getElementById("typedtext");

 while ( iRow < iIndex ) {
  sContents += aText[iRow++] + '<br />';
 }
 destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "_";
 if ( iTextPos++ == iArrLength ) {
  iTextPos = 0;
  iIndex++;
  if ( iIndex != aText.length ) {
   iArrLength = aText[iIndex].length;
   setTimeout("typewriter()", 1000);
  }
 } else {
  setTimeout("typewriter()", iSpeed);
 }
}


typewriter();