""" Demonstrating several features of the annotation analysis pipeline.
"""

from SpotAnnotationAnalysis import SpotAnnotationAnalysis
from BaseAnnotation import BaseAnnotation
from QuantiusAnnotation import QuantiusAnnotation

img_filename = 'beads_300pxroi.png'
json_filename = 'BeadAnnotation_20180413.json'
csv_filename = 'bead_annotations_20180517_shifted.csv'
worker_marker_size = 8
cluster_marker_size = 40

ba = QuantiusAnnotation(json_filename)	# Load data into an annotation object
sa = SpotAnnotationAnalysis(ba)			# Annotation object is saved as a property of a SpotAnnotationAnalysis object
anno_all = ba.df()						# Get the dataframe from the annotation object

# --- Plot to get an overview of annotations ---

# show_ref_points = False
# show_workers = True
# show_clusters = True
clustering_alg = 'AffinityPropagation'
clustering_params = [-350]
# show_correctness_workers = False
# show_correctness_clusters = False
# show_NN_inc = False
# correctness_threshold = None

# sa.plot_annotations(anno_all, img_filename, csv_filename, worker_marker_size, cluster_marker_size, show_ref_points, show_workers, show_clusters, show_correctness_workers, show_correctness_clusters, show_NN_inc, correctness_threshold, clustering_alg, clustering_params)

show_correctness = True
correctness_threshold = 5
sa.plot_nnd_vs_time_spent(anno_all, img_filename, csv_filename, show_correctness, correctness_threshold, clustering_alg, clustering_params)






