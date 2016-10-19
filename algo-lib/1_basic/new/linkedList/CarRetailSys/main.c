#include <stdio.h>

// 汽车管理系统 实质是一个链表

typedef struct carType Car;

struct carType {
	int vehicleID;
	char make[20];			// 汽车制造商
	char model[20];			// model name
	int year;				// Year of manufacture
	int mileage;			// in miles
	double cost;			// in dollars
	Car *next;				// 指向下一个CarType节点
};

// 返回searchID相对应的那个Node之前的Node的指针
Car *ScanList(Car *headPointer, int searchID) {
	// note: 之所以不直接返回找到的Node的指针,而是返回
	//       它之前的Node的指针,是因为这样大大方便了后面的
	//       插入,删除等操作.
	Car *previous;
	Car *current;

	/* Point to start of list */
	previous = headPointer;
	current = headPointer->next;

	// Travserse list -- scan until we find a node with a
	// vehicleID greater than or equal to searchID
	while ((current != NULL) &&
		(current->vehicleID < searchID)) {
		previous = current;
		current = current->next;
	}

	// 返回指向该节点之前的一个节点的指针,或者返回指向最后一个不大于searchID的节点
	// 的指针.
	return previous;
}

void AddEntry(Car *headPointer) {
	Car *newNode;			// 指向新车
	Car *nextNode;			// 这个新车的下一个Car节点
	Car *prevNode;			// 这个新车的前一个节点

	// 动态申请新的内存
	newNode = (Car *) malloc(sizeof(Car));
	// 它返回了申请到的内存地址的首地址指针.

	if(newNode == NULL) {
		printf("Error: could not allocate a new node\n");
		exit(1);
	}

	printf("Enter the following info about the car.\n");
	printf("Seperate each field by white space:\nA");
	printf("vehicle_id make model year mileage cost\n");

	scanf("%d %s %s %d %d %lf, 
		&newNode->vehicleID, newNode->make, newNode->model,
		&newNode->year, &newNode->mileage, &newNode->cost");

	prevNode = ScanList(headPointer, newNode->vehicleID);
	nextNode = prevNode->next;

	// 可以插入的情况
	if((nextNode == NULL) || 
		(nextNode->vehicleID != newNode->vehicleID)) {
		prevNode->next = newNode;
		newNode->next = nextNode;
		printf("Entry added.\n");
	}
	// 不能插入的情况
	else {
		printf("That car already exists in the database!\n");
		printf("Entry not added.\n\n");
		free(newNode);
	}
}

void DeleteEntry(Car *headPointer) {
	int vehicleID;
	Car *delNode;			// 要删除的Node指针
	Car *prevNode;			// 要删除的的Node之前的Node的指针

	printf("Enter the vehicle ID of the car to delete:\n");
	scanf("%d", &vehicleID);

	prevNode = ScanList(headPointer, vehicleID);
	delNode = prevNode->next;

	// 可以删除的情况
	if (delNode != NULL && delNode->vehicleID == vehicleID) {
		prevNode->next = delNode->next;
		printf("vehicle with ID %d deleted.\n\n", vehicleID);
		free(delNode);
	}
	// 不能删除的情况
	else {
		printf("The vehicle was not found in the database\n");
	}
}

void Search(Car *headPointer) {
	int vehicleID;
	Car *searchNode; 	// 要搜索的Node的指针`
	Car *prevNode;		// 要搜索的Node之前的Node的指针

	printf("Enter the vehicle ID number of the car to search for:\n");
	scanf("%d", &vehicleID);

	prevNode = ScanList(headPointer, vehicleID);
	searchNode = prevNode->next;

	if (searchNode != NULL && serachNode->vehicleID == vehicleID) {
		printf("vehicle ID 		: %d\n", searchNode->vehicleID);
		printf("make	   		: %s\n", searchNode->make);
		printf("model	   		: %s\n", searchNode->model);
		printf("year	   		: %d\n", searchNode->year);
		printf("mileage	   		: %d\n", searchNode->mileage);
		printf("cost			: $%10.2f\n\n", searchNode->cost);
	} else {
		printf("The vehicle ID %d was not found in the database.\n\n", vehicleID);
	}
}

int main() {
	int op = 0;				// 当前要执行的操作代码

	Car carBase;			// 空的链表头
	carBase.next = NULL;

	printf("==============================\n");
	printf("=== Used car database ========\n");
	printf("==============================\n");

	while (op != 4) {
		printf("Enter an operation:\n");
		printf("1 - Car aquired. Add a new entry for it.\n");
		printf("2 - sold. Remove its entry.\n");
		printf("3 - Query. Look up a car's informaiton."\n);
		printf("4 - Quit\n");
		scanf("%d", &op);

	if (op == 1)
		AddEntry(&carBase);
	else if (op == 2)
		DeleteEntry(&carBase);
	else if (op == 3)
		Search(&carBase);
	else if (op == 4)
		printf("Goodbye.\n\n");
	else 
		printf("Invalid option. Try again.\n\n");
	}
}