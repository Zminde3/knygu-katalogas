# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['book_catalog\\run.py'],
    pathex=[],
    binaries=[],
    datas=[('book_catalog\\\\templates', 'book_catalog\\\\templates'), ('book_catalog\\\\static', 'book_catalog\\\\static'), ('book_catalog\\\\books.db', 'book_catalog')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
