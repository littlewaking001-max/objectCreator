import maya.cmds as cmds

def create_object(obj_type, name=None):
	obj_map = {
		'cube': cmds.polyCube,
		'cone': cmds.polyCone,
		'sphere': cmds.polySphere,
		'torus': cmds.polyTorus
	}

	if obj_type not in obj_map:
		cmds.warning(f"Unknown object type: {obj_type}")
		return None

	result = obj_map[obj_type]()
	obj = result[0]

	if name:
		obj = cmds.rename(obj, name)

	cmds.select(obj)
	return obj