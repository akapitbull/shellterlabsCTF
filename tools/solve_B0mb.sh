#!/bin/bash

for n1 in $(seq 999);do if ./$1 <<< $(echo $n1) | grep second ;then for n2 in $(seq 999);do if ./$1 <<< $(echo $n1 && echo $n2) | grep third;then for n3 in $(seq 999);do if ./$1 <<< $(echo $n1 && echo $n2 && echo $n3) | grep shellter;then echo "[+] $n1 | $n2 | $n3";break;fi;done;break;fi;done;break;fi;done
