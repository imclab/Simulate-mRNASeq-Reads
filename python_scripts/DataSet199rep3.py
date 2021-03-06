import makeRandomTestData, os, random

genes = {}
name = '199rep3'
numTranscripts = 5000
randomTrans = 'Random.' + str(numTranscripts) + '.' + name
isoformProb = 90
min = 100
max = 5000

if makeRandomTestData.checkForFasta(randomTrans + '.fa'):
    x = os.remove(randomTrans + '.fa')
for i in range(0, numTranscripts):
    isoform = random.randint(1, 100)
    if isoform <= isoformProb and len(genes) > 2:
        geneSelected = random.choice(genes.keys())
        geneSelectedParts = geneSelected.split(' ')
        geneSelectedId = ''
        for part in geneSelectedParts:
            geneSelectedId += part
        identifier = 'testgene_' + str(i) + ' Isoform_' + geneSelectedId
        thisGeneName, seq = makeRandomTestData.generateIsoforms(identifier, genes[geneSelected], 'random', 0, 0, 0, min, max)
        genes[thisGeneName] = seq
    else:
        thisGeneName =  'testgene_' + str(i) + ' ' + randomTrans
        genes[thisGeneName] = makeRandomTestData.makeKmerCountData(random.randint(101, 4999), 'default')
    complete = makeRandomTestData.outputFastaSeq(randomTrans + '.fa', thisGeneName, genes[thisGeneName])

infileName = randomTrans + '.fa'
filename = 'DataSet' + name
genes = makeRandomTestData.inputFastaSeq(infileName)
errors  = 1

if makeRandomTestData.checkForFasta(filename + 'E1R100G100.fa'):
    x = os.remove(filename + 'E1R100G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.fa'):
    x = os.remove(filename + 'E1R100G100RandomReads.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R100G100RandomReads.txt'):
    x = os.remove(filename + 'E1R100G100RandomReads.txt')
if makeRandomTestData.checkForFasta(filename + 'E1R90G100.fa'):
    x = os.remove(filename + 'E1R90G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R80G100.fa'):
    x = os.remove(filename + 'E1R80G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R70G100.fa'):
    x = os.remove(filename + 'E1R70G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R60G100.fa'):
    x = os.remove(filename + 'E1R60G100.fa')
if makeRandomTestData.checkForFasta(filename + 'E1R50G100.fa'):
    x = os.remove(filename + 'E1R50G100.fa')

count = 0
readLength = 100
numGenes = len(genes)
r90 = int(numGenes * .9)
r80 = int(numGenes * .8)
r70 = int(numGenes * .7)
r60 = int(numGenes * .6)
r50 = int(numGenes * .5)
r40 = int(numGenes * .4)
r30 = int(numGenes * .3)
r20 = int(numGenes * .2)
r10 = int(numGenes * .1)

for key in genes:
    thisGeneName = key
    if len(genes[thisGeneName]) > readLength:
        complete = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100.fa', thisGeneName, genes[thisGeneName])
        level = random.randint(0, 50)
        coverageReq = float(len(genes[thisGeneName])) / float(readLength) * float(level)
        for i in range(0, int(coverageReq)):
            position = random.randint(0,len(genes[thisGeneName])-readLength)
            read = genes[thisGeneName][position:position + readLength]
            identifier1 = key + 'Count' + str(i) + 'Begin' + str(position) + 'End' + str(position + readLength - 1)
            if errors:
                read, identifier1 = makeRandomTestData.addSeqErrorsId(read, identifier1, errors)

            a = makeRandomTestData.outputFastaSeq(filename + 'E1R100G100RandomReads.fa', identifier1, read)
        b = makeRandomTestData.outputGeneCoverage(filename + 'E1R100G100RandomReads.txt', key, 'Random Placement - Number of Reads' + ':' + str(coverageReq), level)

        count += 1

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r90):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R90G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r80):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R80G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r70):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R70G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r60):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R60G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r50):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R50G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r40):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R40G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r30):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R30G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r20):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R20G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)

genes2 = makeRandomTestData.inputFastaSeq(infileName)
for i in range(0, r10):
    thisGeneName = random.choice(genes2.keys())
    complete = makeRandomTestData.outputFastaSeq(filename + 'E1R10G100.fa', thisGeneName, genes2[thisGeneName])
    genes2.pop(thisGeneName)





print 'Finished'
