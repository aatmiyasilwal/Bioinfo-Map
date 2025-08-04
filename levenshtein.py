#levenshtein.py
import streamlit as st
from data import campusMappings

class StringComparer:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for row in range(len(word1) + 1):
            dp.append([])
            for col in range(len(word2) + 1):
                if row == 0:
                    dp[row].append(col)
                elif col == 0:
                    dp[row].append(row)
                else:
                    if word1[row - 1].lower() == word2[col - 1].lower():  # Case insensitive comparison
                        dp[row].append(min(dp[row - 1][col] + 1, dp[row][col - 1] + 1, dp[row - 1][col - 1]))
                    else:
                        dp[row].append(min(dp[row - 1][col] + 1, dp[row][col - 1] + 1, dp[row - 1][col - 1] + 1))

        return dp[-1][-1]

    def checkString(self, input_string: str, hkuPlaces: list):
        closest_match = None
        min_distance = float('inf')

        for place in hkuPlaces:
            distance = self.minDistance(input_string, place)
            if distance == 0:
                return place  # Exit if an exact match is found
            elif distance < min_distance:
                min_distance = distance
                closest_match = place

        if closest_match:
            return closest_match
        else:
            return ""