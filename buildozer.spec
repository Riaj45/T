[app]
title = Flashlight Pro
package.name = flashlightpro
package.domain = org.flashlightpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.3.0,pyjnius
orientation = portrait
fullscreen = 0

android.permissions = CAMERA,WAKE_LOCK
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
