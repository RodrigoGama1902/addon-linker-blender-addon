# AddonLinker

This add-on will simplify the process of linking Blender Add-ons with mklink

# How to install

- Install the zip file

The add-on will be in the "Tool" tab

# Add-on Preferences

- Auto Get Addon Name - When linking and add-on from other folder, the installed add-on name can be suggested by this add-on, you can select between different methods in the "Get Addon Name Mode"
- Get Addon Name Mode - Select the name suggest method
  - Init Info - This method will check the **init**.py info data, and get the add-on name parameter.
  - Directory Name - This method will simply get the directory name of the selected directory
  - Previous Directory Name - This method will simply get the previous directory name of the selected directory

# How to use

- In the add-on panel, input the directory path of the add-on you want to link
- If you have "Auto Get Addon Name" enabled in add-on preferences, the add-on name will be suggested automatically
- You can also manually change the name
- Click in Link add-on
- Restart Blender
- Enable the linked add-on in Blender Preferences
