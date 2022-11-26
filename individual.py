#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    weather = (7, 2, -1, 0, -3, 4, -1, 3, 2, 0, -5, -9, -15, -6, -2,
                    0, 1, -2, 4, 1, 4, 2, -3, 1, 3, 5, 0, -2, 6, 3)
    precipitation = (120, 222, 0, 0, 107, 41, 134, 0, 0, 0, 45, 23, 0, 45, 32,
                          66, 0, 0, 0, 0, 0, 0, 244, 198, 0, 0, 0, 54, 0, 0)

    rain = 0
    snow = 0
    for i, item in enumerate(weather):
        if item > 0:
            rain += precipitation[i]
        else:
            snow += precipitation[i]

    print(f"rain fell {rain} mm")
    print(f"snow fell {snow} mm")