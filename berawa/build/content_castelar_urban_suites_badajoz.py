# Contenido de la demo Castelar Urban Suites (Badajoz) (es/en/fr/de). Hechos de castelarurbansuites.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las suites reales.','en':' Images are illustrations and do not show the actual suites.','fr':' Les images sont des illustrations et ne montrent pas les suites réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Suiten.'}
H={'es':['Suite Arce y Suite Árbol de Fuego','Suite Jacaranda (familiar)'],'en':['Arce Suite and Árbol de Fuego Suite','Jacaranda Suite (family)'],'fr':['Suite Arce et Suite Árbol de Fuego','Suite Jacaranda (familiale)'],'de':['Suite Arce und Suite Árbol de Fuego','Suite Jacaranda (Familie)']}
RD={
'es':['Arce: vistas directas al Parque de Castelar desde el salón y el dormitorio. Árbol de Fuego: bañera exenta en el dormitorio, dos duchas enfrentadas, lavabo doble y WC cerrado independiente.','Dos dormitorios independientes con cama de 150 cm cada uno y sofá cama en el salón: hasta 6 personas.'],
'en':['Arce: direct views of Parque de Castelar from the living room and bedroom. Árbol de Fuego: freestanding bathtub in the bedroom, two facing showers, double washbasin and separate enclosed WC.','Two separate bedrooms with a 150 cm bed each and a sofa bed in the living room: up to 6 people.'],
'fr':['Arce : vue directe sur le Parque de Castelar depuis le salon et la chambre. Árbol de Fuego : baignoire îlot dans la chambre, deux douches face à face, double vasque et WC fermé séparé.','Deux chambres indépendantes avec un lit de 150 cm chacune et un canapé-lit au salon : jusqu’à 6 personnes.'],
'de':['Arce: direkter Blick auf den Parque de Castelar vom Wohn- und Schlafzimmer. Árbol de Fuego: freistehende Badewanne im Schlafzimmer, zwei gegenüberliegende Duschen, Doppelwaschbecken und separates WC.','Zwei getrennte Schlafzimmer mit je einem 150-cm-Bett und Schlafsofa im Wohnzimmer: bis zu 6 Personen.']}
ART={
'hero':('hills',9951,['#20302a','#d39a62','#efcd9c','#4f6f5b','#3a5747','#22362b']),
'intro':('arches',9952,['#ece7dd','#cf9660','#3d5a4a','#20302a','#121c17']),
'r1':('columns',9961,['#eeeeea','#f8f7f3','#3d5a4a','#2b4337','#16231c']),
'r2':('arches',9962,['#ebe4d8','#c98e58','#5a3b2b','#3a261b','#20150f']),
'g1':('hills',9971,['#e8eee6','#efe4cc','#d79f66','#97b39a','#6a8b6f','#46634b']),
'g2':('skyline',9972,['#243029','#d89d63','#f1d09f','#5b4a3e','#473a30','#2a221c']),
'g3':('waves',9973,['#20302a','#e3ab72','#f4d8ad','#3d5a4a','#2f4a3c','#18271f']),
'g4':('columns',9974,['#edece6','#f8f6f1','#5a3b2b','#3a261b','#20150f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Castelar Urban Suites · Apartamentos frente al Parque de Castelar, Badajoz',see_rooms='Ver las suites',hero_k='Badajoz · Edificio Presidente',hero_t='Diseño y confort frente al Parque de Castelar',hero_s='10 apartamentos de 3 tipos en el histórico Edificio Presidente, en el corazón de Badajoz.',
 intro_t='Donde la elegancia se encuentra con el confort',intro_p1='Diseño contemporáneo, materiales naturales, luz cuidada y espacios inteligentes, frente al Parque de Castelar y a 5 minutos a pie del casco histórico.',
 intro_p2='Check-in autónomo con cerradura inteligente a cualquier hora, anfitrión virtual por WhatsApp durante toda la estancia y bicicletas bajo petición.',
 stats=['10 apartamentos','3 tipos de suite','Check-in autónomo','Anfitrión virtual 24 h'],nav_rooms='Suites',rooms_t='Nuestras suites',rooms_s='Todas con cocina completa, cama de 150 cm, baño independiente, salón comedor, Wi-fi, TV y escritorio.',
 svcs=['Check-in autónomo','Anfitrión virtual 24 h','Bicicletas bajo petición','Cocina completa','Wi-fi de alta velocidad','Lavadora'],
 around_s='Frente al Parque de Castelar, a 5 minutos a pie del casco histórico y la Alcazaba y a 15 minutos en coche de la frontera con Portugal.',
 loc_p='C/ Juan Antonio Cansinos Rioboo 3 · 06002 Badajoz (Edificio Presidente). Check-in desde las 16:00 y check-out hasta las 12:00.',
 chips=['¿Qué suites tenéis?','¿A qué hora es el check-in?','¿Hay parking?','¿Cómo reservo?']),
'en':dict(title='Castelar Urban Suites · Apartments facing Parque de Castelar, Badajoz',see_rooms='See the suites',hero_k='Badajoz · Edificio Presidente',hero_t='Design and comfort facing Parque de Castelar',hero_s='10 apartments of 3 types in the historic Edificio Presidente, in the heart of Badajoz.',
 intro_t='Where elegance meets comfort',intro_p1='Contemporary design, natural materials, careful lighting and smart spaces, facing Parque de Castelar and a 5-minute walk from the old town.',
 intro_p2='Self check-in with a smart lock at any time, a virtual host on WhatsApp throughout your stay and bicycles on request.',
 stats=['10 apartments','3 suite types','Self check-in','24 h virtual host'],nav_rooms='Suites',rooms_t='Our suites',rooms_s='All with full kitchen, 150 cm bed, separate bathroom, living-dining room, Wi-fi, TV and desk.',
 svcs=['Self check-in','24 h virtual host','Bicycles on request','Full kitchen','High-speed Wi-fi','Washing machine'],
 around_s='Facing Parque de Castelar, a 5-minute walk from the old town and the Alcazaba and 15 minutes by car from the Portuguese border.',
 loc_p='C/ Juan Antonio Cansinos Rioboo 3 · 06002 Badajoz (Edificio Presidente). Check-in from 16:00 and check-out until 12:00.',
 chips=['Which suites do you have?','What time is check-in?','Is there parking?','How do I book?']),
'fr':dict(title='Castelar Urban Suites · Appartements face au Parque de Castelar, Badajoz',see_rooms='Voir les suites',hero_k='Badajoz · Edificio Presidente',hero_t='Design et confort face au Parque de Castelar',hero_s='10 appartements de 3 types dans l’historique Edificio Presidente, au cœur de Badajoz.',
 intro_t='Là où l’élégance rencontre le confort',intro_p1='Design contemporain, matériaux naturels, lumière soignée et espaces intelligents, face au Parque de Castelar et à 5 minutes à pied du centre historique.',
 intro_p2='Check-in autonome avec serrure connectée à toute heure, hôte virtuel sur WhatsApp pendant tout le séjour et vélos sur demande.',
 stats=['10 appartements','3 types de suite','Check-in autonome','Hôte virtuel 24 h'],nav_rooms='Suites',rooms_t='Nos suites',rooms_s='Toutes avec cuisine complète, lit de 150 cm, salle de bain indépendante, salon-salle à manger, Wi-fi, TV et bureau.',
 svcs=['Check-in autonome','Hôte virtuel 24 h','Vélos sur demande','Cuisine complète','Wi-fi haut débit','Lave-linge'],
 around_s='Face au Parque de Castelar, à 5 minutes à pied du centre historique et de l’Alcazaba et à 15 minutes en voiture de la frontière portugaise.',
 loc_p='C/ Juan Antonio Cansinos Rioboo 3 · 06002 Badajoz (Edificio Presidente). Arrivée à partir de 16:00 et départ jusqu’à 12:00.',
 chips=['Quelles suites avez-vous ?','À quelle heure est le check-in ?','Y a-t-il un parking ?','Comment réserver ?']),
'de':dict(title='Castelar Urban Suites · Apartments am Parque de Castelar, Badajoz',see_rooms='Suiten ansehen',hero_k='Badajoz · Edificio Presidente',hero_t='Design und Komfort am Parque de Castelar',hero_s='10 Apartments in 3 Kategorien im historischen Edificio Presidente, im Herzen von Badajoz.',
 intro_t='Wo Eleganz auf Komfort trifft',intro_p1='Zeitgemäßes Design, natürliche Materialien, durchdachtes Licht und clevere Räume, gegenüber dem Parque de Castelar und 5 Gehminuten von der Altstadt.',
 intro_p2='Self-Check-in mit Smart Lock zu jeder Uhrzeit, virtueller Gastgeber per WhatsApp während des ganzen Aufenthalts und Fahrräder auf Anfrage.',
 stats=['10 Apartments','3 Suitetypen','Self-Check-in','Virtueller Gastgeber 24 h'],nav_rooms='Suiten',rooms_t='Unsere Suiten',rooms_s='Alle mit voll ausgestatteter Küche, 150-cm-Bett, eigenem Bad, Wohn-Essbereich, WLAN, TV und Schreibtisch.',
 svcs=['Self-Check-in','Virtueller Gastgeber 24 h','Fahrräder auf Anfrage','Voll ausgestattete Küche','Schnelles WLAN','Waschmaschine'],
 around_s='Gegenüber dem Parque de Castelar, 5 Gehminuten von Altstadt und Alcazaba und 15 Autominuten von der portugiesischen Grenze.',
 loc_p='C/ Juan Antonio Cansinos Rioboo 3 · 06002 Badajoz (Edificio Presidente). Check-in ab 16:00 Uhr, Check-out bis 12:00 Uhr.',
 chips=['Welche Suiten gibt es?','Wann ist der Check-in?','Gibt es einen Parkplatz?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://bookonline.pro/es/properties/101494?unidades=1'
BOOK=dict(mode='engine',url={l:'https://bookonline.pro/'+l+'/properties/101494?unidades=1' for l in ('es','en','fr','de')})
D=dict(name='Castelar Urban Suites',ac='#20302a',ac2='#5a3b2b',ac2_a11y='#3a261b',book=BOOK,around=['Parque de Castelar','Alcazaba de Badajoz'],foot=FOOT,
 address='C/ Juan Antonio Cansinos Rioboo 3 · 06002 Badajoz',phones=['+34 633 383 093'],emails=['reservas@castelarurbansuites.com'],maps='Castelar Urban Suites, Edificio Presidente, C/ Juan Antonio Cansinos Rioboo 3, 06002 Badajoz',t=T)
META=dict(repo='demo-castelar-urban-suites-badajoz',name='Castelar Urban Suites',legal_name='Ibérica de Distribución y Operadores Extremeños, S.L.',registry_ids=['B37290038','AT-BA-00427'],
 url='https://castelarurbansuites.com/',domain='castelarurbansuites.com',municipality='Badajoz',province='Badajoz',sector='10 apartamentos turísticos de 3 tipos en el Edificio Presidente de Badajoz',
 read_at='2026-10-30T08:59:00+01:00',created_at='2026-10-30T08:58:00+01:00',built_at='2026-10-30T09:15:00+01:00',audit_date='2026-10-30T08:46:20+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T16:35:47+01:00',url='https://www.google.com/maps/place/Apartamentos+Castelar+Urban+Suites/@38.8774051,-6.9767023,17z/data=!3m1!4b1!4m6!3m5!1s0xd16e50d3dcac657:0xb411f568fba85a7a!8m2!3d38.8774051!4d-6.9767023!16s%2Fg%2F11ywgnw59d'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (bookonline.pro, propiedad 101494, enlace «Reservar» de castelarurbansuites.com), HTTP 200 comprobado el 30/10/2026 en es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué suites tenéis?','K01'),('¿Qué equipamiento tienen?','K02'),('¿A qué hora es el check-in?','K03'),('¿Puedo llegar antes?','K04'),('¿Hay parking?','K05'),('¿Admitís mascotas?','K06'),('¿Alquiláis bicicletas?','K07'),('¿Dónde estáis?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuál es la política de cancelación?','K10'),('¿Se puede fumar?','K11'),('¿Hay servicio de limpieza?','K12'),('¿Cómo contacto con el anfitrión virtual?','K13'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which suites do you have?','K01'),('What equipment do they have?','K02'),('What time is check-in?','K03'),('Can I arrive early?','K04'),('Is there parking?','K05'),('Do you accept pets?','K06'),('Do you rent bicycles?','K07'),('Where are you?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('What is the cancellation policy?','K10'),('Can I smoke?','K11'),('Is there a cleaning service?','K12'),('How do I contact the virtual host?','K13'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quelles suites avez-vous ?','K01'),('Quel est leur équipement ?','K02'),('À quelle heure est le check-in ?','K03'),('Puis-je arriver plus tôt ?','K04'),('Y a-t-il un parking ?','K05'),('Acceptez-vous les animaux ?','K06'),('Louez-vous des vélos ?','K07'),('Où êtes-vous situés ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),("Quelle est la politique d'annulation ?",'K10'),('Peut-on fumer ?','K11'),('Y a-t-il un service de ménage ?','K12'),("Comment contacter l'hôte virtuel ?",'K13'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Suiten gibt es?','K01'),('Welche Ausstattung gibt es?','K02'),('Wann ist der Check-in?','K03'),('Kann ich früher anreisen?','K04'),('Gibt es einen Parkplatz?','K05'),('Sind Haustiere erlaubt?','K06'),('Kann man Fahrräder mieten?','K07'),('Wo liegen die Suiten?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Wie sind die Stornobedingungen?','K10'),('Darf man rauchen?','K11'),('Gibt es einen Reinigungsservice?','K12'),('Wie erreiche ich den virtuellen Gastgeber?','K13'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
