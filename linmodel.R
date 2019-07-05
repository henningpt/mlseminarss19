library (Matrix)


# daten einlesen und Modell bauen
df       <- read.csv('df_test_casement.csv', header=T)
df_test  <- df[1:1000, ]
df_train <- df[1001:200, ]
model    <- lm(target.temp ~ temp.1 + temp.2 + temp.3, data=df_train)

test_prediction <- predict(model, newdata=df_test)
plot(df_test$target.temp, (df_test$target.temp - test_prediction) / df_test$target.temp, pch="x", col="blue")	
abline(h=0.05, col="orange")
abline(h=-0.05, col="orange")
summary(model)


png('./hist.png')
hist <- hist((df_test$target.temp - test_prediction) / df_test$target.temp, col="blue", breaks="Scott")
dev.off()

