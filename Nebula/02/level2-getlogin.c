#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv, char **envp) {
  char *buffer;

  gid_t gid;
  uid_t uid;

  gid = getegid();
  uid = geteuid();

  setresgid(gid, gid, gid);
  setresuid(uid, uid, uid);
  // using getlogin to get username
  char *username;
  username = getlogin();
  buffer = NULL;

  asprintf(&buffer, "/bin/echo %s is cool", username);
  printf("about to call system(\"%s\")\n", buffer);

  system(buffer);
}