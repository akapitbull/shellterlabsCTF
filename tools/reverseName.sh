for file in *;do mv $file $( echo $file | rev );echo "$file | $(echo $file | rev)";done && echo [+]Finish!
