#include <bits/stdc++.h>
using namespace std;

#define increment(in, choice) switch((choice)) { case 'A': (in).a++; break; case 'B': (in).b++; break; case 'C': (in).c++; break;}
#define decrement(in, choice) switch((choice)) { case 'A': (in).a--; break; case 'B': (in).b--; break; case 'C': (in).c--; break;}

int n;
string table;

struct counts {
    int a = 0;
    int b = 0;
    int c = 0;
};

counts count(int l, int r) {
    counts c;
    for (int i = l; i < r; i++)
        increment(c, table[i]);
    
    return c;
}

int getSwaps(counts total, counts a, counts b, counts c) {
    int swaps = 0;
    swaps += b.a;
    swaps += c.a;

    if (a.b > b.a) {
        b.b += b.a;
        c.b += (a.b - b.a);
    } else {
        c.c += c.a;
        b.c += (a.c - c.a);
    }

    swaps += b.c;
    return swaps;
}

int solve(counts total, int a, int b, int c) {
    counts ac = count(a, a + total.a);
    counts bc = count(b, b + total.b);
    counts cc = count(c, c + total.c);

    int m = getSwaps(total, ac, bc, cc);
    for (int i = 0; i < n - 1; i++) {
        decrement(ac, table[(((a) >= n) ? ((a) - n) : ((a)))]);
        decrement(bc, table[(((b) >= n) ? ((b) - n) : ((b)))]);
        decrement(cc, table[(((c) >= n) ? ((c) - n) : ((c)))]);

        increment(ac, table[(((a + total.a) >= n) ? ((a + total.a) - n) : ((a + total.a)))]);
        increment(bc, table[(((b + total.b) >= n) ? ((b + total.b) - n) : ((b + total.b)))]);
        increment(cc, table[(((c + total.c) >= n) ? ((c + total.c) - n) : ((c + total.c)))]);

        a++;
        b++;
        c++;

        m = min(m, getSwaps(total, ac, bc, cc));
    }

    return m;
}

int main() {
    cin >> table;
    n = table.length();

    int m = 2147483647;
    counts total = count(0, n);
    if (total.a == 0 && total.b == 0)
        cout << '0';
    else if (total.a == 0 && total.b == 0)
        cout << '0';
    else if (total.a == 0 && total.b == 0)
        cout << '0';
    else {
        
        m = min(m, solve(total, 0, total.a, total.a + total.b));
        m = min(m, solve(total, total.c + total.b, total.c, 0));
    }

    cout << m;
}