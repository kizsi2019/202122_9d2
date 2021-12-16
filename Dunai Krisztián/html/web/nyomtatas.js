function kalkulal() {
    //Űrlapadatok
    const szelesseg=document.getElementById("szelesseg").value
    const magassag=document.getElementById('magassag').value;
    const papir=document.getElementById('papirtipus').value;
    //Számítások
    let terulet=Math.round((szelesseg*magassag)/10000);    
    let koltseg=terulet*papir;

    //Megjelenítés
    document.getElementById('koltseg').style.visibility = "visible";
}

