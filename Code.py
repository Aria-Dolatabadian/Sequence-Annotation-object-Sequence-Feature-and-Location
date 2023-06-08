from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio import SeqFeature
from Bio.SeqFeature import SeqFeature,FeatureLocation
# from Bio import SeqFeature and from Bio.SeqFeature import SeqFeature,FeatureLocation can not be on at the same time (related to line 35)
#work on random sequences
simple_seq= Seq ('ACGACGACAGCATACTCTACAGCGACGACGACAGCTACTACATCTACAAGCAGACA'
                 'GATAGAGAGAGATATATACTCTACAGGACAGAGAGAGAGAGCAGCAGACGACTATT'
                 'TATATAGAGAGATACAGATAGACAGTTGGCATAGAGTGACAGAGGGGTTTTGGACG'
                 'CAGATGACAGATGAGAGAGATATATAGTGTGCAGATGGCGCGTAGAGAGAGAGTTG')
sample_seq_r = SeqRecord(simple_seq, id="ARIA1234", features=['Gene'])
print(sample_seq_r.id)
print(sample_seq_r.features)
#import a FASTA file
record =SeqIO.read('sequence.fasta','fasta')
print(record)
#or
print(record.features)
print(record.id)
print(record.description)
print(record.seq)
print(record.dbxrefs)
print(record.annotations)
#import a gb file
record1 =SeqIO.read('sequence.gb','genbank')
print(record1)
print(record1.seq)
print(record1.dbxrefs)
print(record1.annotations)
print(record1.features)
#Sequence location
# start_pos = SeqFeature.AfterPosition(5)
# end_pos = SeqFeature.BetweenPosition(9, left=8, right=9)
# my_location = SeqFeature.FeatureLocation(start_pos, end_pos)
# print(my_location)
#accessng location
my_snp = 4350
for feature in record1.features:
    if my_snp in feature:
        print(feature.type, feature.qualifiers.get('db_xref'))
feature = SeqFeature(FeatureLocation(5,18),type='gene',strand=-1)
feature_seq = record1.seq[feature.location.start:feature.location.end].reverse_complement()
print(feature_seq)
print(len(feature_seq))
print(feature.location)
