"""
Name: clean.py
Author: Owen Sharpe
Description: every cleaning decision applied to the loaded panel, one small function per rule. The loader stays faithful to the Bloomberg pulls; the judgement calls (which discount curve on which dates, which dates are too thin to use, what counts as a bad print) live here so each one is named, tested, and can be cited in papers.
"""

from __future__ import annotations
