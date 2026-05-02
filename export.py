import bpy

points_2d = [(0, 70), (2, 1), (4, 70), (6, 2)]
depth = 2

def export_to_blender(points_2d, depth):
    verts = []
    for x, y in points_2d:
        verts.append((x, y, 0)) # Bottom vertex
        verts.append((x, y, depth)) # Top vertex

    faces = []
    for i in range(len(points_2d) - 1):
    # the math here is ai
        b1 = i * 2
        t1 = i * 2 + 1
        b2 = (i + 1) * 2
        t2 = (i + 1) * 2 + 1
        
        faces.append((b1, b2, t2, t1))

    # create the object and export it, courtesy of stack overflow

    mesh = bpy.data.meshes.new("BridgeMesh")
    obj = bpy.data.objects.new("Bridge", mesh)
    bpy.context.collection.objects.link(obj)

    mesh.from_pydata(verts, [], faces)
    mesh.update()

    bpy.ops.wm.save_as_mainfile(filepath="bridge.blend")
