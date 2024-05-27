# DLP risināšana lietojot nestriktās attiečibas


## T-normas. 


   Par t-normu T intervālā [0,1] sauc attēlojumu: $T: [0,1]^{2} \to [0,1]$, kas katram $x,y,z \in [0,1]$ apmierina:


* $T(x,y)=T(y,x)$ (simetrijas nosacījums);
* $T(x,T(y,z))=T(T(x,y),z)$ (asociativitāte);
* $T(x,y)\leq T(x,z)$,  kad $y\leq z$ (monotonitāte);
* T(x,1)=x (robežnosacījums). 

Piemēram:
* $T_{M}(x,y) = \min(x,y)$ minimuma t-norma;
* $T_{P}(x,y) = x\cdot y$ reizinājuma t-norma;
* $T_{L}(x,y) = \max(x+y-1,0)$ Lukasēviča t-norma.


Ar šo pieeju katrai mērķa funkcijai tiek izveidota piederības funkcija:
$$\mu_{i}(x) = \frac{z_{i}(x) - z^{min}_{i}}{z^{max}_{i} - z^{min}_{i} },$$

kur $x \in D$, $z^{min}_{i} = \min\limits_{x\in D}{z_{i}(x)}$ un $z^{max}_{i} =  \max\limits_{x\in D}{ z_{i}(x )}$.

un tālāk agregē piederības funkcijas, lietojot t-normas, sākotnējo DLP problēmu pārrasktot kā:     
$$\max\limits_{x\in D} T(\mu_{1}(x),\ldots, \ \mu_{l}(x)).$$





## Nestriktās ekvivalences

Funkciju $d:X \times X \to \mathbb{R^{+}}$ sauc par metriku, ja visiem $x,y,z \in X$ izpildās:


* $x=y \iff d(x,y) =0$;
* $d(x,y) = d(y,x)$;
* $d(x,z)\leq d(x,y) + d(y,z)$.

Par nestrikto ekvivalenci ($T$-ekvivalenci) sauc attiecību   $E:X\times X \to [0,1]$, kur katram $x,y,z \in X$ izpildās: 

*  $E(x,x) = 1$ (refleksivitāte);
*  $E(x,y) = E(y,x)$ (simetrija);
* $T(E(x,y),E(y,z)) \leq E(x,z)$ (T-transitivitāte).

Piemēram:

* $E_{L}(x,y) = \max(1- d(x,y),0)$  (lietojot Lukasieviča t-normas aditīvo ģeneratoru);
* $E_{P}(x,y) = e^{-d(x,y)}$ (lietojot reizinājuma t-normas aditīvo ģeneratoru);
* $E_{H}(x,y)  = \frac{1}{1+d(x,y)}$ (lietojot Hamahera t-normas aditīvo ģeneratoru un $\lambda =0$).

Ar šo pieeju tiek agregētas nestriktās ekvivalences tā, lai:

$$\max\limits_{y\in D} A(  E_{1}(x^{max}_{1},y), \ldots,\ E_{l}(x^{max}_{l},y)  ).$$

funkcija $A$ arī būtu nestriktā ekvivalence. Šeit $x_{i}^{max}$ ir ppunkts, kurā i-tā mērķa funkcija sasniedz savu maksimumu. 


## Nestrikties sakārtojumi


 Nestrikto attiecību $L: X \times X \to [0,1]$  sauc par nestrikto sakārtojuma attiecību ($T$-$E$-sakārtojums) attiecīgajai  t-normai $T$ un $T$-ekvivalencei  $E$  tad un tikai tad, ja katram $x,y,z \in X$ izpildās:

* $L(x,y) \geq E(x,y)$  (E-refleksivitāte);
* $T(L(x,y),L(y,z)) \leq L(x,z)$ (T-transitivitāte);
* $T(L(x,y),L(y,x)) \leq E(x,y)$ (T-E-antisimetrija).

Piemēram: 

$$
L(x,y)=    \begin{cases} 
1&  \text{ ja } x \preceq y  \\
E(x,y)  & \text{ citādi} . 
\end{cases}$$


Ar šo pieeju, katrai mērķa funkcijai tiek definēts sakārtojums un šie sakārtojumi tiek agregēti: 

   $$P(x,y) = A(P_{1}(x,y), \ldots, \ P_{l}(x,y))$$

lai funkcija P(x,y) arī būtu nestriktais sakārtojums. Tad DLP problēmu var uzrakstīt kā maxmin problēmu: 

$$\max_{y\in D} \min_{x\in D} P(x,y).$$

## DLP risināšana

Katrai no pieejam ir izveidota atsevišķa funkcija. Failā main.py ir parādīts, kā izsaukt katru no funkcijām. Vispirms tiek definēta pati DLP prolēmu, kuras definēšanai ir nepieciešams nosacījumu vektors $b$, matrica $A$ un mērķa funkciju koeficienti. Pēc tam šie parametri tiek padoti funkcijai failā MakeMOlp.py, kas atrod katrai mērķa funkcijai lokālos ektrēmus. Gan minimuma punktus, kas maksimuma. Pēc tam tiek noteiktas kopas D virsotnes. (Vajadzīgs sakārtojumu algoritmam).

Pēc tam var izsaukt katru metodi un iegūt atrisinājumu $x$. Risinot ar t-normām, ir iespējams izvēlēties, ar kuru t-normu agregēt mērķa funkcijas. Dažādas t-normas var dot dažādus atrisinājumus. Pašlaik, neatkarīgi no t-normas izvēles, liet lietots Nelder-Mead algoritms.

Risinot ar nestriktajām ekvivalencēm, problēma tiek pārrakstīta kā LP problēma un atrisināta ar simpleksa metodi.

Risinot ar nestriktajiem sakārtojumiem, tiek lietots algoritms, kas ir aprakstīts pie maxmin problēmu risināšanas sadaļas un apvienots ar gradienta projekcijas algoritmu.

Iekš main.py ir definēts piemērs ar 6 mērķa funkcijām. Šo piemēru risinot ar pilnu pārlasi ir jāuzmanās, jo tas var aizņemt pārāk daudz laika. Tāpēc ir ieteicams atrisināt šo piemēru ar kādu no iepriekš minētajām metodēm un pēc tam šo atrisinājumu padot, kā sākuma punktu pilnajai pārlasei.

