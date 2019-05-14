# retroflag-picase-tinker
Safe Shutdown Script for Retroflag Pi Case on Tinker Board. 
Works on ROTT 1.0.7 (Amrbian + Retropie 4.4), SUPERPI Case.
Replace gpiozero with Asus GPIO. Use multi_switch.sh.

Turn switch "SAFE SHUTDOWN" to ON.

Install script copy files to /opt/RetroFlag and add SafeShutdownTinker.py to rc.local

User must be 'tinker'.
To install scripts, donwload or clone in your $HOME

cd retroflag-picase-tinker
./install_tinker.sh

System will be restart.

Original Project
https://github.com/RetroFlag/retroflag-picase

-------------------Multi Switch Shutdown-----------------
Multi Switch Shutdown with advanced shutdown features for more natural behaviour:

If you press restart if emulator is currently running, then you will be kicked back to ES main menu.
If you press restart in ES main screen, ES will be restartet (no reboot!), good for quick saving metadata or internal saves.
If you press power-off then Raspberry will shutdown
All metadata is always saved

Multi Switch Shutdown by crcerror at here https://github.com/crcerror/retroflag-picase
