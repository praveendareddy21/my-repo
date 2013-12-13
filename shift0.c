#include<iostream>
using namespace std;
int main()
{
	int arr[10];
	int i,j,k,l;
	int count;
	int index;
	cin>>count;
	for(i=0;i<count;i++){
		cin>>arr[i];
	}
	index =0;
	for (i=0;i<count;i++)
	{
		if(arr[i]>0){
			arr[index]=arr[i];
			index++;
		}
	}
	for(i=index;i<count;i++)
	{
		arr[i]=0;
	}
	for(i=0;i<count;i++)
	{
		cout<<arr[i]<<endl;
	}

	return 0;


}
