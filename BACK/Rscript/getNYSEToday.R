args<-commandArgs(TRUE)
today <- args

library(tseries)
library(xts)
stockName <- 'BABA'
stockTable <- na.omit(as.xts(get.hist.quote(instrument=stockName,
                                            provider=c("yahoo"),
                                            start=today,
                                            quote=c("Open"))))
stockTable[1,]

#colnames(stockTable[,1])
#rownames(stockTable[,])
#stockTable[,1]
