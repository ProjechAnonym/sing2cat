def generateClash(port,ui_url,external_tag,key):
    return {
        "clash_api": {
        "external_controller": f"0.0.0.0:{port}",
        "external_ui": "ui",
        "external_ui_download_url": ui_url,
        "external_ui_download_detour": external_tag,
        "secret": f"{key}"
        }
        }