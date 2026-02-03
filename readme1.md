Prerequisites
Ubuntu
Python 3.12
Virtual environment already created (temp/)
Required Python packages already installed:

    sudo apt update
    sudo apt install python3-pip
    sudo apt install python3.12-venv 
    sudo apt install exiftool   or sudo apt install -y exiftool

    pyulog
    pandas
    numpy
    pytz
            python -m pip install pyulog pandas numpy pytz 
            - This must be installed inside the Python Environment venv

            Or this
            python -m pip install --upgrade pip
            python -m pip install pyulog pandas numpy pytz  


exiftool installed system-wide

Tanay_01-14-26/
│
├── log_27_2026-1-13-11-15-06.ulg
├── 101SIYI_IMG/          # Original images (untouched)
├── 101SIYI_IMG_GEO/      # Output images (with metadata)
│
├── extract_ulog.py
├── gps_utc.py
├── sample_every_3s.py
├── assign_images.py
├── write_exif.py
│
├── gps.csv
├── gps_utc.csv
├── attitude.csv
├── sampled_metadata.csv
├── image_metadata.csv
│
└── temp/                 # Python virtual environment


create venv
    python3 -m venv temp - temp is sample folder name to be created
    source temp/bin/activate  - run the venv ( Python Environment )

Run the Following Pycode in Order:
    1. python extract_ulog.py
            Result:
                gps.csv
                attitude.csv
    2. python gps_utc.py
            Result:
                gps_utc.csv
    3. python sample_every_3s.py  - Modify time as needed
            Result:
                sampled_metadata.csv
    4. python assign_images.py
        Create folder : 101SIYI_IMG_GEO - This is so the Orignal image is untouched
            Result: 
                101SIYI_IMG_GEO/image_metadata.csv
    5. python write_exif.py
            Result:
                101SIYI_IMG_GEO/*.JPG  -> Images now injected with GPS and Date/Time
                
    1. python run_pipeline.py
            - This will automate all the 5 previous steps as long as there already a folder created for the output images with injected metadata
                
            - Must be inside Python Environment already before executing this!
            
            - Wait for the last command to finished executing. 
            Then check the images generated if the files were injected properly

Verify Metadata
    exiftool 101SIYI_IMG_GEO/$(ls 101SIYI_IMG_GEO | head -n 1)
