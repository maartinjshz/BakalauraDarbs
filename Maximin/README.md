# Maxmin pproblēmu skaitliska risināšana


## Līdzības attiecība


   Par līdzības atiecību sauc attiecību $S:\mathbb{R}\times \mathbb{R} \to \mathbb{R}^{+}$, kur katram $x, \ y, \ z \in \mathbb{R}$ izpildās:

* $S(x,x) = 1$ (refleksivitāte);
* $S(x,y) = S(y,x)$ (simetrija);
* $x\preceq y\preceq z\Rightarrow$ $S(x,z)\leq S(y,z)\; \text{ un }\; S(x,z)\leq S(x,y)$ (monotonitāte).

Piemēram: 

* $S_{L}^{p}(x,y) = \max(1- d(x,y)^{p},0)$ ;
* $S_{P}^{p}(x,y) = e^{-d(x,y)^{p}}$  ;
* $S_{H}^{p}(x,y)  = \frac{1} 
 {1+d(x,y)^{p}}$ ,

kur $p \in (0, + \infty)$. 

## Maxmin problēmu risiāšana


$$\max\limits_{x} F(x) \text{ kur } F(x) =  \min \{ f1 , f2 , f3, f4, f5 \},$$

kur 
* $f_{1} = 0.49x_{1} + 0.12x_{2} + 7.93$ ;
* $f_{2} =  0.3x_{1} - 0.08x_{2} + 8.26$;
* $f_{3} =0.39x_{1} + 0.33x_{2} + 8.34$;
* $f_{4} = -0.3x_{1} + 0.016x_{2} + 8.448$;
* $f_{5} =  -0.191x_{1} - 0.192x_{2} + 8.469$.

Problēmas tiek risinātas skaitlsiki:

$$x_{k+1} = x_{k} + \alpha_{k} d_{k},$$

kur soļa garums $\alpha_{k}$ tiek atrast, lietojot Backtracking Line Search algoritmu. Virziena $d_{k}$ atrašana:


* $ \text{ Sakārto augošā secībā } : f_{i_{1}}(x_{k}) <  \ldots < f_{i_{l}}( x_{k})$ 
* $v_{1} = 1$
* $v_{2} = S(f_{i_{1}}(x_{k}),f_{i_{2}}(x_{k}))$
* $d_{k} = \big( v_{1} \nabla f_{i_{1}} / \| \nabla f_{i_{1}}\| + v_{2} \nabla f_{i_{2}}/\| \nabla f_{i_{2}}\|  \big) / \big(v_{1} + v_{2} \big)$

Pašlaik iterācijas tiek veiktas, līdz tiek iegūts $\alpha_{k} \leq \varepsilon$.
