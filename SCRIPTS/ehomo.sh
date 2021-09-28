
awk 'BEGIN{val=1; val2=0}{if(val==2 && $2==0 ){print val2"\n"$0};val=$2;val2=$0}' orca.out | awk '{print $1" "$2" "$4}'
