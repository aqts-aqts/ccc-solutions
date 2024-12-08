#include <bits/stdc++.h>

int main() {
    int n;
    std::cin >> n;

    std::cout << std::fixed << std::setprecision(28);

    std::vector<std::pair<double, double>> sheep;
    sheep.reserve(n);

    for (int i = 0; i < n; ++i) {
        double x, y;
        std::cin >> x >> y;
        sheep.emplace_back(x, y);
    }

    for (int i = 0; i < n; ++i) {
        std::pair<double, double> interval = {0, 1000};

        for (int j = 0; j < n; ++j) {
            if (i == j) {
                continue;
            }

            auto [x1, y1] = sheep[i];
            auto [x2, y2] = sheep[j];

            if (x1 == x2) {
                if (y1 > y2) {
                    interval = {1, 0};
                    break;
                }
                continue;
            } else if (x1 > x2) {
                double min_x = (x2 * x2) / (2 * (-x1 + x2)) + (y2 * y2) / (2 * (-x1 + x2)) - (x1 * x1) / (2 * (-x1 + x2)) - (y1 * y1) / (2 * (-x1 + x2));
                interval.first = std::max(interval.first, min_x);
            } else {
                double max_x = (x2 * x2) / (2 * (-x1 + x2)) + (y2 * y2) / (2 * (-x1 + x2)) - (x1 * x1) / (2 * (-x1 + x2)) - (y1 * y1) / (2 * (-x1 + x2));
                interval.second = std::min(interval.second, max_x);
            }

            if (interval.first > interval.second) {
                break;
            }
        }

        if (interval.first <= interval.second) {
            std::cout << std::fixed << std::setprecision(2);
            std::cout << "The sheep at (" << sheep[i].first << ", " << sheep[i].second << ") might be eaten.\n";
        }
    }

    return 0;
}