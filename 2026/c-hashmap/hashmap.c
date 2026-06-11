#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Entry {
	const char* key;
	void* value;
	struct Entry* next;
};

struct HashMap {
	// a pointer to an array of pointers going to entries
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

static int hashmap_resize(struct HashMap* map) {
	// saving old entries
	size_t oldCapacity = map->capacity;
	struct Entry** oldBuckets = map->buckets;

	// allocating new memory for new entries
	// and assigning original buckets to new memory
	struct Entry** newEntries = calloc(map->capacity*2, sizeof(struct Entry *));
	if (newEntries == NULL) {
		return 1;
	}
	map->capacity = map->capacity*2;
	map->buckets = newEntries;

	// copy the old buckets over
	// walk linked lists
	for (size_t i = 0; i < oldCapacity; i++) {
		struct Entry* entry = oldBuckets[i];
		while (entry != NULL) {
			struct Entry* next = entry->next;
			size_t new_hash = hash(entry->key, map->capacity);

			// you have to set this in case there was a collision resizing, it gets saved here not overwritten
			// if theres nothing there then next just becomes null because of calloc
			entry->next = map->buckets[new_hash];
			map->buckets[new_hash] = entry;
			entry = next;
		}
	}

	free(oldBuckets);
	printf("New map capacity is %zu\n", map->capacity);
	return 0;
}

int hashmap_set(struct HashMap* map, const char* key, void* value) {
	if (map->size+1 / (float)map->capacity > map->load_factor) {
		int status = hashmap_resize(map);
		if (status != 0) {
			return 1;
		}
	}
	// Put the entry on the heap
	struct Entry* entry = malloc(sizeof(struct Entry));
	if (entry == NULL) {
		return 1;
	}

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
		return 0;
    	}
		
	while (bucket->next != NULL) {
		printf("Collision walking on key... %s\n", key);
		if (strcmp(bucket->key, key) == 0) {
			printf("Updating %s at %zu\n", key, hash_key);
			bucket->value = value;
			free(entry);
			return 0;
		}
		bucket = bucket->next;
	}

	// final element in bucket check
	if (strcmp(bucket->key, key) == 0) {
		printf("Updating %s at %zu\n", key, hash_key);
		bucket->value = value;
		free(entry);
		return 0;
	}

	bucket->next = entry;
	map->size++;
	return 0;
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

	return NULL;
}

int hashmap_delete(struct HashMap* map, const char* key) {
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
			return 0;
		}
		prev = entry;
		entry = entry->next;
	}
	printf("Key not found\n");
	return 1;
}

int hashmap_destroy(struct HashMap* map) {
	if (map == NULL) {
		return 0;
	}
	if (map->buckets == NULL) {
		free(map);
		return 0;
	}

	for (size_t i=0; i<map->capacity; i++) {
		struct Entry* entry = map->buckets[i];
		while (entry != NULL) {
			struct Entry* next = entry->next;
			free(entry);
			entry = next;
		}
	}
	free(map->buckets);
	free(map);
	return 0;
}

size_t hashmap_size(struct HashMap* map) {
	return map->size;
}
