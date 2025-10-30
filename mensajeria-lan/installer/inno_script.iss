\
        [Setup]
        AppName=MensajeriaLAN
        AppVersion=1.0
        DefaultDirName={pf}\MensajeriaLAN
        DefaultGroupName=MensajeriaLAN
        OutputBaseFilename=MensajeriaLAN_Installer
        Compression=lzma
        SolidCompression=yes

        [Files]
        Source: "..\client\dist\MensajeriaLAN.exe"; DestDir: "{app}"; Flags: ignoreversion

        [Icons]
        Name: "{group}\MensajeriaLAN"; Filename: "{app}\MensajeriaLAN.exe"
        Name: "{commondesktop}\MensajeriaLAN"; Filename: "{app}\MensajeriaLAN.exe"
