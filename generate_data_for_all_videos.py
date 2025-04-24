import os
from pathlib import Path
import subprocess

if os.name == 'posix':
    dataset_root = Path("/home/ubuntu/datasets/chimp/")
else:
    dataset_root = Path("C:/Workspace/ChimpanzeesThesis/data_local_copy")

video_dir = dataset_root / "per_signal_videos_fixed_interlacing"

# Paths for output directories
motion_seg_dir = video_dir / "res_phase_2"
sam2_dir = video_dir / "sam2dir"

# Ensure output directories exist
motion_seg_dir.mkdir(parents=True, exist_ok=True)
sam2_dir.mkdir(parents=True, exist_ok=True)

# Path to the inference script
script_path = Path("core/utils/run_inference.py")

# Find all .mp4 files in the directory
video_paths = sorted(video_dir.glob("*.mp4"))

for video_path in video_paths[13:]:
    print(f"\nProcessing: {video_path.name}")

    # First command
    cmd1 = [
        "python", str(script_path),
        "--video_path", str(video_path),
        "--depths", "--tracks", "--dinos", "--e"
    ]

    # Second command
    cmd2 = [
        "python", str(script_path),
        "--video_path", str(video_path),
        "--motin_seg_dir", str(motion_seg_dir),
        "--motion_seg_infer", "--e"
    ]

    # Third command
    cmd3 = [
        "python", str(script_path),
        "--video_path", str(video_path),
        "--sam2dir", str(sam2_dir),
        "--motin_seg_dir", str(motion_seg_dir),
        "--sam2", "--e"
    ]


    # Run each command
    for cmd in [cmd1, cmd2, cmd3]:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running command: {' '.join(cmd)}\n{e}")
