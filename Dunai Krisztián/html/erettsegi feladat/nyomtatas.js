function kalkulal(){

    //Ürlapadatok
    const szelesseg=document.getElementById('szelesseg').value;
    const magassag=document.getElementById('magassag').value;
    const papir=document.getElementById('papirtipus').value;

    //Számítások
    let terulet=Math.round((szelesseg*magassag)/10000);    
    let koltseg=terulet*papir;


 document.getElementById('terulet').innerHTML = terulet;
 document.getElementById('koltseg').innerHTML = koltseg;
        document.getElementById('papir').innerHTML = papir;

    //Megjelenítés
    document.getElementById('valasz').style.visibility = "visible";
}
