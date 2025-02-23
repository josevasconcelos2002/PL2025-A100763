# TPC2

Data: 14/02/2025 <br>
Nome: José Pedro Torres Vasconcelos <br>
Número Mecanográfico: A100763 <br> <br> <br>

![José Vasconcelos, A100763](/images/me.png)


<br>

## **Resumo**
Programa escrito em python, sem utilizar o módulo CSV, que lê o ![dataset fornecido](./assets/obras.csv), processa-o e cria os seguintes resultados:

* Lista ordenada alfabeticamente dos compositores musicais;

* Distribuição das obras por período: quantas obras catalogadas em cada período;

* Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.


## **Resultados**

**Lista ordenada alfabeticamente dos compositores musicais:**

```
[
'Alessandro Stradella', 'Antonio Caldara', 'Antonio Maria Abbatini', 'Baldassare Galuppi', 'Barbara Strozzi', 'Barbara of Portugal',
'Bernardo Pasquini', 'Carlos Seixas', 'Claude Balbastre', 'Claudio Monteverdi', 'Cristofaro Caresana', 'David Perez',
'Dieterich Buxtehude', 'Domenico Scarlatti', 'Duarte Lobo', 'Duarte Lôbo', 'Elisabeth Sophie of Mecklenburg', "Emanuele d'Astorga",
'Estevao de Brito', 'Filpe Da Madre De Deus', 'Francesco Cavalli', 'Francesco Durante', 'Franz Benda', 'Friederike Sophie Wilhelmine',
'Gaspar Fernandes', 'Gaspar Sanz', 'Georg Bohm', 'George Frideric Handel', 'Giacomo Carissimi', 'Giovanni Battista Bassani',
'Giovanni Battista Bononcini', 'Giovanni Battista Martini', 'Giovanni Battista Pergolesi', 'Giovanni Battista Sammartini',
'Giovanni Gabrieli', 'Giovanni Legrenzi', 'Giuseppe Sammartini', 'Giuseppe Tartini', 'Gregor Aichinger', 'Gregorio Allegri',
'Guillaume-Gabriel Nivers', 'Heinrich Ignaz Franz Biber', 'Heinrich Scheidemann', 'Henri Desmarets', 'Jacopo Peri', 'Jacques Boyvin',
'Jan Pieterszoon Sweelinck', 'Jean Titelouze', 'Jean-Baptiste Lully', 'Jean-Jacques Rousseau', 'Jean-Joseph Mondonville',
'Jean-Joseph Mouret', 'Jean-Marie Leclair', 'Jean-Philippe Rameau', 'Jeremiah Clarke', 'Joachim Neander', 'Johann Adam Reincken',
'Johann Adolph Hasse', 'Johann Christoph Bach', 'Johann Christoph(er) Pepusch', 'Johann David Heinichen', 'Johann Ernst Eberlin',
'Johann Hermann Schein', 'Johann Jakob Froberger', 'Johann Joachim Quantz', 'Johann Krieger', 'Johann Ludwig Krebs', 'Johann Mattheson',
'Johann Michael Bach', 'Johann Nicolaus Bach', 'Johannes Schenck', 'John Blow', 'John Bull', 'John Dowland', 'John IV', 'John Weldon',
'Joseph Gibbs', 'Juan Bautista Cabanilles', 'Leopold I', 'Lodovico Grossi da Viadana', 'Louis Couperin', 'Manuel Correia', 'Manuel Machado',
'Manuel Rodriguez Coelho', 'Marc-Antoine Charpentier', 'Marin Marais', 'Melchior Schildt', 'Monsieur de Sainte-Colombe',
'Nicola Francesco Haym', 'Nicolas Siret', 'Nicolaus Bruhns', 'Orlando Gibbons', 'Paolo Agostino', 'Pedro de Araujo', 'Peter Philips',
'Pierre Beauchamp', 'Pietro Della Valle', 'Robert Cambert', 'Samuel Scheidt', 'Stefano Landi', 'Tomaso Albinoni',
'Wilhelm Friedemann Bach', 'Wilhelmine of Prussia'
]
```
<br>

**Distribuição das obras por período: quantas obras catalogadas em cada período:**

```
{
    'Barroco': 23,
    'Clássico': 15,
    'Medieval': 46,
    'Renascimento': 39, 
    'Século XX': 17, 
    'Romântico': 16, 
    'Contemporâneo': 7
}
```
<br>

**Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.**

```
{
    'Barroco': ['Rage Over a Lost Penny', 'Military Band No. 1', 'The Rondo', 'Ab Irato', 'Die Ideale, S.106', 'Fantasy No. 2',
    'Hungarian Rhapsody No. 16', 'Hungarian Rhapsody No. 5', 'Hungarian Rhapsody No. 8', 'Impromptu Op.51', 'In the Steppes of Central Asia',
    'Mazurkas, Op. 50', 'Nocturne in C minor', 'Paganini Variations, Book I', 'Polonaise Op. 44', 'Polonaise-Fantasie', 'Polonaises Op.71',
    'Preludes Op. 49', 'Prince Rostislav', 'Rondo Op. 5', 'Shéhérazade, ouverture de féerie', 'Symphonies de Beethoven', 'Études Op.10'],
    
    'Clássico': ['Zärtliche Liebe', 'Bamboula, Op. 2', 'Capriccio Italien', 'Czech Suite', 'French Overture', 'Hungarian Rhapsody No. 14',
    'Hungarian Rhapsody No. 18', 'Händelgesellschaft volume 50', "In Nature's Realm", 'Mass in C major', 'Scherzo No.3',
    'Serenade for Strings in G minor', 'Serenata Notturna', 'Stabat Mater', 'Suite for Orchestra in B minor'],

    'Medieval': ['Three Pieces for Orchestra', 'Adagio in B minor', 'Ballade No.1', 'Ballades, Op. 10', 'Barcarole Op. 60', 'Coriolan Overture',
    'Dixit Dominus', 'Eroica Variations', 'Fantasia and Fugue, BWV 542, G minor', 'Fantasia in D minor', 'Fantasy on Hungarian Folk Themes',
    'Faust Overture', 'Gigue in G major, K. 574', 'Grande valse brillante', 'Hungarian Rhapsody No. 11', 'Hungarian Rhapsody No. 13',
    'Hungarian Rhapsody No. 15', 'Hungarian Rhapsody No. 3', 'Hungarian Rhapsody No. 4', 'Hungarian Rhapsody No. 7', 'Impromptu, Op. 29',
    'La Savane', 'Mazurkas, Op. 30', 'Mazurkas, Op. 63', 'Mazurkas, Op. 67', 'Mazurkas, Op. 68', 'Morceau de salon', 'Preludes Op. 11 No. 4',
    'Preludes Op. 74', 'Première rhapsodie', 'Prélude, Choral et Fugue', 'Rhapsodie Espagnole', 'Romance in F major', 'Rondo for Piano No. 3',
    'Serenade for Wind Instruments', 'Suite No. 1 for two pianos', 'Suite No. 2 for two pianos', 'Suite in D minor, HWV 437', 'Tapiola',
    'The Noon Witch', 'Tragic Overture', 'Tönet, ihr Pauken! Erschallet, Trompeten!, BWV 214', 'Valses Sentimentales', 'Variations in F minor',
    'Variations on a Theme of Corelli, Op. 42', 'Wedding day at Troldhaugen'],
 
    'Renascimento': ['Bagatelles, Opus 119', 'Bagatelles, Opus 33', 'Cantatas, BWV 141-150', 'Carnival Overture', 'Estampes',
    'Fantaisie brillante, Op. 22', 'Festklänge, S.101', 'Funeral March in Memory of Rikard Nordraak', 'Hamlet, S.104',
    'Hungarian Rhapsody No. 10', 'Hungarian Rhapsody No. 12', 'Hungarian Rhapsody No.1', 'Komm, Jesu, komm!', "L'Art de varier",
    'Le Mancenillier', 'Legends, Op.59', 'Liturgy of St. John Chrysostom', 'Marie-Magdeleine', 'Mazurkas, Op. 56', 'Morceaux de Salon, Op. 10',
    'Nocturne in A-flat', 'Othello', 'Polonaises, Op.26', 'Preludes Op. 11', 'Preludes, Op. 32', 'Romance in G major', 'Rondo Op. 1',
    'Scans of the Bach Gesellschaft edition of the Eight Short Preludes and Fugues', 'Scherzo No.4', "Schubert's Valses Nobles", 'Shéhérazade',
    'Six Pieces for Piano, Op. 118', "St. Paul's Suite", 'Symphonic Dances, Op. 64', 'The Creatures of Prometheus', 'Transcendental Études',
    'Valse romantique', 'Variation on a Waltz by Diabelli', 'Vers la flamme'],
  
    'Século XX': ['Berceuse', 'Eleven Chorale Preludes, Op. 122', 'Fürchte dich nicht', 'Hungarian Rhapsody No. 17', 'Hungarian Rhapsody No. 9',
    'Nocturnes Op. Posth. 72', 'Papillons', 'Peer Gynt Suite Suite No. 1', 'Serenade for Strings', 'Sigurd Jorsalfar',
    'Singet dem Herrn ein neues Lied', 'Sonatas and Partitas for Solo Violin', 'Sonatina in F major', 'Sonatina in G',
    "Symphonic Poem No.1, Ce qu'on entend sur la montagne", 'The Storm, Op.76', 'Variations on a Theme of Chopin, Op. 22'],
   
    'Romântico': ['Book II', 'Fantasy No. 4', "Feu d'artifice", "Feuilles d'Album", 'Grande Tarantelle', "Jeux d'enfants",
    'Lobet den Herrn, alle Heiden', 'Moments musicaux', 'Overture, Scherzo and Finale', 'Preludes Op. 59',
    'Präludium und Fuge über das Thema B-A-C-H', 'Psalm 42 , Op. 42', 'Salve Regina', 'Scherzo No. 2', 'Syrinx', 'Waltzes, Op. 34'],
    
    'Contemporâneo': ['Impromptu, Op. 36', 'Les cinq doigts', 'Polonaises, Op.40', 'Preludes Opus 51', 'Rhapsodies, Op. 79',
    'Sonnerie de Ste-Geneviève du Mont-de-Paris', 'Études Op. 25']
}
```
<br>

