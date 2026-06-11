#ifndef HASHMAP_H
#define HASHMAP_H

#include <stddef.h>

//struct HashMap;

struct HashMap {
	// a pointer to an array of pointers going to entries
	struct Entry** buckets;
	size_t capacity;
	size_t size;
	float load_factor;
};


struct HashMap* hashmap_create(size_t capacity);
void hashmap_set(struct HashMap* map, const char* key, void* value);
void* hashmap_get(struct HashMap* map, const char* key);
int hashmap_destroy(struct HashMap* map);
int hashmap_delete(struct HashMap* map, const char* key);
size_t hashmap_size(struct HashMap* map);

#endif
