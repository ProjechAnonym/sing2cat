def ClashDash(port,ui_url,key):
    return {
        "clash_api": {
        "external_controller": f"0.0.0.0:{port}",
        "external_ui": ui_url,
        "external_ui_download_url": "https://github.com/MetaCubeX/Yacd-meta/archive/gh-pages.zip",
        "external_ui_download_detour": "select",
        "secret": f"{key}"
        },
        "cache_file": { "enabled": True, "path": "/opt/singbox/cache.db" }
        }