#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  srand(time(0));
  printf("%d\n", RAND_MAX);
  printf("%d\n", rand() % 1000000);
}
