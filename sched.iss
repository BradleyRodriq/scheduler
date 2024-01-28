[Setup]
AppName=Scheduler_by_Bradley_Rodriguez
AppVersion=1.0
DefaultDirName={pf}\YourAppName
OutputDir=Output
OutputBaseFilename=YourAppNameSetup

[Files]
Source: "build\*"; DestDir: "{app}"

[Icons]
Name: "{commondesktop}\YourAppName"; Filename: "{app}\installer.exe"