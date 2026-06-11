#include "hashmap.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
	struct HashMap* map = hashmap_create(8);
	if (map == NULL) {
		printf("Allocation failed\n");
		return 1;
	}
	printf("Created map with capacity %zu\n", map->capacity);

	char str[] = "Hi\0";
	hashmap_set(map, "jack", str);

	char str2[] = "Hi2\0";
	hashmap_set(map, "jack", str2);

	int num = 12;
	hashmap_set(map, "jacknum", &num);

	void* strpt = hashmap_get(map, "jack");
	printf("Retrieved %s from hashmap\n", (char *)strpt);

	void* intpt = hashmap_get(map, "jacknum");
	printf("Retrieved %d from hashmap\n", *(int *)intpt);

	strpt = hashmap_get(map, "jack");
	printf("Retrieved %s from hashmap\n", (char *)strpt);

	intpt = hashmap_get(map, "jacknum");
	printf("Retrieved %d from hashmap\n", *(int *)intpt);

	hashmap_set(map, "jacknum1", &num);
	hashmap_set(map, "jacknum2", &num);
	hashmap_set(map, "jacknum3", &num);
	hashmap_set(map, "jacknum4", &num);

	printf("Map items: %zu\n", map->size);
	hashmap_delete(map, "jacknum4");
	printf("Map items: %zu\n", map->size);

	num = 11;
	hashmap_set(map, "jacknum4", &num);
	printf("Map items: %zu\n", map->size);

	intpt = hashmap_get(map, "jacknum4");
	if (intpt != NULL){
		printf("Retrieved %d from hashmap\n", *(int *)intpt);
	}

	hashmap_delete(map, "jacknum4");
	printf("Map items: %zu\n", map->size);

	//free(map);
	hashmap_destroy(map);
}
