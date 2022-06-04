#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv, char **envp) {
  char *buffer;

  gid_t gid;
  uid_t uid;
  const char invalid_chars[] = "!\"$&'()*,:;<=>?@[\\]^`{|}";

  gid = getegid();
  uid = geteuid();

  setresgid(gid, gid, gid);
  setresuid(uid, uid, uid);
  buffer = NULL;

  asprintf(&buffer, "/bin/echo %s is cool", getenv("USER"));
  if ((strpbrk(buffer, invalid_chars)) != NULL) {
    perror("strpbrk");
    exit(EXIT_FAILURE);
  }
  printf("about to call system(\"%s\")\n", buffer);

  system(buffer);
}