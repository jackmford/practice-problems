#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Entry {
	const char* key;
	void* value;
	struct Entry* next;
};

struct HashMap {
	struct Entry** buckets;
	size_t capacity;
	size_t size;
	float load_factor;
};

// djb2 hash
size_t hash(const char* key, size_t capacity) {
	size_t h = 5381;

	// walk the key one char at a time
	while (*key) {
		h = h*33 + (unsigned char)*key;
		key++;
	}
	return h % capacity;
}

struct HashMap* hashmap_create(size_t capacity) {
	struct HashMap* map = malloc(sizeof(struct HashMap));
	if (map == NULL) return NULL;


	// allocate buckets and initialize to zero
	map->buckets = calloc(capacity, sizeof(struct Entry *));

	if (map->buckets == NULL) {
		free(map);
		return NULL;
	}

	map->capacity = capacity;
	map->size = 0;
	map->load_factor = 0.75f;

	return map;
}

void hashmap_set(struct HashMap* map, const char* key, void* value) {
	// Put the entry on the heap
	struct Entry* entry = malloc(sizeof(struct Entry));
	entry->key = key;
	entry->value = value;
	entry->next = NULL;

	// hash the key
	size_t hash_key = hash(key, map->capacity);

	struct Entry* bucket = map->buckets[hash_key];

	if (bucket == NULL) {
        	// empty bucket, just place it directly
		printf("Inserting %s at %zu\n", key, hash_key);
		map->buckets[hash_key] = entry;
		map->size++;
		return;
    	}

	if (strcmp(bucket->key, key) == 0) {
		printf("Updating %s at %zu\n", key, hash_key);
		bucket->value = value;
		free(entry);
		return;
	}
		
	while (bucket->next != NULL) {
		printf("Collision walking on key... %s\n", key);
		bucket = bucket->next;
	}

	map->size++;
	bucket->next = entry;
}

void* hashmap_get(struct HashMap* map, const char* key) {
	size_t hash_key = hash(key, map->capacity);
	struct Entry* entry = map->buckets[hash_key];

	while (entry != NULL) {
		if (strcmp(entry->key, key) == 0) {
			return entry->value;
		}
		entry = entry->next;
	}

	printf("Key not found\n");
	return NULL;
}

void hashmap_delete(struct HashMap* map, const char* key) {
	size_t hash_key = hash(key, map->capacity);
	struct Entry* entry = map->buckets[hash_key];
	struct Entry* prev = NULL;

	while (entry != NULL) {
		if (strcmp(entry->key, key) == 0) {
			if (prev == NULL) {
				// found it right away at the head
				map->buckets[hash_key] = entry->next;
			} else {
				// remove the current matching entry
				prev->next = entry->next;
			}
			free(entry);
			map->size--;
			printf("Deleted key: %s\n", key);
			return;
		}
		prev = entry;
		entry = entry->next;
	}

	printf("Key not found\n");
}


int main() {
	struct HashMap* map = hashmap_create(16);
	if (map == NULL) {
		printf("Allocation failed\n");
		return 1;
	}
	printf("Created map with capacity %zu\n", map->capacity);

	printf("%zu\n", hash("alice", 16));
	printf("%zu\n", hash("alice", 16));
	printf("%zu\n", hash("carol", 16));
	printf("%zu\n", hash("jack", 16));
	printf("%zu\n", hash("jacknum", 16));
	
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
	hashmap_delete(map, "jacknum4");
	printf("Map size: %zu\n", map->size);

	num = 11;
	hashmap_set(map, "jacknum4", &num);

	intpt = hashmap_get(map, "jacknum4");
	if (intpt != NULL){
		printf("Retrieved %d from hashmap\n", *(int *)intpt);
	}

	//TODO implement delete
	//TODO implement automatic resizing

	free(map);
}
