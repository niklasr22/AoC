#include <fstream>
#include <vector>
#include <iostream>
#include <tuple>
#include <map>
#include <string>
#include <sstream>

using namespace std;

tuple<vector<string>, vector<string>> getLines()
{
    ifstream file("2024/inputs/day5.txt");
    vector<string> rules;
    vector<string> updates;

    string line;
    vector<string> *current = &rules;
    while (getline(file, line))
    {
        if (line == "")
        {
            current = &updates;
            continue;
        }
        current->push_back(line);
    }

    file.close();
    return {rules, updates};
}

int main()
{
    auto data = getLines();
    vector<string> raw_rules = get<0>(data);
    vector<string> updates = get<1>(data);
    map<string, vector<string>> rules;

    for (string rule : raw_rules)
    {
        int sep = rule.find("|");
        string key = rule.substr(0, sep);
        string value = rule.substr(sep + 1);
        rules[key].push_back(value);
    }

    int a_mid_sum, b_mid_sum = 0;
    for (string update : updates)
    {
        vector<string> pages;

        stringstream ss(update);
        string page;
        while (getline(ss, page, ','))
        {
            pages.push_back(page);
        }

        vector<string> copied_pages(pages);
        sort(copied_pages.begin(), copied_pages.end(), [&rules](string a, string b)
             {
            if (rules.find(a) != rules.end() && find(rules[a].begin(), rules[a].end(), b) != rules[a].end())
            {
                return true;
            }
            else
            {
                return false;
            } });

        if (equal(copied_pages.begin(), copied_pages.end(), pages.begin()))
        {
            a_mid_sum += atoi(pages[pages.size() / 2].c_str());
        }
        else
        {
            b_mid_sum += atoi(copied_pages[copied_pages.size() / 2].c_str());
        }
    }

    cout << "A: " << a_mid_sum << endl;
    cout << "B: " << b_mid_sum << endl;

    return 0;
}