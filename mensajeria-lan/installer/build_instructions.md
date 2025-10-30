# Cómo crear el instalador
1. Generar el ejecutable:
   ```bash
   pyinstaller --onefile --windowed app.py --name MensajeriaLAN
   ```
2. Copiar `dist/MensajeriaLAN.exe` en esta carpeta.
3. Abrir `inno_script.iss` con Inno Setup Compiler y presionar *Build*.
4. Se generará `MensajeriaLAN_Installer.exe` listo para instalar.
