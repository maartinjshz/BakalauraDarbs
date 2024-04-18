# BakalauraDarbs
 Šeit tiek apkopoti kodi, kuri tika lietoti Bakalaura darba ietvaros. Kods tiek sadalīts divās daļās, viena atbilst maxmin risināšanai bez ierobežojumiem. Otra MOLP prolbēmu risināšanai. 


 ### Maxmin problēmu risināšan

 ### MOLP problēmu risināšana. 

Failā main.py ir piemērs, kā tiek izsauktas visas no darbā aprakstītajām risināšanas metodēm. 

Virpirms tiek definēts pats uzdevums. Pašlaik ir iespējams risināt tikai lineārās programmēšanas uzdevumus, kuriem ierobežojumi mainīgajiem ir formā $x_{i} \geq 0$. 

Lai definētu uzdevumu, tiek definēta matrica C, kas atbilst mērķa funkciju koeficientiem, matrica A un vektors b nosacījumiem. Šīs matricas tiek padotas funkcijai MolpProblem no MakeMolp.py . Pēc tam šo objektu var padod izvēlētajai metodei un tiks atgriezta vērtība, kas atbilst pareto optimālam atrisinājumam. 



