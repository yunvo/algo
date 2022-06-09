// 2021-03-24
// BOJ 2800 괄호 제거
// Kim Jun Woo

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string s;
vector<string> ans;

int pair_end(string sp, int start) {
	int c = 0; 
	for (int i = start + 1; i < sp.length(); i++) {
		if (sp[i] == '(') c++;
		if (sp[i] == ')') {
			if (c == 0) {
				return i;
			}
			else {
				c--;
			}
		}
	}
}

void solve(string sp) {
	string spp;
	for (int i = 0; i < sp.length(); i++) {
		spp = sp;
		if (sp[i] == '(') {
			spp.erase(pair_end(sp, i), 1);
			spp.erase(i, 1);
			// 중복값 넣지 않기
			if (find(ans.begin(), ans.end(), spp) == ans.end()) {
				ans.push_back(spp);
				solve(spp);
			}
		}
	}
}

int main(void) {
	getline(cin, s);

	solve(s);
	sort(ans.begin(), ans.end());
	// 중복 제거
	ans.erase(unique(ans.begin(), ans.end()), ans.end());

	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << endl;
	}
	return 0;
}