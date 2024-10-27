#include <bits/stdc++.h>
using namespace std;
int main()
{
	int input, ge, shi, bai, summury, outer;
	cin>>input;
	
	outer = input;
	ge = input % 10;
	input = input - ge;
	shi = input % 100;
	shi = shi / 10;
	bai = input / 100;
	
	summury = ge*ge*ge+shi*shi*shi+bai*bai*bai;
	if (summury == outer)
		cout<<"YES";	
		else
		cout<<"NO";

	return 0;
}

