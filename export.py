import bpy

# TEST DATA MADE MY AI

# 8 corner vertices
verts = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), # Bottom 4
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)  # Top 4
]

# 6 faces (each defines one side of the cube)
faces = [
    (0, 1, 2, 3), # Bottom
    (4, 5, 6, 7), # Top
    (0, 1, 5, 4), # Front
    (1, 2, 6, 5), # Right
    (2, 3, 7, 6), # Back
    (3, 0, 4, 7)  # Left
]


mesh = bpy.data.meshes.new("MyMesh")
obj = bpy.data.objects.new("MyObj", mesh)
bpy.context.collection.objects.link(obj)
mesh.from_pydata(verts, [], faces)

# Save to file
bpy.ops.wm.save_as_mainfile(filepath="output.blend")
