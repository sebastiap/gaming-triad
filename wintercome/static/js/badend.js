// set up text to print, each item in array is new line
var aText = new Array(
"Despiertas.",
"Una Brisa Helada te atraviesa...",
"te causa el escalofrio mas largo que hayas experimentado.",
"...",
"El aturdimiento dura unos minutos...",
"abres los ojos y lo recuerdas:",
"Tu nombre es ...",
"...",
"<a href='/winter'>El invierno ha llegado...</a>"
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