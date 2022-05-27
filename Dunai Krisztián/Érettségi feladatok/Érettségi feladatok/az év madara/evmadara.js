var evmadara = [];
evmadara[1979] = "gyurgyalag";
evmadara[1980] = "fehér gólya";
evmadara[1981] = "fehér gólya";
evmadara[1982] = "a fecskék";
evmadara[1983] = "a fecskék";
evmadara[1984] = "a cinegék";
evmadara[1985] = "gyöngybagoly";
evmadara[1986] = "túzok";
evmadara[1987] = "fogoly";
evmadara[1988] = "kuvik";
evmadara[1989] = "búbos banka";
evmadara[1990] = "búbos banka";
evmadara[1991] = "európai szalakóta";
evmadara[1992] = "vörös vércse";
evmadara[1993] = "barátposzáta";
evmadara[1994] = "fehér gólya";
evmadara[1995] = "fülemüle";
evmadara[1996] = "vörösbegy";
evmadara[1997] = "harkályok";
evmadara[1998] = "harkályok";
evmadara[1999] = "fehér gólya";
evmadara[2000] = "kerecsensólyom";
evmadara[2001] = "bíbic";
evmadara[2002] = "sárgarigó";
evmadara[2003] = "pacsirták";
evmadara[2004] = "rozsdafarkúak";
evmadara[2005] = "parlagi sas";
evmadara[2006] = "tövisszúró gébics";
evmadara[2007] = "mezei veréb";
evmadara[2008] = "kanalasgém";
evmadara[2009] = "kék vércse";
evmadara[2010] = "a fecskék";
evmadara[2011] = "széncinege";
evmadara[2012] = "egerészölyv";
evmadara[2013] = "gyurgyalag";
evmadara[2014] = "túzok";
evmadara[2015] = "búbos banka";

function frissit(){
    var ev = document.getElementById('ev').value;
    evszam.innerHTML = ev;
    madar.innerHTML = evmadara[ev];
    nagyKezdo()
}

function nagyKezdo(szoveg){
    return szoveg.charAt(0).toUpperCase() + szoveg.slice(1);
}

function veletlen(){
    ev.value=Math.floor(Math.random() * 36) + 1979;
    return frissit();
    
}