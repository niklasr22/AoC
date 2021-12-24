#include <map>
#include <list>
#include <string>
#include <iostream>
using namespace std;

typedef struct _key{
    long a;
    int b;

    bool operator==(const _key &o) const {
        return a == o.a && b == o.b;
    }

    bool operator<(const _key &o) const {
        return a < o.a || (a == o.a && b < o.b);
    }
} key;

map<key, list<string>*> cache;

int ix[] = {13,11,11,10,-14,-4,11,-3,12,-12,13,-12,-15,-12};
int iy[] = {10,16,0,13,7,11,11,10,16,8,15,2,5,10};
int iz[] = {1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 1, 26, 26, 26};

long routine(long z, int d, int pos)
{
    long x = z % 26 + ix[pos];
    z /= iz[pos];
    if (x != d) {
        z = z * 26 + d + iy[pos];
    }
    return z;
}

list<string>* search(long z, int pos)
{
    list<string>* result = new list<string>;
    if (pos == 14) {
        if (z == 0)
            result->push_back("");
    } else {
        for (int d = 1; d <= 9; ++d) {
            long new_z = routine(z, d, pos);
            key k = {pos + 1, new_z};
            string ds = ((string)"") + (char)('0' + d);
            list<string>* res;
            if (cache.count(k) != 0) {
                res = cache[k];
            } else {
                res = search(new_z, pos + 1);
                cache.insert(pair<key, list<string>*>(k, res));
            }
            for (list<string>::iterator it = res->begin(); it != res->end(); it++)
                result->push_back(ds + (*it));
        }
    }
    return result;
}

int main()
{
    list<string>* mainres = search(0, 0);
    long max = 0;
    long min = LONG_MAX;
    for (list<string>::iterator it = mainres->begin(); it != mainres->end(); it++) {
        long l = stol(*it);
        if (l > max)
            max = l;
        if (l < min)
            min = l;
    }
    cout << "a) " << max << "\n";
    cout << "b) " << min << "\n";
    return 0;
}