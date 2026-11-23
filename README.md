# Embedding Neighbor Search

Find nearest images from precomputed vision embeddings.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `{"query.jpg":[0.1,0.2],"other.jpg":[0.2,0.3]}`

Run: `python main.py embeddings.json query.jpg 5`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

DINOv2 or any embedding model exporting vectors as JSON. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

Embeddings must already exist. This tool searches them without loading a vision model. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.

## License

MIT. See `LICENSE`.
