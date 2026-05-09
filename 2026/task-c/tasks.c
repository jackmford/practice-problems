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

int readFile() {
	FILE *fptr;
	fptr = fopen("tasks.txt", "r");

	struct Task t = {0, 0};

	printf("Reading file...\n");

	if (fptr != NULL) {
		while (fgets(t.taskDesc, 75, fptr)) {
			//t.taskDesc[74] = '\0';
			printf("%s", t.taskDesc);
		}
        	fclose(fptr);
	} else {
		printf("Failed to open tasks file");
		return 1;
	}

	return 0;
}

int main(int argc, char *argv[]) {
	// arr is a ptr to a Task
	// im making space for 5 Tasks with malloc
	struct Task* arr = malloc(1 * sizeof(struct Task));
	int pos = 0;

	if (argc > 1) {
		if (strcmp(argv[1], "add") == 0 && argc == 3) {
			// TODO: need to get the last written task num in list to auto add new one
			// idk if we even need this we can just display them in order
			// status should always be 0
			struct Task t = {0, 0};
			strncpy(t.taskDesc, argv[2], sizeof(t.taskDesc)-2);
			t.taskDesc[sizeof(t.taskDesc) - 1] = '\0';

			int returnCode = writeToFile(&t);

			printf("Task num %d %d %s\n", t.taskNum, t.status, t.taskDesc);
			arr[pos] = t;
			pos = pos + 1;
		}
		else if (strcmp(argv[1], "list") == 0) {
			readFile();
		}
	}

	free(arr);
}
