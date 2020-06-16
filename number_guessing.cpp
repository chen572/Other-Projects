#include <iostream>
//#include "number_guessing_functions.hpp"
#include <stdlib.h>
#include <time.h>

int main()  {

    /* random seed each time */
    srand(time(NULL));

    /* the random number */
    int num = rand() % 100 + 1;

    std::string user_guess;
    
    std::cout << "The computer chose a number between 1 - 100\nTry to guess it: ";
    std::cin >> user_guess;


}