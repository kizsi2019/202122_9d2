var sulinevek = [];
sulinevek['bercsenyi'] = 'Bercsényi Miklós Élelmiszeripari Szakközépiskola';
sulinevek['giorgio'] = 'Giorgio Perlasca Kereskedelmi, Vendéglátóipari Szakközépiskola és Szakiskola';
sulinevek['keleti'] = 'Keleti Károly Közgazdasági Szakközépiskola';
sulinevek['magyar'] = 'Magyar Gyula Kertészeti Szakközépiskola és Szakiskola';
sulinevek['pataky'] = 'Pataky István Híradásipari és Informatikai Szakgimnázium';
sulinevek['szlaszlo'] = 'Szent László Gimnázium';
sulinevek['zrinyi'] = 'Zrínyi Miklós Gimnázium';

function mutat(sulinev){    
    document.getElementById('sulikep').src = 'iskolak/'+sulinev+'.jpg';
    document.getElementById('sulikep').title = sulinevek[sulinev];
}
