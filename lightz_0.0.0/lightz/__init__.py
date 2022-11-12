# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Lightz",
    "author" : "Jishu Artz", 
    "description" : "This addon is for making your scene better and faster by using lightz.",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 0),
    "location" : "",
    "warning" : "Do not try to click the 'Light it Up!' button by changing your pivot point. This addon cant take more than 10 lights",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Lighting" 
}


import bpy
import bpy.utils.previews
from .easybpy import *
from random import uniform
import os


addon_keymaps = {}
_icons = None


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


class SNA_OT_Light_It_Up_C570F(bpy.types.Operator):
    bl_idname = "sna.light_it_up_c570f"
    bl_label = "Light it up"
    bl_description = "Add lights to your scene"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        #Scene setup
        create_collection("Lights")
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)
        #Light setup
        bpy.ops.object.light_add(type='AREA', align='WORLD', location=(-2.24954, 0, 3.67798 ), scale=(1, 1, 1))
        translate_along_x(-2.24954)
        move_along_x(-2.24954)
        translate_along_z(3.67798)
        move_along_z(3.67798)
        rotate_around_x(0.000002)
        rotate_around_y(-31.45)
        rotate_around_z(0)
        #Collection setup
        select_all_lights()
        objs = bpy.context.selected_objects
        coll_target = bpy.context.scene.collection.children.get("Lights")
        if coll_target and objs:
            # Loop through all objects
            for ob in objs:
                # Loop through all collections the obj is linked to
                for coll in ob.users_collection:
                    # Unlink the object
                    coll.objects.unlink(ob)
                # Link each object to the target collection
                coll_target.objects.link(ob)
                collection_name = "Lights"
        collection_found = False
        for collection in bpy.data.collections:
            if collection.name == collection_name:
                collection.color_tag = "COLOR_03"
                collection_found = True
                break
        if not collection_found:
            collection = bpy.data.collections.new(collection_name)
            collection.color_tag = "COLOR_03"
            bpy.context.scene.collection.children.link(collection)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_INDIVIDUAL_SETTINGS_C0512(bpy.types.Panel):
    bl_label = 'Individual Settings'
    bl_idname = 'SNA_PT_INDIVIDUAL_SETTINGS_C0512'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Lightz'
    bl_order = 1
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_ECFD2 = layout.box()
        box_ECFD2.alert = False
        box_ECFD2.enabled = True
        box_ECFD2.active = True
        box_ECFD2.use_property_split = False
        box_ECFD2.use_property_decorate = False
        box_ECFD2.alignment = 'Expand'.upper()
        box_ECFD2.scale_x = 1.0
        box_ECFD2.scale_y = 1.0
        box_ECFD2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_ECFD2.label(text='Light 1', icon_value=302)
        box_ECFD2.prop(bpy.data.lights['Area'], 'type', text='Light type', icon_value=0, emboss=True)
        box_ECFD2.prop(bpy.data.lights['Area'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_ECFD2.prop(bpy.data.lights['Area'], 'color', text='Color', icon_value=0, emboss=True)
        box_ECFD2.prop(bpy.data.lights['Area'], 'energy', text='Power', icon_value=328, emboss=True)
        box_ECFD2.prop(bpy.data.lights['Area'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_ECFD2.prop(bpy.data.lights['Area'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_ECFD2.prop(bpy.data.objects['Area'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_B8E48 = layout.box()
        box_B8E48.alert = False
        box_B8E48.enabled = True
        box_B8E48.active = True
        box_B8E48.use_property_split = False
        box_B8E48.use_property_decorate = False
        box_B8E48.alignment = 'Expand'.upper()
        box_B8E48.scale_x = 1.0
        box_B8E48.scale_y = 1.0
        box_B8E48.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_B8E48.label(text='Light 2', icon_value=302)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'type', text='Light type', icon_value=0, emboss=True)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'color', text='Color', icon_value=0, emboss=True)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'energy', text='Power', icon_value=328, emboss=True)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_B8E48.prop(bpy.data.lights['Area.001'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_B8E48.prop(bpy.data.objects['Area.001'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_E7109 = layout.box()
        box_E7109.alert = False
        box_E7109.enabled = True
        box_E7109.active = True
        box_E7109.use_property_split = False
        box_E7109.use_property_decorate = False
        box_E7109.alignment = 'Expand'.upper()
        box_E7109.scale_x = 1.0
        box_E7109.scale_y = 1.0
        box_E7109.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_E7109.label(text='Light 3', icon_value=302)
        box_E7109.prop(bpy.data.lights['Area.002'], 'type', text='Light type', icon_value=0, emboss=True)
        box_E7109.prop(bpy.data.lights['Area.002'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_E7109.prop(bpy.data.lights['Area.002'], 'color', text='Color', icon_value=0, emboss=True)
        box_E7109.prop(bpy.data.lights['Area.002'], 'energy', text='Power', icon_value=328, emboss=True)
        box_E7109.prop(bpy.data.lights['Area.002'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_E7109.prop(bpy.data.lights['Area.002'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_E7109.prop(bpy.data.objects['Area.002'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_34406 = layout.box()
        box_34406.alert = False
        box_34406.enabled = True
        box_34406.active = True
        box_34406.use_property_split = False
        box_34406.use_property_decorate = False
        box_34406.alignment = 'Expand'.upper()
        box_34406.scale_x = 1.0
        box_34406.scale_y = 1.0
        box_34406.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_34406.label(text='Light 4', icon_value=302)
        box_34406.prop(bpy.data.lights['Area.003'], 'type', text='Light type', icon_value=0, emboss=True)
        box_34406.prop(bpy.data.lights['Area.003'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_34406.prop(bpy.data.lights['Area.003'], 'color', text='Color', icon_value=0, emboss=True)
        box_34406.prop(bpy.data.lights['Area.003'], 'energy', text='Power', icon_value=328, emboss=True)
        box_34406.prop(bpy.data.lights['Area.003'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_34406.prop(bpy.data.lights['Area.003'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_34406.prop(bpy.data.objects['Area.003'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_24FC2 = layout.box()
        box_24FC2.alert = False
        box_24FC2.enabled = True
        box_24FC2.active = True
        box_24FC2.use_property_split = False
        box_24FC2.use_property_decorate = False
        box_24FC2.alignment = 'Expand'.upper()
        box_24FC2.scale_x = 1.0
        box_24FC2.scale_y = 1.0
        box_24FC2.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_24FC2.label(text='Light 5', icon_value=302)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'type', text='Light type', icon_value=0, emboss=True)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'color', text='Color', icon_value=0, emboss=True)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'energy', text='Power', icon_value=328, emboss=True)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_24FC2.prop(bpy.data.lights['Area.004'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_24FC2.prop(bpy.data.objects['Area.004'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_A9013 = layout.box()
        box_A9013.alert = False
        box_A9013.enabled = True
        box_A9013.active = True
        box_A9013.use_property_split = False
        box_A9013.use_property_decorate = False
        box_A9013.alignment = 'Expand'.upper()
        box_A9013.scale_x = 1.0
        box_A9013.scale_y = 1.0
        box_A9013.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_A9013.label(text='Light 6', icon_value=302)
        box_A9013.prop(bpy.data.lights['Area.005'], 'type', text='Light type', icon_value=0, emboss=True)
        box_A9013.prop(bpy.data.lights['Area.005'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_A9013.prop(bpy.data.lights['Area.005'], 'color', text='Color', icon_value=0, emboss=True)
        box_A9013.prop(bpy.data.lights['Area.005'], 'energy', text='Power', icon_value=328, emboss=True)
        box_A9013.prop(bpy.data.lights['Area.005'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_A9013.prop(bpy.data.lights['Area.005'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_A9013.prop(bpy.data.objects['Area.005'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_A1B6A = layout.box()
        box_A1B6A.alert = False
        box_A1B6A.enabled = True
        box_A1B6A.active = True
        box_A1B6A.use_property_split = False
        box_A1B6A.use_property_decorate = False
        box_A1B6A.alignment = 'Expand'.upper()
        box_A1B6A.scale_x = 1.0
        box_A1B6A.scale_y = 1.0
        box_A1B6A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_A1B6A.label(text='Light 7', icon_value=302)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'type', text='Light type', icon_value=0, emboss=True)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'color', text='Color', icon_value=0, emboss=True)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'energy', text='Power', icon_value=328, emboss=True)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_A1B6A.prop(bpy.data.lights['Area.006'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_A1B6A.prop(bpy.data.objects['Area.006'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_FCED4 = layout.box()
        box_FCED4.alert = False
        box_FCED4.enabled = True
        box_FCED4.active = True
        box_FCED4.use_property_split = False
        box_FCED4.use_property_decorate = False
        box_FCED4.alignment = 'Expand'.upper()
        box_FCED4.scale_x = 1.0
        box_FCED4.scale_y = 1.0
        box_FCED4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_FCED4.label(text='Light 8', icon_value=302)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'type', text='Light type', icon_value=0, emboss=True)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'color', text='Color', icon_value=0, emboss=True)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'energy', text='Power', icon_value=328, emboss=True)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_FCED4.prop(bpy.data.lights['Area.007'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_FCED4.prop(bpy.data.objects['Area.007'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_2D9A6 = layout.box()
        box_2D9A6.alert = False
        box_2D9A6.enabled = True
        box_2D9A6.active = True
        box_2D9A6.use_property_split = False
        box_2D9A6.use_property_decorate = False
        box_2D9A6.alignment = 'Expand'.upper()
        box_2D9A6.scale_x = 1.0
        box_2D9A6.scale_y = 1.0
        box_2D9A6.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_2D9A6.label(text='Light 9', icon_value=302)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'type', text='Light type', icon_value=0, emboss=True)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'color', text='Color', icon_value=0, emboss=True)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'energy', text='Power', icon_value=328, emboss=True)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_2D9A6.prop(bpy.data.lights['Area.008'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_2D9A6.prop(bpy.data.objects['Area.008'], 'scale', text='Scale', icon_value=0, emboss=True)
        box_49D39 = layout.box()
        box_49D39.alert = False
        box_49D39.enabled = True
        box_49D39.active = True
        box_49D39.use_property_split = False
        box_49D39.use_property_decorate = False
        box_49D39.alignment = 'Expand'.upper()
        box_49D39.scale_x = 1.0
        box_49D39.scale_y = 1.0
        box_49D39.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_49D39.label(text='Light 10', icon_value=302)
        box_49D39.prop(bpy.data.lights['Area.009'], 'type', text='Light type', icon_value=0, emboss=True)
        box_49D39.prop(bpy.data.lights['Area.009'], 'shape', text='Shape', icon_value=0, emboss=True)
        box_49D39.prop(bpy.data.lights['Area.009'], 'color', text='Color', icon_value=0, emboss=True)
        box_49D39.prop(bpy.data.lights['Area.009'], 'energy', text='Power', icon_value=328, emboss=True)
        box_49D39.prop(bpy.data.lights['Area.009'], 'shadow_soft_size', text='Radius', icon_value=328, emboss=True)
        box_49D39.prop(bpy.data.lights['Area.009'], 'spread', text='Spread', icon_value=0, emboss=True)
        box_49D39.prop(bpy.data.objects['Area.009'], 'scale', text='Scale', icon_value=0, emboss=True)


class SNA_OT_Random_Colors_2741E(bpy.types.Operator):
    bl_idname = "sna.random_colors_2741e"
    bl_label = "Random colors"
    bl_description = "Add random colors to your scene lights"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        select_all_lights()
        for light in selected_objects():
            r = uniform(0,1)
            g = uniform(0,1)
            b = uniform(0,1)
            light.data.color = [r,g,b]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_SETUP__90EB3(bpy.types.Panel):
    bl_label = 'Setup '
    bl_idname = 'SNA_PT_SETUP__90EB3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Lightz'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_18C18 = layout.box()
        box_18C18.alert = False
        box_18C18.enabled = True
        box_18C18.active = True
        box_18C18.use_property_split = False
        box_18C18.use_property_decorate = False
        box_18C18.alignment = 'Expand'.upper()
        box_18C18.scale_x = 1.0
        box_18C18.scale_y = 1.0
        box_18C18.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = box_18C18.operator('sna.light_it_up_c570f', text='Light it up!', icon_value=302, emboss=True, depress=False)
        op = box_18C18.operator('sna.random_colors_2741e', text='Random colors', icon_value=627, emboss=True, depress=False)


class SNA_PT_SUPPORT_19CE6(bpy.types.Panel):
    bl_label = 'Support'
    bl_idname = 'SNA_PT_SUPPORT_19CE6'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Lightz'
    bl_order = 2
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_61700 = layout.box()
        box_61700.alert = False
        box_61700.enabled = True
        box_61700.active = True
        box_61700.use_property_split = False
        box_61700.use_property_decorate = False
        box_61700.alignment = 'Expand'.upper()
        box_61700.scale_x = 1.0
        box_61700.scale_y = 1.0
        box_61700.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = box_61700.operator('wm.url_open', text='Patreon', icon_value=_icons['patreon-logo-png-badge-7.webp'].icon_id, emboss=True, depress=False)
        op.url = 'https://www.patreon.com/JishuArtz'
        op = box_61700.operator('wm.url_open', text='Gumroad', icon_value=load_preview_icon(r'C:\Users\india\Downloads\gumroad-logo-3A93C7330E-seeklogo.com.png'), emboss=True, depress=False)
        op.url = 'https://jishuartz.gumroad.com/'


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_OT_Light_It_Up_C570F)
    bpy.utils.register_class(SNA_PT_INDIVIDUAL_SETTINGS_C0512)
    bpy.utils.register_class(SNA_OT_Random_Colors_2741E)
    bpy.utils.register_class(SNA_PT_SETUP__90EB3)
    bpy.utils.register_class(SNA_PT_SUPPORT_19CE6)
    if not 'patreon-logo-png-badge-7.webp' in _icons: _icons.load('patreon-logo-png-badge-7.webp', os.path.join(os.path.dirname(__file__), 'icons', 'patreon-logo-png-badge-7.webp'), "IMAGE")


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Light_It_Up_C570F)
    bpy.utils.unregister_class(SNA_PT_INDIVIDUAL_SETTINGS_C0512)
    bpy.utils.unregister_class(SNA_OT_Random_Colors_2741E)
    bpy.utils.unregister_class(SNA_PT_SETUP__90EB3)
    bpy.utils.unregister_class(SNA_PT_SUPPORT_19CE6)
