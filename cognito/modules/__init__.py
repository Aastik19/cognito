"""
Data checking module
"""
from __future__ import print_function
import os
import sys
import pandas as pd
import numpy as np


class Check():
    """
    Check class helps us to identify the types of
    variables categorical | Continuous | Discrete
    """
    def __ini__(self):
        pass

    @staticmethod
    def is_working(column="Cognito!"):
        """
        Determines whether the specified command is working.
        :param      column:  The column
        :type       column:  string
        """
        return "Hello, %s! How are you %s?"%(column, column)


    @staticmethod
    def is_categorical(column):
        """
        Determines whether the specified col is categorical.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_categorical(data['Age'])
            >> True
        """
        try:
            return bool(True) if column.dtypes == 'object' else bool(False)

        except AttributeError:

            print("Method only supported pandas.cores.series")


    @staticmethod
    def is_continuous(column):
        """
        Determines whether the specified col is continuous.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_continuous(data['Age'])
            >> False
        """
        try:
            return bool(True) if column.dtypes == 'float64' else bool(False)

        except AttributeError:

            print("Method only supported pandas.cores.series")


    @staticmethod
    def is_discrete(column):
        """
        Determines whether the specified column is discrete.

        :param      column:  column name
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_discrete(data['Age'])
            >> True
        """



    @staticmethod
    def is_identifier(column):
        """
        Determines whether the specified column is identifier.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_identifier(data['Age'])
            >> True

        """



    @staticmethod
    def is_missing(column):
        """
        Determines whether the specified column is having missing.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_missing(data['Price'])
            >> False
        """

    @staticmethod
    def sum(num1, num2):
        """
        Takes two numerical values and gives their sum as output.

        :param     integer: a
        :param     integer: b
        :return    integer: a+b

        Usage:
        ======
            >> Check.sum(10, 20)
            >> 30
        """
        return num1+num2
