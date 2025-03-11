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
