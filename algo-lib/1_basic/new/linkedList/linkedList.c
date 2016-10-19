#include <stdio.h>

typedef struct ListElement {
	struct ListElement *next;
} ListElement;

typedef struct IntElement {
	int data;
	struct IntElement *next;
} IntElement;


// 给定链表首元素, 要求删除链表中的特定值的元素.?
bool deleteElement( IntElement **head, IntElement *deleteMe) {
	IntElement *elem;

	if (!head || !*head || !deleteMe ) // Check for null pointers
		return false;

	elem = *head;
	if (deleteMe == *head) {// case: head
		*head = elem->next;
		free(deleteMe);
		return true;

}



typedef struct Node{
    int data;    
    struct Node *pNext;
    }NODE, *PNODE;  //NODE等价于struct Node， PNODE是struct Node * 型的指针.

