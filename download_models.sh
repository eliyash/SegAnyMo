cd sam2/checkpoints
./download_ckpts.sh
cd ../..

cd preproc
mkdir checkpoints
cd checkpoints
wget https://storage.googleapis.com/dm-tapnet/bootstap/bootstapir_checkpoint_v2.pt
cd ..
