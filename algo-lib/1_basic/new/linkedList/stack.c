typedef struct Element {
	void *data;
	struct Element *next;
} Element;

void push(Element *stack, void *data);
void *pop(Element *stack);