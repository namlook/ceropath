

BASENAME=$1
CMD_PATH=/Users/namlook/Documents/projets/ceropath/bin

# programs
MUSCLE=$CMD_PATH/muscle3.8.31_i86darwin64
DNADIST=dnadist
DNADIST_CONFIG=$CMD_PATH/dnadist.cfg
BIONJ=$CMD_PATH/BIONJ/BIONJ_MacOS
# $PWD=`pwd`
NWK2SVG=$CMD_PATH/nwk2svg.r

# files
COI_AFA=$CMD_PATH/files/coi_cbgp.afa

$MUSCLE -in $BASENAME -out $BASENAME.afa &&
$MUSCLE -profile -in1 $COI_AFA -in2 $BASENAME.afa -phyiout infile -maxiters 1 -diags &&
cat $DNADIST_CONFIG | $DNADIST &&
$BIONJ outfile $BASENAME.nwk &&
Rscript $NWK2SVG $BASENAME.nwk $PWD &&
rm $BASENAME.afa outfile infile
