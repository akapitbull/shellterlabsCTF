for file in *;do mv $file $( echo $file | rev );done
