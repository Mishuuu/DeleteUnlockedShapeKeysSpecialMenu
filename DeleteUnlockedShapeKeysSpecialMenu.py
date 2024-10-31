bl_info = {
    "name": "Delete Unlocked Shape Keys",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Shape Keys",
    "description": "Adds option to delete all unlocked shape keys",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}
import bpy

def delete_unlocked_shape_keys(obj):
    if obj.type == 'MESH' and obj.data.shape_keys:
        shape_keys = obj.data.shape_keys.key_blocks
        for i in range(len(shape_keys) - 1, 0, -1):
            if not shape_keys[i].lock_shape:
                obj.shape_key_remove(shape_keys[i])

class DeleteUnlockedShapeKeys(bpy.types.Operator):
    bl_idname = "object.delete_unlocked_shape_keys"
    bl_label = "Delete Unlocked Shape Keys"
    bl_description = "Delete all unlocked shape keys for the active object"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object and context.active_object.type == 'MESH' and context.active_object.data.shape_keys

    def execute(self, context):
        delete_unlocked_shape_keys(context.active_object)
        return {'FINISHED'}

def draw_delete_unlocked_shape_keys(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(DeleteUnlockedShapeKeys.bl_idname)

def register():
    bpy.utils.register_class(DeleteUnlockedShapeKeys)
    bpy.types.MESH_MT_shape_key_context_menu.append(draw_delete_unlocked_shape_keys)

def unregister():
    bpy.utils.unregister_class(DeleteUnlockedShapeKeys)
    bpy.types.MESH_MT_shape_key_context_menu.remove(draw_delete_unlocked_shape_keys)

if __name__ == "__main__":
    register()