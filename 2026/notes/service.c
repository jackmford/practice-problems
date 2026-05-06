#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define LOG_ENTRIES 1000000

void write_logs(const char *filename) {
    FILE *f = fopen(filename, "w");
    char *buffer = malloc(1024);
    
    for (int i = 0; i < LOG_ENTRIES; i++) {
        sprintf(buffer, "Entry %d: something happened at timestamp %d\n", i, i * 100);
        fputs(buffer, f);
    }
    // buffer never freed
}

int spawn_worker() {
    pid_t pid = fork();
    
    if (pid == 0) {
        // child: do some work and exit
        sleep(2);
        exit(0);
    }
    // parent never calls wait()
    return pid;
}

int main() {
    printf("Starting service...\n");
    
    write_logs("/tmp/service.log");
    
    for (int i = 0; i < 5; i++) {
        spawn_worker();
    }
    
    // "stay alive" to simulate a running service
    printf("Workers spawned. Sleeping...\n");
    sleep(30);
    
    fclose(NULL);  // intentional crash
    return 0;
}
