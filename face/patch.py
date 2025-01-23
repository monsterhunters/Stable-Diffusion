# Path to the core.py file
file_path = '/facefusion/facefusion/uis/layouts/default.py'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace the line with the updated version
updated_content = content.replace("ui.launch(favicon_path = 'facefusion.ico', inbrowser = state_manager.get_item('open_browser')", "ui.launch(favicon_path = 'facefusion.ico', inbrowser = state_manager.get_item('open_browser'),share=True")

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)
