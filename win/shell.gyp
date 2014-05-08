{
	"targets": [
  {
    "target_name": "MMShellHook",
    "type": "static_library",
    "sources": [
      "MMShellHook.cpp"
    ],
      'msvs_settings': {
        'VCLinkerTool': {
        'EntryPointSymbol': 'DllMainCRTStartup',
            'AdditionalDependencies': [
              'kernel32.lib',
              'gdi32.lib',
              'winspool.lib',
              'comdlg32.lib',
              'advapi32.lib',
              'shell32.lib',
              'ole32.lib',
              'oleaut32.lib',
              'user32.lib',
              'uuid.lib',
              'odbc32.lib',
              'odbccp32.lib',
              'delayimp.lib',
              'credui.lib',
              'netapi32.lib',
            ],
          }
      }
  },
		{
			"target_name": "keylistener",
			"type": "executable",
			"sources": [
				"win.cpp"
			],
      "dependencies": [
        "MMShellHook"
      ],
			'msvs_settings': {
        'VCLinkerTool': {
          'SubSystem': 2,
        'EntryPointSymbol': 'WinMainCRTStartup',
            'AdditionalDependencies': [
              'kernel32.lib',
              'gdi32.lib',
              'winspool.lib',
              'comdlg32.lib',
              'advapi32.lib',
              'shell32.lib',
              'ole32.lib',
              'oleaut32.lib',
              'user32.lib',
              'uuid.lib',
              'odbc32.lib',
              'odbccp32.lib',
              'delayimp.lib',
              'credui.lib',
              'netapi32.lib',
            ],
          }
      }
    },
	]
}