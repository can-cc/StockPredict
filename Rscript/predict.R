args<-commandArgs(TRUE)
stockName <- args
library(xts)
library(tseries)
library(quantmod)

stockTable <- as.xts(get.hist.quote(stockName,
                                    quote=c("Open", "High", "Low", "Close","Volume","AdjClose")))
colnames(stockTable) <- c("Open", "High", "Low", "Close","Volume","Adjusted")
stocklen = nrow(stockTable)

T.ind <- function(quotes,tgt.margin=0.025,n.days=10) {
  v <- apply(HLC(quotes),1,mean)
  
  r <- matrix(NA,ncol=n.days,nrow=NROW(quotes))
  for(x in 1:n.days) r[,x] <- Next(Delt(v,k=x),x)
  
  x <- apply(r,1,function(x) sum(x[x > tgt.margin | x < -tgt.margin]))
  if (is.xts(quotes)) xts(x,time(quotes)) else x
}


myATR <- function(x) ATR(HLC(x))[,'atr']
mySMI <- function(x) SMI(HLC(x))[,'SMI']
myADX <- function(x) ADX(HLC(x))[,'ADX']
myAroon <- function(x) aroon(x[,c('High','Low')])$oscillator
myBB <- function(x) BBands(HLC(x))[,'pctB']
myChaikinVol <- function(x) Delt(chaikinVolatility(x[,c("High","Low")]))[,1]
myCLV <- function(x) EMA(CLV(HLC(x)))[,1]
myEMV <- function(x) EMV(x[,c('High','Low')],x[,'Volume'])[,2]
myMACD <- function(x) MACD(Cl(x))[,2]
myMFI <- function(x) MFI(x[,c("High","Low","Close")], x[,"Volume"])
mySAR <- function(x) SAR(x[,c('High','Close')]) [,1]
myVolat <- function(x) volatility(OHLC(x),calc="garman")[,1]

data.model <- specifyModel(T.ind(stockTable) ~ Delt(Cl(stockTable),k=1) + myATR(stockTable) + myADX(stockTable) +    myEMV(stockTable) + myVolat(stockTable)  + myMACD(stockTable) + mySAR(stockTable) + runMean(Cl(stockTable)) )
Tdata.train <- as.data.frame(modelData(data.model))
form = paste("T.ind.", 'stockTable', " ~ .", sep="")
Tform <- as.formula(form)

#library(RMySQL)
#library(DBI)
#conn <- dbConnect(MySQL(), dbname = "stockPredict", username="root", password="root", host="127.0.0.1",port=3306)


library(DMwR)
library(nnet)
norm.data <- scale(Tdata.train)
nn <- nnet(Tform,norm.data,size=10,decay=0.01,maxit=1000,linout=T,trace=F)
unscale(predict(nn, Tdata.train[nrow(Tdata.train),]), norm.data)
