args<-commandArgs(TRUE)
cells <- unlist(strsplit(args, ' '))
stockName <- cells[[1]]
today <- cells[[2]]

library(tseries)
library(xts)

stockName <- 'BABA'
today <- '2015-1-30'
stockTable <- na.omit(as.xts(get.hist.quote(instrument=stockName,
                                            provider=c("yahoo"),
                                            start=today,
                                            quote=c("AdjClose"))))
stockTable[1,]