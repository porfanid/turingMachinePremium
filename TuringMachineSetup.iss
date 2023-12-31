; Script for Inno Setup
; Create an installer for TuringMachine.pro

[Setup]
AppName=TuringMachine.pro
AppVersion=1.0
DefaultDirName={pf}\TuringMachine.pro
DefaultGroupName=TuringMachine.pro
OutputDir=Output
PrivilegesRequired=lowest ; Set to "lowest" to avoid admin rights requirement

[Files]
Source: "turingmachine.pro.exe"; DestDir: "{app}"
Source: "turingmachine.pro.jpg"; DestDir: "{app}"

[Run]
Filename: "{app}\turingmachine.pro.exe"; Description: "Launch TuringMachine.pro"; Flags: postinstall skipifsilent

[Icons]
Name: "{commondesktop}\TuringMachine.pro"; Filename: "{app}\turingmachine.pro.exe"; WorkingDir: "{app}"; IconFilename: "{app}\turingmachine.pro.jpg"
