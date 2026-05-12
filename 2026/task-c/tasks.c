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

int createFile() {
	FILE *fptr;
	fptr = fopen("tasks.txt", "a");
	if (fptr != NULL) {
		fclose(fptr);
		return 0;
	}

	return 1;
}

int writeTaskToFile(struct Task* t) {
	FILE *fptr;
	fptr = fopen("tasks.txt", "a");

	if (fptr != NULL) {
		fprintf(fptr, "%d %s\n", t->taskNum, t->taskDesc);
        	fclose(fptr);
		return 0;
	}

	return 1;
}

int overwriteFile(struct Task* arr, int taskCount) {
	FILE *fptr;
	fptr = fopen("tasks.txt", "w");

	if (fptr != NULL) {
		for (int i = 0; i<taskCount; i++) {
			fprintf(fptr, "%d %s\n", i+1, arr[i].taskDesc);
		}
        	fclose(fptr);
	}

	return 0;
}

int readFile(struct Task* arr) {
	FILE *fptr;
	fptr = fopen("tasks.txt", "r");
	int pos = 0;

	if (fptr != NULL) {
		struct Task t = {0, 0};
		while (fscanf(fptr, "%d %74[^\n]", &t.taskNum, t.taskDesc ) == 2) {
			arr[pos] = t;
			pos = pos+1;
		}
        	fclose(fptr);
		return pos;
	} else {
		printf("Failed to open tasks file");
		return 0;
	}
}

int deleteTask (struct Task* arr, int taskCount, int taskToDelete) {
	for (int i = 0; i<taskCount; i++) {
		if (arr[i].taskNum == taskToDelete) {
			for (int j = i; j < taskCount - 1; j++) {
        			arr[j] = arr[j + 1];
    			}
			taskCount--;
			int status = overwriteFile(arr, taskCount);
			if (status == 0) {
				printf("Task %d deleted..\n", taskToDelete);
				return 0;
			} else {
				printf("Issue deleting task\n");
				return 1;
			}
		}

	}
	printf("Task not found..\n");
	return 0;
}

int main(int argc, char *argv[]) {
	// arr is a ptr to a Task
	struct Task* arr = malloc(10 * sizeof(struct Task));
	int pos = 0;
	int createFlag = createFile();
	if (createFlag != 0) {
		exit(1);
	}
	int taskCount = readFile(arr);

	// TODO: task archive writer
	// - dynamic array

	if (argc > 1) {
		if (strcmp(argv[1], "add") == 0 && argc == 3) {
			struct Task t = {taskCount+1, 0};
			strncpy(t.taskDesc, argv[2], sizeof(t.taskDesc)-1);

			// null terminate string no matter what
			t.taskDesc[sizeof(t.taskDesc) - 1] = '\0';

			writeTaskToFile(&t);
			printf("Task num %d %d %s written to file\n", t.taskNum, t.status, t.taskDesc);
		}
		else if (strcmp(argv[1], "list") == 0) {
			printf("### TASKS ###\n\n");
			for (int i=0; i<taskCount; i++) {
				printf("[%d] %s\n", arr[i].taskNum, arr[i].taskDesc);
			}
		}
		else if (strcmp(argv[1], "delete") == 0 && argc == 3) {
			int taskToDelete = atoi(argv[2]);
			deleteTask(arr, taskCount, taskToDelete);
		}
	}

	free(arr);
}
