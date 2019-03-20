
d = {'Izvoli': {
    'izvoli': 'Izvoli?'},
     'FOI': {
         'foi': 'Faklutet organizacije i informatike jedna je od sastavnica Sveučilišta u Zagrebu. FOI je visokoobrazovna ustanova u interdisciplinarnom području informatike, organizacije i poslovanja. Studijski programi utemeljeni su na modernim svjetskim modelima, načelima Bolonjske deklaracije i ECTS bodovnom sustavu.'},
     'Dvorana': {
         'dvorana': 'Koja dvorana?'},
     'Profesor': {
         'profesor': 'Koji profesor?'},
     'Raspored': {
         'raspored': 'Za koji vrstu studija trebaš raspored?'},
    'Classrooms': {
    'd9': 'Dvorana devet se nalazi u podrumu, u istočnom krilu zgrade',
    'info': 'Info Klub kafić se nalazi u podrumu, u istočnom krilu zgrade',
    'knjiznica': 'Knjižnica se nalazi u podrumu, u južnom krilu zgrade',
    'd10': 'Dvorana deset se nalazi u prizemlju, u istočnom krilu zgrade',
    'referada': 'Referada se nalazi u prizemlju, u istočnom krilu zgrade',
    'lab5': 'Laboratorij pet se nalazi u prizemlju, u istočnom krilu zgrade',
    'skriptarnica': 'Skriptarnica se nalazi u prizemlju, u istočnom krilu zgrade',
    'foto': 'Fotokopiraona se nalazi u prizemlju, kod samog  ulaza u zgradu',
    'd6': 'Dvorana šest se nalazi u prizemlju, u južnom krilu zgrade',
    'd7': 'Dvorana sedam se nalazi u prizemlju, u južnom krilu zgrade',
    'lab12': 'Laboratorij dvanaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab13': 'Laboratorij trinaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab14': 'Laboratorij četrnaest se nalazi u prizemlju, u južnom krilu zgrade',
    'lab15': 'Laboratorij petnaest se nalazi u prizemlju, u južnom krilu zgrade',
    'dekanat': 'Dekanat se nalazi na prvom katu, na kraju istočnog krila zgrade',
    'CPSRK': 'Centar za podršku studentima i razvoj karijera se nalazi na prvom katu, u istočnom krilu zgrade',
    'racunovodstvo': 'Računovodstvo se nalazi na prvom katu, u istočnom krilu zgrade',
    'd4': 'Dvorana četiri se nalazi na prvom katu, između južnog i istočnog krila, u kutu',
    'd11': 'Dvorana jedanaest se nalazi na prvom katu, u južnom krilu zgrade',
    'd1': 'Dvorana jedan se nalazi na drugom katu, na kraju istočnog krila zgrade',
    'd2': 'Dvorana dva se nalazi na drugom katu, u istočnom krilu zgrade',
    'd8': 'Dvorana osam se nalazi na drugom katu, između južnog i istočnog krila, u kutu',
    'd3': 'Dvorana tri se nalazi na drugom katu, u južnom krilu zgrade'}}

from ScrapProfesssors import *
professors = scrapProfessors()

prof = {}
for name, user_name in professors.items():
        prof[user_name] = 'Izvoli podatke za ' + name

d['Professors'] = prof
        
def dictionary():
        return d

