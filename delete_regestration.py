import random as r

def delete_line_with_registration(file):
    for line in file.readlines():
        if line.startswith("eNodeB - ID:") and "250;11" not in line:
            print(line.strip(), file=out_file)

with open("LTE_R&S LTE Scanner_[1].txt", 'r') as in_file, \
        open(f"LTE_R&S_Scanner_trans_list_{r.randint(1, 1000)}.txt", "w") as out_file:

    header = """;exported by ROMES LTE BCCH View
;The name is either the name of the station found in the database or in the case no station was found in the data base "eNodeB <eNodeBID/CellID> <PhyCellID>
;Postion of 0.0/0.0 means unknown
;
;Name;Longitude;Latitude;PosErrorDirection;PosErrorLambda1;PosErrorLambda2;IsDirected;Direction;ConfInt;Power;MaxPowerUsedForTowerEstimationbyPE;TowerID;MCC;MNC;TAC;CellIdentity;EARFCN;PhyCellID"""

    print(header, file=out_file)
    delete_line_with_registration(in_file)

