bl_info = {
    "name": "Open VSE Documentation",
    "author": "tintwotin",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "location": "Sequencer > View Menu > Documentation",
    "description": "Expose option to ppen online VSE documentation",
    "warning": "",
    "doc_url": "",
    "category": "Sequencer",
}

import bpy
from bpy.types import Operator
import webbrowser


class OPERATOR_OT_open_vse_docs(Operator):
    """Open online VSE documentation"""

    bl_idname = "sequencer.vse_docs"
    bl_label = "Documentation"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        webbrowser.open("vse-docs.readthedocs.io")

        return {"FINISHED"}


def menu_append(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(OPERATOR_OT_open_vse_docs.bl_idname)


def register():
    bpy.utils.register_class(OPERATOR_OT_open_vse_docs)
    bpy.types.SEQUENCER_MT_view.append(menu_append)


def unregister():
    bpy.utils.unregister_class(OPERATOR_OT_open_vse_docs)
    bpy.types.SEQUENCER_MT_view.remove(menu_append)


if __name__ == "__main__":
    register()
