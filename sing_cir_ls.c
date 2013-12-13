#include<stdio.h>
#include<stdlib.h>
struct node{
	int elem;
	struct node * next;
};
typedef struct node * Node;

Node fill_ls(int a[] ,int len,Node po){
int i,j;
Node new,cur=po;
for(i=1;i<len;i++){
	new=( Node)malloc(sizeof(struct node));// u r goin mad wid dis eh ! ! !get ur shit together !!!

	new->next=NULL;
	new->elem=a[i];
	printf("NOW %d \n",new->elem);
	cur->next=new;
	cur=cur->next;
}

printf("NOW HERE%d \n",po->elem);
	
return po;

}

Node insert_ls(Node po,int el){
	printf("ik");
	Node cur,prev,new;
	prev=po;
	cur=po->next;
	
	new=( Node)malloc(sizeof(struct node));
	new->elem=el;
	//bor

	while(1){
		if (cur->elem >el && prev-> elem < el){
			prev->next=new;
			new->next=cur;
			break;


		}
		if (cur->elem  < el && prev->elem > el){
			prev->next=new;
			new->next=cur;
			break;
		}
		cur=cur->next;
		prev=cur;


	}

	return po;
}

int main(){
	int i,j,len=9;
	int * k;
	int a[9] = {1,3,4,6,8,11,14,23,45};
	Node n,copy;
	n=( Node)malloc(sizeof(struct node));
	n->elem=a[0];
	n->next=NULL;
	copy=n;
	printf("seem %d",n);
	printf("al %d",n->elem);
	fill_ls(a,len,n);
	printf("al %d",n->elem);
	
	while(1){
		if (n==NULL ) break;

		printf("^ %d\n",n->elem);
		n=n->next;
	}
	printf("** %d\n",copy->elem);
	insert_ls(copy,17);
return 0;
}
