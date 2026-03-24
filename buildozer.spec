[app]

title = SakinaAI
package.name = sakinaai
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyttsx3

orientation = portrait

fullscreen = 0

android.permissions = RECORD_AUDIO, INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33

[buildozer]

log_level = 2
warn_on_root = 1