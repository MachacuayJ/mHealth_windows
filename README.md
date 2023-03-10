# mHealth_windows

Generate windows from mHealth dataset (available at: http://archive.ics.uci.edu/ml/datasets/mhealth+dataset), only including right-lower-arm magnetometers and gyroscopes, and chest accelerometers (9 sensors in total). The '0' activty was excluded. One can specify the desired samples per window and the overlapping as arguments.

## Usage

First, clone the repo using the following command:

```
git clone https://github.com/MachacuayJ/mHealth_windows.git
```

Then, move to the donwloaded directory:

```
cd mHealth_windows
```

Install the required dependencies (if they are not already installed):

```
pip install -r requirements.txt
```

Finally, run the "main.py" script specifying the window size (-ws), the overlapping (-ov), and whether merge all clients data or not (if not, include "-c" as argument). For instance, to get the data by clients separately with 128 samples per window and 50% overlapping, use the following command:

```
python main.py -ws 128 -ov 50 -c
```

After running the above command, an "output_data" directory will be created according to the given arguments.
