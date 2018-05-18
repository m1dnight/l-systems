#!/bin/bash

echo "Generating Dragon Curve.."
python dragon_curve.py

echo "Generating Fractal Plant.."
python fractal_plant.py

echo "Generating Fractal Tree.."
python fractal_tree.py

echo "Generating Stochastic Fractal Tree.."
python fractal_tree_stochastic.py

echo "Done. Generated following outputs:"

ls *.jpg