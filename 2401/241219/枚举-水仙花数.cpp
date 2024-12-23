#include <bits/stdc++.h>
using namespace std;
int main()
{
	for(int b=1;b<=9;b++) 
		for(int s=0;s<=9;s++)
			for(int g=0;g<=9;g++)
				if(b*b*b+s*s*s+g*g*g==b*100+s*10+g)
					cout<<b*100+s*10+g<<endl;


	return 0;
}

