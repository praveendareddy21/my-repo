#include<stdio.h>
foo(int a[][4] ,int i){
printf("%d",a[0][3]);

}
int main()
{
	int a[5][4];
	a[0][3]=11;
	int i=4,m=5;
	foo(a,i);
	int * j,*k;
	j=&i;
	k=j;
	j=&m;
	printf("%d\n",*j);
	printf("%d",*k);



	return 0;
}
