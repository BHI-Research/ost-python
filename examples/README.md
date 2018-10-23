# Evaluator - Examples

This folder contains examples that you can use to easily test the OST's Evaluator.
Before run the examples, install the evaluator dependencies as mentioned in the [evaluator folder](../evaluator).
Then, use `download-data.sh` to download and extract the H5 files and videos that will be used in the examples.

```
$ chmod +x download-data.sh
$ ./download-data.sh
```

Finally, run the scripts that you'll find in each folder.

* half-same-data: the half of the summarization data is the same as the user reference. In this case, F-measure should be 0.5.
* same-data: the summarization data is the same as the user data. In this case, F-measure should be 1.
* non-match-data: there are no matches between the summarization data and the user reference. In this case, F-measure should be 0.
* usual-example: a typical example that we've taken from our results.
