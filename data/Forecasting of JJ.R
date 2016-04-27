library(tseries)
##The data
jj=read.csv('~/Desktop/project5/john_jay_daily.csv')
jj1=jj$count
##Exploratory Plots
ts.plot(jj1)

rjj=sqrt(jj1)
ts.plot(rjj)

logjj=log(jj1)
ts.plot(logjj)

djj=diff(jj1)
ts.plot(djj)

logdjj=diff(logjj)
ts.plot(logdjj)

logrjj=diff(rjj)
ts.plot(logrjj)

acf(logrjj)
acf(logrjj,type="partial")
spec.pgram(logrjj)
###Suggest ARIMA()
##Therefore for ARIMA model 
##From the PACF, we can suggest AR(7)
model<-arima(rjj,order=c(7,1,1))
model
#aic=4727.21
model1<-arima(rjj,order=c(7,1,2))
model1
#aic=4729.15
model2<-arima(rjj,order=c(7,1,3))
model2
#aic=4730.76
model3<-arima(rjj,order=c(7,1,4))
model3
#aic=4728.24
model4<-arima(rjj,order=c(7,1,5))
model4
#aic=4726.08
model5=arima(rjj,order=c(7,1,6))
model5
#aic=4707.33
model6=arima(rjj,order=c(7,1,7))
model6
##aic=4679.41
model7<-arima(rjj,order=c(7,1,8))
model7
#aic=4677.26
model8=arima(rjj,order=c(7,1,9))
model8
##aic=4681.32
model9<-arima(rjj,order=c(7,1,10))
model9
#aic=4678.09
model10=arima(rjj,order=c(7,1,11))
model10
##AIC=4677.69
model11=arima(rjj,order=c(7,1,12))
model11
##AIC=4679.6
model12=arima(rjj,order=c(7,1,13))
model12
##aic=4679.62


##ARIMA(7,1,11)
res=model7$residuals
ts.plot(res)
acf(res)
acf(res,type="partial")
##We can see from the plot that most of the residuals are within the bounds, so the model fits
a=predict(model7,16)
##capacity of JJ during the next 16 days.
