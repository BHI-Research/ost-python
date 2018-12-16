# OST-Python: Open Summarization Toolbox
> A C++ implementation of OST can be found [here](https://github.com/leanbalma/OST).

Open Summarization Toolbox (OST) is an open evaluation framework for video summarization. OST is compatible with existing datasets and published results.

# How OSM works
OSM compares the keyframes of a summarization method with the keyframes selected by human users to quantify the quality of the abstraction. The frames are compared extracting a HSV color space histogram. If the correlation between two histograms is higher than a given threshold, the frames are considered equivalent. Five metrics are calculated:

* Cohen's Kappa.
* F-measure coefficient.
* Precision and Recall.
* CUSa and CUSe (as a compatibility feature).

## Installation
`ost-python` is available in the Python Package Index and can be installed using `pip`. __Python 3__ is required.

We highly encourage you to set up a virtual environment before install the dependencies. [Here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) you
can find instructions about how to install and use Virtualenvwrapper.

```
$ mkvirtualenv ost
$ (ost) pip3 install ost-python
```

## How to use it

### CLI

`ost-python` provides a CLI tool that you can use to get your metric using your terminal.

You can specify the following parameters:

* Method (`--method`/`-m`): besides running our evaluation method (`bhi`), you can also run [CUS](https://sites.google.com/site/vsummsite/download) specifing `cus` instead of `bhi` for this parameter. Default Value: `bhi`.
* Epsilon (`--epsilon`/`-e`): value that determines the maximum distance between the histograms of two matched keyframes. Default value: `0.4`
* Distance (`--distance`/`-d`): maximum distance (in frames number) between the two keyframes that will be compared. Default value: `120`.
* Reference path (`--automatic_summarization`/`-a`): path to the method keyframes.
* User path (`--users_summarization`/`-u`): path to the user keyframes.
* Reference path H5 (`--automatic_summary_path`): automatic summary path in the h5 file.
* User path H5 (`--user_summary_path`): user summary path in the h5 file.
* Video path (`--original_video`/`-v`): path to the original video.

Example:

```
$ ost-python -u dataset_users.h5 -a result.h5 -v videos/video_11.mp4 --user_summary_path video_11/user_summary --automatic_summary_path video_11/machine_summary
```

### Python package API

Import the methods you need from the package:

`from ost import prepare_folders, computeCUS, computeBHI`

#### `prepare_folders(uSummary, aSummary, video, aSummaryFramesPath, uSummaryFramesPath)`

#### `computeCUS(epsilon, videoFrames, refPath, predictionPath)`

#### `computeBHI(epsilon, videoFrames, distance, refPath, predictionPath)`


Example:

```python
from ost import computeBHI
import cv2

videoPath = path/to/video
users_summarization = path/to/user/summ/folder
automatic_summarization = path/to/automatic/summ/folder

epsilon = 0.4
distance = 120

cap = cv2.VideoCapture(videoPath)
videoLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

f1, kappa = computeBHI(
    epsilon
    videoLength,
    distance
    users_summarization,
    automatic_summarization
)

print('F1:', f1)
print('Kappa:', kappa)
```

## Supported platforms

We have tested `ost-python` on the following platforms:

* Ubuntu 18.04 LTS
* Fedora 29

## Contributors

* Aggio, Santiago [ slaggio@criba.edu.ar ]
* Balmaceda, Leandro [ balmacedalm@gmail.com ]
* Diaz, Ariel [ arielivandiaz@gmail.com ]
* Iparraguirre, Javier [ j.iparraguirre@computer.org ]
* Rostagno, Adrian [ arostag@frbb.utn.edu.ar ]

## License

This project is licensed and distributed under the GNU General Public License v3.
