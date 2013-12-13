#include<iostream>
#include<string>
using namespace std ;
int main(){
	string s1=" brand new string";
	cout<<"flash program"<<s1<<endl;
	char buf[20];
	string s2= " and ";
	string s3=s1 + s2;
	cout<<s3[5];
	s3.copy(buf);
	
	return 0;
}
