
from nc_analysis import Dataset
import matplotlib.pyplot as plt

filename = "./nc_analysis/sample_data/DBRD-NATURE2020-depth.r0.1.nc"
ds = Dataset(filename)
x1, x2, model = ds.kmeans('dvs', 'lQ', 4)

print("cluster centers:")
print(model.cluster_centers_)

cluster_id = model.labels_
plt.scatter(x1, x2, c=cluster_id)
plt.xlabel('dvs')
plt.ylabel('lQ')
plt.ylim(0, 8)
plt.title('cluster classification')
plt.show()

print("finished")
