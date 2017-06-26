library(text2vec)
library(RMeCab)


res <- RMeCab("./neko.txt")
print(res)


# if (res[res[,2]=="名詞",]) {
# print(res))
# }
# print(res_noun)

#it <- itoken(res_noun2, preprocess_function = tolower, tokenizer = word_tokenizer, chunks_number = 10, progessbar = F)

# vocab <- vocabulary(src = res_noun, ngram = c(1L, 1L))
# print( difftime( Sys.time(), t1, units = 'sec'))

# it <- itoken(movie_review[['review']], preprocess_function = tolower, 
#              tokenizer = word_tokenizer, chunks_number = 10, progessbar = F)
# corpus <- create_vocab_corpus(it, vocabulary = vocab)
# dtm <- get_dtm(corpus)
# dim(dtm)


# library(RMeCab)
# library(ggplot2)

# res <- RMeCabFreq("neko.txt")
# res_noun <- res[res[,2]=="名詞",]
# nrow(res_noun <- res[res[,2]=="名詞" & res[,4] > 1,])
# res_noun[rev(order(res_noun$Freq)),]
# res_noun2 <- data.frame(word=as.character(res_noun[,1]),
#                         freq=res_noun[,4])
# res_noun2 <- subset(res_noun2, rank(-freq)<25)
# ggplot(res_noun2, aes(x=reorder(word,freq), y=freq)) +
#   geom_bar(stat = "identity", fill="pink") +
#   theme_bw(base_size = 10, base_family = "HiraKakuProN-W3") +
#   coord_flip()




# library(RMeCab)
# res <- RMeCabC("私の猫です。飲みに行くの？")
# unlist (res)





