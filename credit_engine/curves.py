"""
Name: curves.py
Author: Owen Sharpe
Description: OIS discount curve. Bootstraps discount factors from one day's OIS par quotes and interpolates log-linearly between nodes (piecewise-constant forwards). Knows nothing about the panel or dates: it takes a single day's cleaned quotes and returns a curve.
"""

from __future__ import annotations
