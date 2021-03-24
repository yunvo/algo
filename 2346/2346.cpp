#include <iostream>
#include <vector>
using namespace std;

// queue

int n, m, k = 0, c = 0, d = 1;
int cc = 0;
int q[1000];
bool b[1000];

// 다음 터트릴곳 찾기
int find(int s) {
	while (b[s]) {
		if (d > 0) {
			s++;
			if (s >= n) s = 0;
		}
		else {
			s--;
			if (s < 0) s = n - 1;
		}
	}	
	return s;
}



int main(void) {
	cin >> n;
	m = n;
	for (int i = 0; i < n; i++) {
		cin >> q[i];
		b[i] = false;
	}
	// 첫 풍선 터트리기
	b[0] = true;
	c++;
	cout << k + 1 << " ";

	// 풍선 다 터트릴 때 까지
	while (c < n) {
		cc = 0;
		int l = q[k];
		// 방향
		if (q[k] > 0) d = 1;
		else d = -1;
		// 풍선 터트릴지 판단
		while (true) {
			if (k >= n) k = 0;
			if (k < 0) k = n - 1;
			if (b[k]) k = find(k);
			if (l > 0 && cc == l - 1) {
				b[k] = true;
				break;
			}
			if (l < 0 && cc == l + 1) {
				b[k] = true;
				break;
			}
			if (l > 0) {
				k++;
				cc++;
			}
			else {
				k--;
				cc--;
			}

		}
		cout << k + 1 << " ";
		c++;
	}	
}