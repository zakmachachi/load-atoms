from pathlib import Path

from generate_page import DATASETS, DOC_SOURCE, build_datasets_index, build_page

if __name__ == "__main__":
    for file in (DOC_SOURCE / "datasets").glob("*.rst"):
        file.unlink()
    for dataset_id in DATASETS:
        build_page(dataset_id)
    build_datasets_index()
