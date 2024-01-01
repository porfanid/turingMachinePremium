VENV_PATH = /usr/bin/turingmachine.pro/venv

install:
    # Create directories
    mkdir -p /usr/bin/turingmachine.pro
    mkdir -p /usr/share/applications
    mkdir -p /usr/share/icons

    # Copy files
    cp turingmachine.pro.py /usr/bin/turingmachine.pro
    cp ui_form.py /usr/bin/turingmachine.pro
    cp requirements.txt /usr/bin/turingmachine.pro
    cp ui_license_import.py /usr/bin/turingmachine.pro
    cp turingmachine.pro.jpg /usr/share/icons
    cp turingmachine.pro.desktop /usr/share/applications

    # Create virtual environment
    python3 -m venv $(VENV_PATH)
    $(VENV_PATH)/bin/pip install -r /usr/bin/turingmachine.pro/requirements.txt

    # Set permissions
    chmod +x /usr/bin/turingmachine.pro/turingmachine.pro.py

clean:
    # Clean up
    rm -rf $(VENV_PATH)
