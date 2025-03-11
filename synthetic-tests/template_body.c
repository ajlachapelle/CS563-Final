#ifndef N
#define N 32
#endif

#ifndef FT
#define FT double
#endif

// Summation macros for sum (used with metrinome) and injected sum (used with fpgen)
// Macros are used instead of functions so that Metrinome can analyze them
#define sum {for (i = N-1 ; i > 0 ; i--){\
                L[i-1] += L[i];}}

#define injected_sum {for (i = N-1 ; i > 0 ; i--)\
                        {tmp = L[i-1] + L[i];\
                        fp_injection((void *)(L+i-1), (void *)(L+i), (void *)&tmp);\
                        L[i-1] = tmp;}}

int main (int argc, char *argv[]) { 
    assert(N >= 2);
    float input[N];   
    klee_make_symbolic(&input, sizeof(input), "input");

    FT L[N];
    int i;

    // read input
    for (i = N-1 ; i >= 0; i--){
        L[i] = input[i] / FLT_MAX * 100;
    }

    // The synthesis script will replace the FLAG line with a summation variation:
    // FLAG

    return 0;
}
