import bpy
from . import layers, channels, presets, interface


classes = (
    layers.LP_OT_AddFillLayer,
    layers.LP_OT_AddPaintLayer,
    layers.LP_OT_RemoveLayer,
    layers.LP_OT_MoveLayerUp,
    layers.LP_OT_MoveLayerDown,
    channels.LP_OT_MakeChannel,
    channels.LP_OT_RemoveChannel,
    channels.LP_OT_MoveChannelUp,
    channels.LP_OT_MoveChannelDown,
    presets.LP_OT_PbrSetup,
    interface.LP_OT_SwitchToNodeEditor,
)
reg_classes, unreg_classes = bpy.utils.register_classes_factory(classes)


def register():
    reg_classes()


def unregister():
    unreg_classes()