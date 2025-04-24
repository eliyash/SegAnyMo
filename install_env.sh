pip install -r requirements.txt
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121

cd sam2
pip install -e .
cd ..

cd preproc/tapnet
pip install .

cd ../..
