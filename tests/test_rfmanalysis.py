#!/usr/bin/env python

"""Tests for `rfmanalysis` package."""

#import pytest


from rfmanalysis import rfmanalysis



analysis = RFMAnalysis(data,  'customer_id', 'order_date', 'revenue')

# Create RFM columns
analysis.create_rfm_columns()

# Scale RFM columns
analysis.scale_rfm_columns()

# Calculate RFM scores and segments
analysis.rfm_scores()

# Give names to the RFM segments
analysis.give_names_to_segments()

# Get the distribution of RFM segments
segment_distribution = analysis.segments_distribution()
print(segment_distribution)
visualizer = RFMVisualizer()
# Create an instance of RFMVisualizer
visualizer.plot_rfm(analysis.rfm_data)
visualizer.visualize_segments(analysis.rfm_data)
visualizer.segment_distribution_barplot(analysis.rfm_data)
visualizer.segment_boxplot(analysis.rfm_data)

# Assuming you have the RFM data in a variable named 'rfm_data'
#visualizer.segment_piechart(analysis.rfm_data)
visualizer.segment_comparison(analysis.rfm_data)