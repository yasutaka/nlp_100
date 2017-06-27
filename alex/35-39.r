library(RMeCab)
library(ggplot2)
library(zipfR) #for 39


res <- RMeCabFreq("neko.txt")
res_noun <- res[res[,2]=="名詞",]
nrow(res_noun <- res[res[,2]=="名詞" & res[,4] > 1,])
res_noun[rev(order(res_noun$Freq)),]
res_noun2 <- data.frame(word=as.character(res_noun[,1]),
                        freq=res_noun[,4])
res_noun2 <- subset(res_noun2, rank(-freq)<25)
ggplot(res_noun2, aes(x=reorder(word,freq), y=freq)) +
  geom_bar(stat = "identity", fill="pink") +
  theme_bw(base_size = 10, base_family = "HiraKakuProN-W3") +
  coord_flip()
## first plot will be printed at this point



#### ZIPF exercise 39
ZM = lnre("zm", alpha = 2/3, B = 0.1)
zmsample = rlnre(ZM, n=1000)
print(zmsample)
plot(zmsample, main="ZIPF Frequency Spectrum", col ="red")
## ZIPF plot will be printed at this point


