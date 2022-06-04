#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char **argv, char **envp) {
  gid_t gid;
  uid_t uid;
  gid = getegid();
  uid = geteuid();
  setresgid(gid, gid, gid);
  setresuid(uid, uid, uid);
  putenv("PATH=/bin:/sbin:/usr/bin:usr/sbin"); // set correct PATH before run echo.
  system("/usr/bin/env echo and now what?");
}