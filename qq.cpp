#include <iostream>
#include <algorithm>
#include <queue>
#include <string.h>
#include <limits.h>
#include <vector>
#include <math.h>
#include <stack>
#include <bitset>
#include <string>
typedef long long ll;
using namespace std;
vector<ll> getPi(string sub) {
	vector<ll> pi(sub.size(), 0);
	for (int i = 1, j = 0; i < sub.size(); i++) {
		while (j > 0 && sub[i] != sub[j]) j = pi[--j];
		if (sub[i] == sub[j]) pi[i] = ++j;
	}
	return pi;
}


int main() {
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	string target;
	ll n;
	cin >> target >> n;
	vector<ll> res = getPi(target);
    for (int i = 1; i < res.size(); i++) {
		cout<<res[i]<<" ";
	}
	cout << n * (ll)target.size() - (ll)res[target.size() - 1] * (n - 1)<<'\n';

	return 0;
}