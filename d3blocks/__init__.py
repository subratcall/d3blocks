from d3blocks.d3blocks import d3blocks
# import d3blocks.Movingbubbles as Movingbubbles
# import d3blocks.timeseries.Timeseries as Timeseries
import movingbubbles.Movingbubbles as Movingbubbles
import timeseries.Timeseries as Timeseries

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.2.0'

# module level doc-string
__doc__ = """
d3blocks
=====================================================================

Description
-----------
d3blocks is for the creation of exclusive stand alone and interactive graphs in d3 javascript.

Example
-------
>>> from d3blocks import d3blocks
>>> d3 = d3blocks()
>>> df = d3.import_example(data='random_time')
>>> d3.movingbubbles(df)

References
----------
https://github.com/d3blocks/d3blocks

"""
