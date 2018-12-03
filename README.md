# OST-Python: Open Summarization Toolbox
> A C++ implementation of OST can be found [here](https://github.com/leanbalma/OST).

Open Summarization Toolbox (OST) is an open evaluation framework for video summarization. OST is compatible with existing datasets and published results.

`ost-python` is available in the Python Package Index and can be installed using `pip`:

```
pip install ost-python
```

## How to use it
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
