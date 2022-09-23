"""Main module."""

from nc_analysis.load_data import load_netcdf
from nc_analysis.stats.kmeans import calc_kmeans

class Dataset:
    def __init__(self, filename):
        self.ds = load_netcdf(filename)

    def kmeans(self, x1_name, x2_name, n_clusters):
        # run kmeans for the dataset for two variables
        x1 = self.ds.variables[x1_name][:].ravel()
        x2 = self.ds.variables[x2_name][:].ravel()
        return x1, x2, calc_kmeans(x1, x2, n_clusters)

