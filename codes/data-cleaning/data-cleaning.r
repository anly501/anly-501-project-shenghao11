library(tidyverse)
library(stringr)

# natural population growth data
popultaion <- read.csv(file = "../../data/00-raw-data/natural-population-growth.csv")
popultaion <- popultaion[,!(names(popultaion) %in% 'Code')]
head(population)

# gdp data
gdp <- read.csv(file = '../../data/00-raw-data/gdp-per-capita-growth.csv')
gdp <- gdp[,!(names(gdp) %in% 'Code')]
head(gdp)

# life data
life <- read.csv(file = '../../data/00-raw-data/life-expectancy.csv')
life <- life[,!(names(life) %in% 'Code')]
head(life)

# death
death <- read.csv(file = '../../data/00-raw-data/annual-number-of-deaths-by-world-region.csv')
death <- death[,!(names(death) %in% 'Code')]
head(death)

# birth
births <- read.csv(file = '../../data/00-raw-data/annual-number-of-births-by-world-region.csv')
births <- births[,!(names(births) %in% 'Code')]
head(births)

# disease
disease <- read.csv(file = '../../data/00-raw-data/dalys-rate-from-all-causes.csv')
disease <- disease[,!(names(disease) %in% 'Code')]
head(disease)

# merge
df<-merge(popultaion,gdp,by=c("Entity","Year"))
df<-merge(df,life,by=c("Entity","Year"))
df<-merge(df,death,by=c("Entity","Year"))
df<-merge(df,births,by=c("Entity","Year"))
df<-merge(df,disease,by=c("Entity","Year"))

df<-df[!duplicated(df),]
dfpast<-df[df$Year<2022,]
dffuture<-df[df$Year>2021,]
write.csv(dfpast,'../../data/01-modified-data/cleaned-population-past-r.csv', row.names = TRUE)
write.csv(dffuture,'../../data/01-modified-data/cleaned-population-future-r.csv', row.names = TRUE)