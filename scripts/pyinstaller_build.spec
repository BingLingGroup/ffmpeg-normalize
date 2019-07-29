# -*- mode: python -*-

block_cipher = None


a = Analysis([r"..\ffmpeg_normalize\__main__.py",
             r"..\ffmpeg_normalize\__init__.py",
             r"..\ffmpeg_normalize\_cmd_utils.py",
             r"..\ffmpeg_normalize\_errors.py",
             r"..\ffmpeg_normalize\_ffmpeg_normalize.py",
             r"..\ffmpeg_normalize\_logger.py",
             r"..\ffmpeg_normalize\_media_file.py",
             r"..\ffmpeg_normalize\_streams.py",
             r"..\ffmpeg_normalize\_version.py",],
             pathex=[r'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name="ffmpeg-normalize",
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
