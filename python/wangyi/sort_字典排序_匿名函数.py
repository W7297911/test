sums=[{"xuhao":2,"age":20},{"xuhao":8,"age":29},{"xuhao":6,"age":25},{"xuhao":22,"age":23}]
sums.sort(key=lambda x:x["xuhao"])
print(sums)
sums.sort(key=lambda x:x["age"],reverse=True)
print(sums)

