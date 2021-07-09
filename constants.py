import os


# the name of the module this addon lives in
MODULE = "layer_painter"


# id names of different nodes for cleaner notation
NODES = {
    "TEX":      "ShaderNodeTexImage",
    "MAPPING":  "ShaderNodeMapping",
    "COORDS":   "ShaderNodeTexCoord",
    "PRINC":    "ShaderNodeBsdfPrincipled",
    "MIX":      "ShaderNodeMixRGB",
    "RGB":      "ShaderNodeRGB",
    "OUT":      "ShaderNodeOutputMaterial",
    "NORMAL":   "ShaderNodeNormalMap",
    "BUMP":     "ShaderNodeBump",
    "DISP":     "ShaderNodeDisplacement",
    "FRAME":    "NodeFrame",
    "EMIT":     "ShaderNodeEmission",
}


# name of the opacity node inside a layer
OPAC_NAME = "OPACITY"


# name of the group input node inside a lp node group
INPUT_NAME = "INPUTS"

# name of the group output node inside a lp node group
OUTPUT_NAME = "OUTPUTS"


# name of the preview emission node
PREVIEW_EMIT_NAME = "LP Preview Emit"

# name of the preview output node
PREVIEW_OUT_NAME = "LP Preview Out"