#include "hashmap.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int seen_before(const char* const* words, size_t index) {
	for (size_t i = 0; i < index; i++) {
		if (words[i] != NULL && words[index] != NULL && strcmp(words[i], words[index]) == 0) {
			return 1;
		}
	}

	return 0;
}

int main(void) {
	const char* words[] = {
		"apple", "banana", "apple", "orange", "banana",
		"apple", "grape", "orange", "banana"
	};
	size_t word_count = sizeof(words) / sizeof(words[0]);

	struct HashMap* counts = hashmap_create(8);
	if (counts == NULL) {
		printf("Allocation failed\n");
		return 1;
	}

	for (size_t i = 0; i < word_count; i++) {
		int* count = hashmap_get(counts, words[i]);
		if (count == NULL) {
			count = malloc(sizeof(int));
			if (count == NULL) {
				printf("Allocation failed\n");
				return 1;
			}
			*count = 1;
			hashmap_set(counts, words[i], count);
		} else {
			(*count)++;
		}
	}

	printf("Word frequencies:\n");
	for (size_t i = 0; i < word_count; i++) {
		if (seen_before(words, i)) {
			continue;
		}

		int* count = hashmap_get(counts, words[i]);
		if (count != NULL) {
			printf("%s: %d\n", words[i], *count);
		}
	}

	for (size_t i = 0; i < word_count; i++) {
		if (seen_before(words, i)) {
			continue;
		}

		int* count = hashmap_get(counts, words[i]);
		hashmap_delete(counts, words[i]);
		free(count);
	}

	free(counts);
	return 0;
}
