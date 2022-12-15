# mHealth_windows

Generate windows from mHealth dataset (available at: http://archive.ics.uci.edu/ml/datasets/mhealth+dataset), only including right-lower-arm sensors (9 in total) and the activities L1-L12. One can specify the desired samples per window and the overlapping as arguments.

Usage:

To generate windows of size 128 with 50% overlapping, and return clients data separately. Then the command should be:

```
python main.py --ws 128 --ov 50 -c 
```

To merge all clients data into a single array, then the "-c" argument should be removed. That is:

```
python main.py --ws 128 --ov 50
```
