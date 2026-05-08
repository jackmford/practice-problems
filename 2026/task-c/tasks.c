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

int main(int argc, char *argv[]) {

	// arr is a ptr to a Task
	// im making space for 5 Tasks with malloc
	struct Task* arr = malloc(5 * sizeof(struct Task));
	int pos = 0;

	if (argc > 1) {
		if (strcmp(argv[1], "add") == 0 && argc == 5) {
			struct Task t = {atoi(argv[2]), atoi(argv[3])};
			strncpy(t.taskDesc, argv[4], 74);
			t.taskDesc[74] = '\0';

			printf("Task num %d %d %s\n", t.taskNum, t.status, t.taskDesc);
			arr[pos] = t;
			pos = pos + 1;
		}
		else {
			printf("Incorrect argument number\n");
		}
	}

	printf("%s\n", arr->taskDesc);
	free(arr);
}
