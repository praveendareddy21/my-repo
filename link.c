#include<stdio.h>
#include<stdlib.h>
typedef struct link * node;

struct link{
	int elem;
	node next;
};
int main()
{
	node n;
	n=(node)malloc(10*sizeof(struct link));
	int i=0;
	for (i=0;i<10;i++){
		(n+i)->elem=i;
		//(*(n+i)).elem=i;

		//*(n+i).elem=i;  // does not work as  * low precedence than . so (n+i).elem is derefed
	}

	for (i=0;i<10;i++){
		printf("%d \n",(n+i)->elem);
	}



return 0;
}
