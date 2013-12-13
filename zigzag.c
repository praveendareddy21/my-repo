#include<stdio.h>
int getval(int i ,int j)
{
	int amval=(i+j)*(i+j+1)/2;
	if((i+j)%2==0 ){
		amval=amval+j+1;

	}
	else {
		amval=amval+i+1;

	}

return amval;
}
int main()
{
	int i,j,k,l;
	int nv,kv;
	int x=0,y=0;
	unsigned long long sum=1;
	char str[1000];
	scanf("%d %d",&nv ,&kv);
	scanf("%s",str);
	//printf("@%d",getval(2,1));
	for(i=0;i<kv;i++){
		if (str[i]=='U'){
			x--;
			sum=sum+getval(x,y);
			continue;

		}
		if (str[i]=='D'){
			x++;
			sum=sum+getval(x,y);
			continue;

			
		}
			
		if (str[i]=='L'){
			y--;
			sum=sum+getval(x,y);
			continue;

			
		}
		if (str[i]=='R'){
			y++;
			sum=sum+getval(x,y);
			continue;

		}

		
	}
	printf("%lld",sum);
	
	return 0;
}
