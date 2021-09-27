#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void secret() {
  system("uname -a");
  printf("%s", "You accessed the secret function. Congratulations!\n");
}

void public() {
  printf("%s", "Accessing a public function!\n");

  char buff[8];
  gets(buff);
  printf("Hello, %s\n", buff);
}

int main() {
  printf("%s\n", "A vulnerable program, via https://youtu.be/McgoyVnKhTw");
  printf("%s\n", "Please enter your name:");

  // In the original program at https://youtu.be/McgoyVnKhTw, a buffer
  // is created, filled with gets(), and then used in a printf() call.
  // But this doesn't allow an overflow in my test on a Raspberry Pi 4
  // running 64-bit Ubuntu. As far as I can tell, the trouble is that if
  // I don't call a subfunction from inside main(), then
  // then the return address that's on register x30 on entering main can
  // just stay there; it never needs to be saved to the stack.
  //
  // To work around this, instead I move the vulnerable lines into a function
  // called public(). Before calling public(), the return address initially in
  // x30 (basically, some libc exit function) must get saved to the stack,
  // because x30 will need to be updated with the return address to get back
  // to main() after public() is called. Since this return address is on
  // the stack, it is vulnerable to being overwritten by a buffer overflow.
  public();

  return 0;
}
