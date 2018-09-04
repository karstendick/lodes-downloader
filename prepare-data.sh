#!/usr/bin/env bash


# add auxormain flag based on aux/main in file name
for file in ./*aux*
do
    cat $file | awk -F, '{if (NR==1) print $0 FS "auxormain"; else print $0 FS "aux"}' > modified/$file
done

for file in ./*main*
do
    cat $file | awk -F, '{if (NR==1) print $0 FS "auxormain"; else print $0 FS "main"}' > modified/$file
done


# add segment column based on segment in file name
for segment in {S000,SA01,SA02,SA03,SE01,SE02,SE03,SI01,SI02,SI03}
do
    for file in *ac_${segment}*
    do
        cat $file | awk -F, -v segment=$segment '{if (NR==1) print $0 FS "segment"; else print $0 FS segment}' > modified/$file
    done
done


# add year column based on year in file name
for year in {2002..2015}
do
    for file in *${year}*
    do
        cat $file | awk -F, -v year=$year '{if (NR==1) print $0 FS "year"; else print $0 FS year}' > modified_with_year/$file
    done
done
