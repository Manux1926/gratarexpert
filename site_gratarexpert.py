from build import AFF_NOTE

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
function f(x,d){return (+x).toLocaleString('ro-RO',{maximumFractionDigits:d||0})}
var c=$('#calc');if(!c)return;
function run(){
 var ad=+$('#ad').value||0,co=+$('#co').value||0,ap=+$('#ap').value,mp=(+$('#mp').value||0)/100,dur=+$('#dur').value||0,tip=$('#tip').value;
 var g=ad*ap+co*ap*0.5;
 var kgTot=g/1000;
 var kgMici=kgTot*mp,kgCarne=kgTot-kgMici;
 var mici=Math.ceil(kgMici*1000/65);
 var carb=0;if(tip==='carbune'){carb=Math.max(2,1.5+kgTot*0.6+Math.max(0,dur-1.5)*1)}else if(tip==='brichete'){carb=Math.max(2,1.2+kgTot*0.5+Math.max(0,dur-1.5)*0.8)}
 var gaz=tip==='gaz'?(0.35*dur*(kgTot>6?1.5:1)):0;
 var chifle=Math.ceil((ad+co*0.5)*1.5);
 $('#rKg').textContent=f(kgTot,1)+' kg';$('#rMici').textContent=f(mici)+' buc.';$('#rCarne').textContent=f(kgCarne,1)+' kg';
 $('#rFoc').textContent=tip==='gaz'?f(gaz,1)+' kg GPL':f(carb,1)+' kg';$('#rFocL').textContent=tip==='gaz'?'Gaz estimat':(tip==='brichete'?'Brichete':'Cărbune');
 $('#rList').innerHTML=['<li><b>'+f(mici)+' mici</b> (~'+f(kgMici,1)+' kg pastă) – socotim 65 g/bucată, crud</li>','<li><b>'+f(kgCarne,1)+' kg</b> ceafă, piept sau cârnați (carne crudă)</li>','<li><b>'+f(chifle)+'</b> chifle sau felii de pâine</li>','<li>Muștar: un borcan de ~300 g la fiecare ~25 de mici</li>','<li>Legume pentru grătar: ~150 g de persoană (ardei, ciuperci, dovlecei)</li>'].join('');
}
c.addEventListener('input',run);c.addEventListener('change',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Calculator grătar: câtă carne, câți mici și cât cărbune</h2>
<div class="grid3">
<div><label class="f" for="ad">Adulți</label><input id="ad" type="number" min="0" value="8"></div>
<div><label class="f" for="co">Copii</label><input id="co" type="number" min="0" value="2"></div>
<div><label class="f" for="ap">Apetit</label><select id="ap"><option value="300">Moderat (300 g/adult)</option><option value="400" selected>Normal (400 g/adult)</option><option value="500">Mare (500 g/adult)</option></select></div>
<div><label class="f" for="mp">Cât din carne să fie mici (%)</label><input id="mp" type="number" min="0" max="100" value="50"></div>
<div><label class="f" for="dur">Durata grătarului (ore)</label><input id="dur" type="number" min="0.5" step="0.5" value="2"></div>
<div><label class="f" for="tip">Pe ce gătești</label><select id="tip"><option value="carbune">Cărbune de lemn</option><option value="brichete">Brichete</option><option value="gaz">Grătar pe gaz</option></select></div>
</div>
<div class="res"><div class="big"><div class="kpi main"><span>Carne crudă în total</span><b id="rKg">–</b></div><div class="kpi"><span>Mici</span><b id="rMici">–</b></div><div class="kpi"><span>Alte cărnuri</span><b id="rCarne">–</b></div><div class="kpi"><span id="rFocL">Cărbune</span><b id="rFoc">–</b></div></div>
<h3 style="margin:16px 0 4px">Lista de cumpărături</h3><ul id="rList"></ul>
<p class="note">Estimări orientative, pentru carne crudă (la gătire se pierde 20–30% din greutate). Rotunjește în sus dacă vin invitați surpriză.</p></div></form></div>"""

TYPES = """<div class="tw"><table class="t"><tr><th>Tip</th><th>Gust</th><th>Pornire</th><th>Potrivit pentru</th></tr>
<tr><td>Cărbune / brichete (kettle, grătar clasic)</td><td>Aromă afumată tipică</td><td>20–30 min</td><td>Mici, ceafă, grătarul de weekend</td></tr>
<tr><td>Gaz</td><td>Mai neutru</td><td>5–10 min</td><td>Gătit des, rapid, pe terasă</td></tr>
<tr><td>Kamado (ceramic)</td><td>Foarte bun, umed</td><td>20–30 min</td><td>Gătit lent, afumat, pizza; consum mic de cărbune</td></tr>
<tr><td>Peleți</td><td>Afumat, controlat</td><td>~15 min</td><td>Gătit lent cu temperatură automată</td></tr>
<tr><td>Electric</td><td>Neutru</td><td>~10 min</td><td>Balcon, unde focul deschis nu e permis</td></tr></table></div>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Regula rapidă: 400 g de carne de om</h2>
<p>Pentru un grătar cu garnituri, socotește <strong>300–400 g de carne crudă pentru fiecare adult</strong> și jumătate pentru copii. Dacă grătarul este „masa principală” fără multe garnituri sau invitații sunt pofticioși, urcă la 500 g. Un mic crud are în jur de 60–70 g, deci 4–5 mici de om acoperă jumătate din porție.</p>
<h2>Ce grătar ți se potrivește</h2>""" + TYPES + """
<p>Detalii și recomandări în <a href="/tipuri-de-gratar.html">ghidul tipurilor de grătar</a>.</p></section>
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/tipuri-de-gratar.html"><span class="tag">Ghid</span><b>Cărbune, gaz, kamado sau peleți?</b><span>Ce tip de grătar alegi și de ce.</span></a>
<a class="c" href="/gratar-pe-gaz-cum-alegi.html"><span class="tag">Cumpărare</span><b>Cum alegi un grătar pe gaz</b><span>Arzătoare, putere, materiale și capcane.</span></a>
<a class="c" href="/carbune-sau-brichete.html"><span class="tag">Ghid</span><b>Cărbune sau brichete?</b><span>Cât ține focul și cât consumi.</span></a></div></section>"""

FAQ = [
    ('Câți mici se socotesc de persoană?', 'Între 4 și 5 mici de adult dacă mai sunt și alte cărnuri, și 6–8 dacă micii sunt singurul fel. Un mic crud cântărește de obicei 60–70 g.'),
    ('Câtă carne iau pentru 10 persoane la grătar?', 'Pentru 10 adulți, cu garnituri, 3–4 kg de carne crudă; fără garnituri sau cu invitați pofticioși, 4,5–5 kg.'),
    ('Cât cărbune îmi trebuie?', 'Pentru un grătar de 1–2 ore pe un kettle obișnuit, 2–3 kg de cărbune sau brichete. Pentru sesiuni lungi sau cantități mari de carne, adaugă cam 1 kg pe oră în plus.'),
]

ART_TIP = """<p>„Grătarul” înseamnă azi cinci lucruri diferite. Alegerea depinde de cât de des gătești, unde locuiești și cât timp ai de pierdut cu focul.</p>""" + TYPES + """
<h2>Cărbune: clasicul</h2><p>Gustul afumat pe care îl asociem cu micii vine de aici. Un grătar kettle cu capac (forma de „ou”) e cel mai versatil: gătești direct, la foc mare, și indirect, cu capacul închis, pentru bucăți mari. Dezavantaj: aprinderea și curățenia.</p>
<h2>Gaz: pentru cine gătește des</h2><p>Pornește în câteva minute și ține o temperatură constantă. Ideal pentru cine face grătar de mai multe ori pe săptămână. Gustul afumat se poate obține cu o cutie de afumare cu așchii de lemn. Vezi <a href="/gratar-pe-gaz-cum-alegi.html">cum alegi unul</a>.</p>
<h2>Kamado: investiția pe termen lung</h2><p>Un vas ceramic gros, care păstrează căldura foarte bine și consumă puțin cărbune. Excelent pentru gătit lent, afumat și pizza. Este greu și mai scump, dar ține mulți ani.</p>
<h2>Peleți: termostat pentru afumat</h2><p>Un melc alimentează automat peleții din lemn, iar un controler ține temperatura setată. Comod pentru gătit lent, dar are nevoie de curent electric și de peleți alimentari, nu de cei pentru centrală.</p>
<h2>Electric: soluția pentru bloc</h2><p>Pe balcon, focul deschis și fumul pot fi interzise de regulamentul blocului sau pot deranja vecinii. Grătarul electric e singura variantă sigură.</p>
<h2>Recomandarea noastră</h2><ul><li>Faci grătar de câteva ori pe vară: kettle pe cărbune.</li><li>Faci grătar săptămânal: gaz, cu 3 arzătoare.</li><li>Îți place gătitul lent: kamado sau peleți.</li><li>Stai la bloc: electric.</li></ul>""" + AFF_NOTE

ART_GAZ = """<p>Un grătar pe gaz bun ține 10 ani sau mai mult. Unul prost ruginește în două sezoane. Iată la ce să te uiți.</p>
<h2>1. Numărul de arzătoare</h2><p>Două arzătoare ajung pentru 2–4 persoane. Trei sau patru îți permit zone cu temperaturi diferite, inclusiv gătit indirect (un arzător oprit sub carne, celelalte pornite).</p>
<h2>2. Puterea nu e totul</h2><p>Producătorii afișează puterea totală în kW. Mai important decât cifra totală este cât de uniform se distribuie căldura și cât de bine închide capacul. Un capac dublu și un termometru precis valorează mai mult decât câțiva kW în plus.</p>
<h2>3. Materialele</h2><ul><li><strong>Grătarul de gătit:</strong> fonta emailată ține căldura și lasă dungi frumoase; inoxul gros e ușor de curățat.</li><li><strong>Corpul:</strong> oțel emailat sau inox. Inoxul subțire de calitate slabă poate rugini.</li><li><strong>Arzătoarele:</strong> din inox, cu garanție lungă.</li></ul>
<h2>4. Accesorii utile</h2><p>Arzător lateral pentru sosuri, plită pentru legume, sistem de colectare a grăsimii ușor de scos și husă de protecție.</p>
<h2>5. Siguranța</h2><p>Folosește butelii verificate, regulator potrivit și furtun în termen de valabilitate. Verifică etanșeitatea cu apă cu săpun la fiecare montare a buteliei.</p>""" + AFF_NOTE

ART_CARB = """<p>Cărbunele de lemn și brichetele fac același lucru, dar se comportă diferit. Alegerea contează pentru cât ține focul și cât consumi.</p>
<h2>Cărbunele de lemn (în bucăți)</h2><ul><li>Se aprinde mai repede și atinge temperaturi mari.</li><li>Arde mai repede; bun pentru mici și fripturi subțiri.</li><li>Bucăți de mărimi diferite, deci căldură mai puțin uniformă.</li></ul>
<h2>Brichetele</h2><ul><li>Se aprind mai greu, dar ard mai mult și mai uniform.</li><li>Bune pentru gătit indirect și sesiuni lungi.</li><li>Alege brichete fără aditivi chimici, din cărbune de lemn presat.</li></ul>
<h2>Cât consumi</h2><p>Pentru un grătar de 1–2 ore pe un kettle obișnuit, 2–3 kg sunt suficiente. Folosește un coș de aprindere (horn): în 15–20 de minute cărbunele e gata, fără lichid de aprindere, care lasă gust neplăcut.</p>
<h2>Când e gata focul</h2><p>Cărbunii sunt gata când se acoperă cu un strat subțire de cenușă albă. Fă un test simplu: ține palma la 10–12 cm deasupra grătarului. Dacă o retragi după 2–3 secunde, focul e mare (bun pentru mici); la 5–7 secunde, focul e mediu.</p>
<div class="box info">Socotește cărbunele și carnea pentru petrecerea ta cu <a href="/">calculatorul de grătar</a>.</div>"""

SITE = {
    'name': 'GrătarExpert', 'domain': 'gratarexpert.online',
    'c1': '#a63d17', 'c2': '#e0662b', 'accent': '#ffd166',
    'mark': '<path d="M14 28h36a18 18 0 0 1-36 0z" fill="#fff"/><path d="M24 46l-4 10M40 46l4 10" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M26 12c3 4-2 6 1 10M34 10c3 4-2 6 1 10" stroke="#ffd166" stroke-width="3" fill="none" stroke-linecap="round"/>',
    'tagline': 'Totul pentru grătarul perfect: cantități, tipuri de grătar, ghiduri de cumpărare și sfaturi de gătit.',
    'badges': ['Calculator mici și cărbune', 'Ghiduri de cumpărare', 'Gratuit'],
    'nav': [('/', 'Calculator'), ('/tipuri-de-gratar.html', 'Tipuri de grătar'), ('/gratar-pe-gaz-cum-alegi.html', 'Grătar pe gaz'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator grătar: carne, mici, cărbune',
    'side_title': 'Câtă carne îți trebuie?', 'side_text': 'Calculează carnea, micii și cărbunele pentru oricâte persoane.',
    'about': '<p>GrătarExpert este un site independent pentru pasionații de grătar din România: ghiduri de cumpărare, calculatoare practice și sfaturi de gătit, testate la grătarul de acasă.</p><p>Unele linkuri către magazine pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Calculator grătar: câtă carne și câți mici de persoană', 'kind': 'tool', 'short': 'Calculator grătar', 'appcat': 'LifestyleApplication',
         'desc': 'Calculează câtă carne, câți mici, câte chifle și cât cărbune îți trebuie la grătar pentru oricâți invitați. Plus ghiduri pentru alegerea grătarului.',
         'h1': 'Calculator grătar: câtă carne, câți mici și cât cărbune', 'toolname': 'Calculator cantități grătar',
         'lead': 'Spune-ne câți invitați ai și ce pui pe grătar. Îți facem lista de cumpărături în câteva secunde.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'tipuri-de-gratar', 'title': 'Grătar pe cărbune, gaz, kamado sau peleți: ce alegi?', 'kind': 'article', 'short': 'Tipuri de grătar',
         'desc': 'Comparație între grătarele pe cărbune, gaz, kamado, peleți și electrice: gust, timp de pornire, preț și pentru cine se potrivește fiecare.',
         'h1': 'Cărbune, gaz, kamado sau peleți: ce grătar alegi', 'lead': 'Cinci tipuri de grătar, explicate fără jargon, și recomandarea pentru fiecare stil.', 'body': ART_TIP},
        {'slug': 'gratar-pe-gaz-cum-alegi', 'title': 'Cum alegi un grătar pe gaz: ghid de cumpărare', 'kind': 'article', 'short': 'Cum alegi un grătar pe gaz',
         'desc': 'Ce contează la un grătar pe gaz: numărul de arzătoare, putere, materiale, accesorii și siguranța buteliei. Ghid de cumpărare pentru 2027.',
         'h1': 'Cum alegi un grătar pe gaz care ține 10 ani', 'lead': 'Cinci criterii care separă un grătar bun de unul care ruginește în două veri.', 'body': ART_GAZ},
        {'slug': 'carbune-sau-brichete', 'title': 'Cărbune sau brichete pentru grătar? Cât consumi', 'kind': 'article', 'short': 'Cărbune sau brichete',
         'desc': 'Diferențele dintre cărbunele de lemn și brichete, cât consumi la un grătar de 2 ore și cum îți dai seama că focul e gata.',
         'h1': 'Cărbune sau brichete: ce folosești și cât îți trebuie', 'lead': 'Cum ard, cât țin și testul palmei pentru temperatura focului.', 'body': ART_CARB},
    ]
}
