#!/usr/bin/env sh
/home/es1video4/caffe/build/tools/caffe train --solver=solver.prototxt 2>&1 | tee ./result/output.txt
