# OST-Python: Open Summarization Toolbox
> A C++ implementation of OST can be found [here](https://github.com/leanbalma/OST).

Open Summarization Toolbox (OST) is an open evaluation framework for video summarization. OST is compatible with existing datasets and published results.

`ost-python` is available in the Python Package Index and can be installed using `pip`. __Python 3__ is required to run `ost-python`:

```
pip3 install ost-python
```

## How to use it
You can edit the following parameters:

* Method (`--method`): besides running our evaluation method, you can also run CUS specifing `cus` instead of `bhi` for this parameter.
* Epsilon (`--epsilon`): value that determines the maximum distance between the histograms of two matched keyframes. Recommended value: 0.4
* Distance (`--distance`): maximum distance (in frames number) between the two keyframes that will be compared. Recommended value: 120.
* Reference path (`--automatic_summarization`): path to the method keyframes.
* User path (`--users_summarization`): path to the user keyframes.
* Reference path H5 (`--automatic_summary_path`): Automatic summary path in the h5 file.
* User path H5 (`--user_summary_path`): User summary path in the h5 file.
* Video path (`--original_video`): path to the original video.

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


## Contributors

* Aggio, Santiago [ slaggio@criba.edu.ar ]
* Balmaceda, Leandro [ balmacedalm@gmail.com ]
* Diaz, Ariel [ arielivandiaz@gmail.com ]
* Iparraguirre, Javier [ j.iparraguirre@computer.org ]
* Rostagno, Adrian [ arostag@frbb.utn.edu.ar ]


## License

This project is licensed and distributed under the GNU General Public License v3.
