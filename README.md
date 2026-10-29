# README page for Skolekantine prosjekt 2026
<P> En skolekantine med CSS, HTML og Python </P>


## PROSJEKTBESKRIVELSE
<p> Skolekantinen er et prosjekt som handler om å lage en "nettside" til en skolekantine. Nettsiden har hovedmenyen, varene, menyen og en side der du kan finne hvor man kontakter skolen.</p>




## HVORDAN VIRKER PROGRAMMET?
<p> Programmet fungerer via flask - der du "åpner" en port og alt sammen blir satt sammen til et nettside som du kan se. (Skriv mer)</p>


## KILDELISTE
<P> Hva slags prompter er det jeg har brukt til prosjektet?</P>

#### Data.py:

`"Hei, Claude. Kan du lage meg en "liste" som skal være i min /data.py som inneholder varer og varmmat (Meny). Det I varer så skal det inneholde maten, prisen og en image.png."`

```
VARER = [
    {"mat": "Baguett med skinke og ost", "pris": 49, "image": "image.png"},
    {"mat": "Baguett med kylling", "pris": 55, "image": "image.png"},
    {"mat": "Salat med tunfisk", "pris": 59, "image": "image.png"},
    {"mat": "Eple", "pris": 10, "image": "image.png"},
    {"mat": "Banan", "pris": 8, "image": "image.png"},
    {"mat": "Yoghurt", "pris": 22, "image": "image.png"},
    {"mat": "Sjokoladebar", "pris": 18, "image": "image.png"},
```
#### Style.css:

<p> INGEN KI BRUKT ENDA </p>



#### HTML- sidene:

##### meny.html
`Hey Claude, I have this rough illustration / sketch that I want to recreate in CSS + HTML. I'm just not quite sure on how to do this, Can you help? (image of the illustration) + (current HTML code)`

<p> HTML </p>

```
<div class="meny">
    {% for dag, retter in meny.items() %}
    <section class="dag">
        <h1>{{ dag }}</h1>
        <h2>{{ retter[0].navn }} &amp; {{ retter[1].navn }}</h2>

        <div class="boxes">
            {% for mat in retter %}
            <div class="box {{ 'mat1' if loop.first else 'mat2' }}">
                <img class="item-image"
                     src="{{ url_for('static', filename='img/' + mat.image) }}"
                     alt="Du mangler {{ mat.navn }} pls fiks NÅÅÅ ELLER SÅ BLIR DET DENG">
                <div class="item">
                    <span class="item-navn">{{ mat.navn }}</span>
                    <span class="item-pris">{{ mat.pris }},-</span>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>
    {% endfor %}
</div>
```

<p> CSS </p>

```

.meny {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
}

.dag {
    margin-bottom: 4rem;
}

.dag h1 {
    margin: 0;
    text-align: center;
    font-size: 4.5rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.dag h2 {
    margin: 0.5rem 0 1rem;
    text-align: center;
    font-size: 2rem;
    font-weight: normal;
}

.boxes {
    display: flex;
    gap: 1.5rem;
    align-items: stretch;
}

.box {
    border: 4px solid #000;
    border-radius: 12px;
    padding: 1rem;
    min-height: 200px;
}

.box.mat1 { flex: 1.2; }
.box.mat2 { flex: 1; }

.item-image {
    display: block;
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 8px;
}

.item {
    display: flex;
    justify-content: space-between;
    margin-top: 0.75rem;
    font-size: 1.25rem;
}

@media (max-width: 600px) {
    .boxes { flex-direction: column; }
    .dag h1 { font-size: 3rem; }
}
```

`Hey Claude, I need help bringing my .Start h1 down to match the other texts. (insert picture of the current layout) (Insert .Start h1, .Start & .home-content CSS.`
```
/* delete this: */
.Start {
  margin-bottom: auto;
}

.home-content {
  z-index: 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}                              /* your pasted rule was missing this closing brace */

.Start h1 {
  margin-bottom: 20px;         /* space between the title and "Kort informasjon" */
  padding-top: 0;              /* removes the big gap above the title */
}
```



## BRUKERTESTING


## SIKKERHETSPRINSIPPER


## Notater til skrivingen av readme.html



- Navn på prosjektet
- Prosjektbeskrivelse. Må inneholde en oversikt over de viktigste funksjonene og hva brukerne kan gjøre på nettsiden. Må inneholde hvilke programmeringsspråk du har brukt i prosjektet.
- Hvordan kjøre programmet. (Må noe lastes ned, må man skrive noe spesielle syntaxer?)
- Litterturliste/kildeliste (for eksempel stack-overflow, chat gpt osv.)
- Brukertesting (hvis brukertesting) og tilbakemeldinger.
- Hvilke sikkerhetsprinsipper som er implementert

`inline kode`

```

```
