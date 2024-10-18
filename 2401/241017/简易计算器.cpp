#include <bits/stdc++.h>
using namespace std;
int main()
{
	int a,b;
	char character;
	cin>>a>>character>>b; 
	
	if(character=='+') 
	{
		// ¸´ºÏÓï¾ä 
		cout<<a+b;
	} 
	if(character=='-') 
	{
		cout<<a-b;
	}
	if(character=='*')
	{
		cout<<a*b;
	} 
	if(character=='/' && b!=0) 
	{
		cout<<a/b;
	}
	else
	{
		cout<<"ERROR";
	}

	return 0;
}

