# Bakalaura Darbs

## Bakalaura darba Anotācija

Šajā darbā tiek aplūkotas dažādas nestriktās attiecības un šo nestrikto attiecību lietojums daudzkriteriālā lineārās programmēšanas uzdevumu risināšanā. Tiek doti kritēriji, kādos risinot maxmin problēmu tiek iegūts atrisinājums sākotnējai daudzkriteriālai lineārās programmēšanas problēmai. Tiek parādīts, kā lietojot nestriktos sakārtojumus,  nestriktās attiecība konstrukcija nav atkarīga no izvēlētās $T$  -normas. Līdzīgs rezultāts tiek pierādīts nestriktajām ekvivalencēm, kas papildus reducē problēmu uz klasisko lineārās programmēšanas problēmu.  Tāpēc beigās tiek aplūkota skaitliskā optimizācija, ja risina daudzkriteriālās lineārās programmēšanas problēmas ar nestriktajiem sakārtojumiem.

Šajā reposotorijā tiek apkopoti kodi, kas tika lietoti risinot darbā minētāsa optimizācijas problēmas. Programmas kodi ir sadalīti divās daļās, daudzkriteriālās lineārās programmēšanas (DLP) problēmu risināšanai un maxmin prolbēmu risināšanai.

### Šajā darbā tika aplūkotas optimizācijas problēmas


Šajā darbā tika apskatītas maxmin problēmas, kur minimums tiek ņemts no lineārām funkcijām: 

$$    \max\limits_{x}  \min \{  a_{1} \cdot x + b_{1}, \ldots , a_{l}\cdot  x + b_{l} ,\} ,$$

kur $x, a_{i} \in \mathbb{R}^m$,  $i=1,...,n$ un $b \in \mathbb{R}^l$ .


###  DLP problēmas

DLP prolbēma vispārīgā gadījumā: 

$$
\begin{equation*} 
    \begin{array}{lll}
    \text{Maksimizēt} 
    & c_{1 1}x_{1}+c_{1 2}x_{2}+ \ldots c_{1m}x_{m} \\
    & \ldots \\
    &c_{l 1}x_{1}+c_{l 2}x_{2}+ \ldots c_{ l m}x_{m} \\
    \text{Pie}\\
    & a_{11}x_{1} + a_{12}x_{2} + \ldots a_{1m}x_{m} \leq b_{1}  \\
    & a_{21}x_{1} + a_{22}x_{2} + \ldots a_{2m}x_{m} \leq b_{2}  \\
    & \ldots \\

    & a_{n1}x_{1} + a_{n2}x_{2} + \ldots a_{nm}x_{m} \leq b_{n}  \\
    & x_i \geq 0 \ i=1,\ldots, \ m,
    \end{array}
\end{equation*}
$$


Šajā darbā tiek aplūkota šādu problēmu risināšana, lietojot nestriktās attiecības, kā t-normas, nestriktās ekvivalences attiecības un nestrikto sakārtojuma attiecību. 