#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// TODO: need some data structure to hold tasks
// - some dynamic array
// Need some loop to take in input from stdin
// Need to write tasks to a txt file or csv
// 1. Define the Task struct and hardcode a few tasks to print
// 2. Add argv parsing to handle add, list, done, delete
// 3. Save/load tasks from a file
// 4. Polish the output with some ASCII formatting

struct Task {
	int taskNum;
	int status;
	char taskDesc[75];
};

int writeToFile(struct Task* t) {
	FILE *fptr;
	fptr = fopen("tasks.txt", "a");

	if (fptr != NULL) {
		fputs(t->taskDesc, fptr);
		fputc('\n', fptr);
        	fclose(fptr);
	}

	return 0;
}

int readFile(struct Task* arr) {
	FILE *fptr;
	fptr = fopen("tasks.txt", "r");
	int pos = 0;

	struct Task t = {0, 0};
	printf("Reading file...\n");
	if (fptr != NULL) {
		while (fgets(t.taskDesc, 75, fptr)) {
			arr[pos] = t;
			pos = pos+1;
			struct Task t = {0, 0};
		}
        	fclose(fptr);
		return pos;
	} else {
		printf("Failed to open tasks file");
		return 0;
	}
}

int deleteTask () {
	return 0;
}

int main(int argc, char *argv[]) {
	// arr is a ptr to a Task
	// im making space for 5 Tasks with malloc
	struct Task* arr = malloc(10 * sizeof(struct Task));
	int pos = 0;
	int taskCount = readFile(arr);

	if (argc > 1) {
		if (strcmp(argv[1], "add") == 0 && argc == 3) {
			// TODO: need to get the last written task num in list to auto add new one
			// idk if we even need this we can just display them in order
			// status should always be 0
			struct Task t = {0, 0};
			strncpy(t.taskDesc, argv[2], sizeof(t.taskDesc)-1);
			t.taskDesc[sizeof(t.taskDesc) - 1] = '\0';

			writeToFile(&t);
			printf("Task num %d %d %s written to file\n", t.taskNum, t.status, t.taskDesc);
		}
		else if (strcmp(argv[1], "list") == 0) {
			for (int i=0; i<taskCount; i++) {
				printf("Task num %d %d %s", arr[i].taskNum, arr[i].status, arr[i].taskDesc);
			}
		}
		else if (strcmp(argv[1], "delete") == 0) {
			deleteTask();
		}
	}

	free(arr);
}
