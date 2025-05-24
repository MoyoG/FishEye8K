

```bash
docker pull ganzobtn:aicity_iccv_2025_track4:latest
```

```bash
docker build -f Dockerfile.jetson -t aicitychallenge/iccv_2025_track4_team_1:latest .
```

```bash
t=aicitychallenge/iccv_2025_track4_team_1:latest
sudo docker run -it --ipc=host --runtime=nvidia -v your_data_folder:/data  $t
```

<!-- ```bash
python run_evaluation.py
``` -->