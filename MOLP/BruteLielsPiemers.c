#include <stdio.h>
#include <stdbool.h>
#define NUM_ELEMENTS 6 // Define the number of elements in the arrays
// SKalārais reizinājums
float DotProd(float *x, float *y, int NrCol) {
    float sum = 0;
    for (int i = 0; i < NrCol; i++) {
        sum = sum + x[i] * y[i];
    }
    return sum;
}

float NestriktaisSakartojums(float *c, float *x, float *y,int NrCol, int row ){

    float z_norma[5] = {1.3333333333333333, 1.1666666666666665, 1.4333333333333331, 1.2666666666666666, 2.2666666666666666};

    float z_x = DotProd(c,x,NrCol);
    float z_y = DotProd(c,y,NrCol);

    if (z_x < z_y){
        return 1;
    }
    else{
        return 1 - (z_x-z_y)/z_norma[row];
    }
}

float AgregacijasOperators(float *x, float *y, int NrCol){

    float C_ub[5][6] = {
        {2, 3, 1, 0, 0, -1}, 
        {1, 2, 1, -2, 0, 0},   
        {0, 1, 3, 0, 0, 4},   
        {3, 0, 1, 4, 1, 0},    
        {-1, 0, 0, 2, 3, 0}  
    };
    float N = 5;
    float sum = 0;

    for (int i =0 ; i < 5 ; i++){
            sum = sum  + NestriktaisSakartojums(C_ub[i],x,y,NrCol,i) /5 ;
        }

    return sum;

}

float Funkcija_P_X_Y(float *y){ 

    // Šeit vajag definēt vektours A un b
    float A_ub[9][6] = {
        {2, 3, 2, 4, 1, 3},            // Coefficients for x1
        {1, 2, 4, 0, 0, 0},            // Coefficients for x2
        {3, 1, 2, 0, 0, 0},            // Coefficients for x3
        {4, 2, 3, 5, 3, 4},            // Coefficients for x4
        {0.2, 0.4, 0.3, 0.5, 0.6, 0.4},// Coefficients for waste constraint
        {2, 3, -1, 2, 1, -1},          // Coefficients for product quality constraint
        {4, 2, 3, 0, 0, 0},            // Coefficients for energy consumption
        {2, 3, 2, 0, 0, 0},            // Additional material constraint
        {1, 1, 1, 1, 1, 1}             // Total production limit
    };

    float b_ub[9] = {1, 1.2, 0.8, 3.5, 0.4, 1, 2, 3, 2};
    float X[11][6] =  {
        {0.0, 0.33333333, 0.0, 0.0, 0.0, 0.0},
        {0.0, 0.0, 0.3, 0.0, 0.0, 0.13333333},
        {0.26666667, 0.0, 0.0, 0.11666667, 0.0, 0.0},
        {0.0, 0.0, 0.0, 0.0, 0.66666667, 0.0},
        {0.0, 0.0, 0.3, 0.0, 0.4, 0.0},
        {0.26666667, 0.0, 0.0, 0.0, 0.46666667, 0.0},
        {0.08, 0.14, 0.21, 0.0, 0.0, 0.0},
        {0.0, 0.2, 0.2, 0.0, 0.0, 0.0},
        {0.2, 0.2, 0.0, 0.0, 0.0, 0.0},
        {0.2, 0.0, 0.0, 0.0, 0.6, 0.0},
        {0.0, 0.0, 0.22222222, 0.0, 0.55555556, 0.0}
    };


// Pārbauda robežas
    for (int i = 0; i < 9; i++) {
       
         //  printf("summa ir %.10f", a);
          // printf("\n");
        if (DotProd(A_ub[i],y,NUM_ELEMENTS) - b_ub[i] > 0) {

            return 0;
        }
    }

    float min_val = 2;

    for (int i = 0; i < 11; i++) {

        float  funval = AgregacijasOperators(X[i], y,  NUM_ELEMENTS) ;
        if (funval < min_val){
            min_val = funval;
        }
    }
    return min_val;
}


void iterizraksts(float *x_lower, float *x_upper, float *X,float h){

        printf("solis h saja iteracija: %.12f ", h,"\n");
        printf("\n");

        printf("apakseja robeza ir (" );

        for (int i = 0; i < NUM_ELEMENTS; i++){
                printf("%.12f", x_lower[i]);}

        printf(" ), un augseja robeza: ");
        for (int i = 0; i < NUM_ELEMENTS; i++){
                printf("%.12f", x_upper[i]);}
        
        printf("\n un saja iteracija x_max ir: (");
        for (int i = 0; i < NUM_ELEMENTS; i++){
                printf("%.12f", X[i]);}
        printf(" ) un f_max ir: %.12f", Funkcija_P_X_Y(X));
        printf("\n");
        printf("\n");

    return 0;
}
 
// Driver code
int main(){
    bool end = true;
    float X[6] = { 0.14149796960,.02254459820,.17647778990,.00000000000,.29641473290,.0000000000 };
    float funMax = Funkcija_P_X_Y(X);
    float h = 0.0000001;

    while (end) {
       
        float x_lower[NUM_ELEMENTS]; // Declare x_lower with size NUM_ELEMENTS
        float x_upper[NUM_ELEMENTS]; // Declare x_upper with size NUM_ELEMENTS

        for (int i=0; i < NUM_ELEMENTS ; i++){
            x_lower[i] = X[i] - h;

            if (x_lower[i] < 0){
                x_lower[i] = 0;
            }
            x_upper[i] = X[i] + h;
        }
        bool innerEnd = true;
        iterizraksts(x_lower, x_upper, X,h);
        float x_h[NUM_ELEMENTS] = {0};

        while(innerEnd){

            if (x_h[0] + x_lower[0] >= x_upper[0]){ innerEnd = false;}
            else{

                for (int i= NUM_ELEMENTS-1; i > 0 ; i--){
                    if(x_h[i] + x_lower[i] >= x_upper[i]){
                        x_h[i-1] += 2*h/50 ; 
                        x_h[i] = 0;
                    }
                    else if(i == NUM_ELEMENTS -1){
                        x_h[i] += 2*h/50;
                    }

                    float EvalX[NUM_ELEMENTS];

                    for (int i=0; i< NUM_ELEMENTS ; i++){
                        EvalX[i] = x_lower[i] + x_h[i];
                    }
                    float funval = Funkcija_P_X_Y( EvalX );

                    if( funval > funMax){
                        funMax = funval;

                        for (int i=0 ; i < NUM_ELEMENTS ; i++){
                            X[i] = EvalX[i];
                        }
                    }
                }
            }
        }
        h = h/10;

        if( h <= 1e-14){ end = false;}
        
    }

    
    printf("\n");
    printf("Atrastais x_max ir: (");
    for (int i = 0; i < NUM_ELEMENTS; i++){
            printf("%.10f", X[i]);}
    printf(" ) un f_max ir: %.10f", Funkcija_P_X_Y(X));
    return 0;
}