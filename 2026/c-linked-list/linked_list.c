#include <stdio.h>
#include <stdlib.h>

struct Node {
	int num;
	struct Node* next;
};

struct Node* ll_insert(struct Node* head, int num) {
	struct Node* ptr = head;
	if (ptr == NULL) {
		printf("There is no head node\n");
		struct Node* n = malloc(sizeof(struct Node));
		if (n == NULL) {
			return head;
		}
		n->num = num;
		n->next = NULL;
		return n;
	}

	while (ptr->next != NULL) {
		ptr = ptr->next;
	}

	struct Node* n = malloc(sizeof(struct Node));
	if (n == NULL) {
		return head;
	}
	n->num = num;
	n->next = NULL;

	ptr->next = n;
	return head;
}

struct Node* ll_delete(struct Node* head, int pos) {
	struct Node* ptr = head;
	struct Node* prev = NULL;
	int ctr = 0;
	while (ptr != NULL && ctr != pos) {
		printf("Walking\n");
		prev = ptr;
		ptr = ptr->next;
		ctr++;
	}

	if (ptr == NULL) {
		printf("Ptr is null\n");
		return head;
	}

	if (prev == NULL) {
		printf("Prev is null\n");
		prev = head;
		head = head->next;
		free(prev);
		return head;
	}

	prev->next = ptr->next;
	free(ptr);

	return head;
}

void ll_print(struct Node* head) {
	struct Node* ptr = head;
	int ctr = 0;
	while (ptr != NULL) {
		printf("Item [%d] value [%d]\n", ctr, ptr->num);
		ptr = ptr->next;
		ctr++;
	}
}

int main() {
	printf("Hello world\n");

	struct Node* n = malloc(sizeof(struct Node));
	n->num = 5;
	n->next = NULL;

	struct Node* n2 = malloc(sizeof(struct Node));
	n2->num = 10;
	n2->next = NULL;

	n->next = n2;

	ll_insert(n, 11);
	ll_print(n);
	n = ll_delete(n, 0);
	n = ll_delete(n, 1);
	n = ll_delete(n, 0);
	n = ll_delete(n, 0);
	n = ll_delete(n, 0);
	n = ll_insert(n, 4);
	n = ll_insert(n, 4);
	n = ll_insert(n, 5);
	ll_print(n);

}
