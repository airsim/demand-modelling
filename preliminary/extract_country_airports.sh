#!/usr/bin/env bash

awk -F'^' '{if ($17 == "FI") {print ($1 "^" $7 "^" $13 "^" $43)}}' ori_por_public.csv  | sort -t'^' -k3gr,3 

