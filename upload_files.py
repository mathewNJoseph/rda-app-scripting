import argparse
import pathlib
import shutil
import sys
import rdams_client as rc
from time import sleep

def copy_and_overwrite(src_path: pathlib.Path, dst_path: pathlib.Path) -> None:
    """
    Read the entire contents of *src_path* and overwrite *dst_path* with them.

    If *dst_path* doesn't exist it will be created; if it does exist
    it is truncated to zero bytes before writing the new data.
    """
    if not src_path.is_file():
        sys.exit(f"Error: source file '{src_path}' does not exist or is not a file.")

    # Make sure the destination directory exists
    dst_path.parent.mkdir(parents=True, exist_ok=True)

    # Open destination in write-binary mode — this clears it automatically
    with src_path.open("rb") as src, dst_path.open("wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)  # stream in 1-MiB chunks

    print(f"Copied '{src_path}' → '{dst_path}' (overwrote any previous contents).")

files_to_upload = []

for file in files_to_upload:
  """
  get the file
  copy it into the ds0841.1_control.ctl file
  submit it
  SAVED THE ID into dict
  """
  source_file = pathlib.Path(f"../control_files/{file}")
  dest_file = pathlib.Path("./ds0841.1_control.ctl")
  copy_and_overwrite(source_file, dest_file)
  response = rc.submit(dest_file)
  if response['http_response'] != 200:
    print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ")