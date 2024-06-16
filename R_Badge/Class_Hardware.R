library(readxl)
library(ggplot2)
library(tidyverse)

data=read_excel("/Users/lucyshichman/Desktop/MSDS-Orientation/MSDS-Orientation-Computer-Survey.xlsx")
head(data)

# changing column names
colnames(data)<-c("Timestamp",
                  "UVA_ID",
                  "Github_ID",
                  "OS",
                  "CPU_Rate",
                  "CPU_Cores",
                  "RAM",
                  "Hard_Drive",
                  "GPU_type",
                  "GPU_Cores")
summary(data)

# remove duplicate rows and outlier row
data= data %>% 
  slice(-1) %>% # remove first row
  distinct() # removed 62 rows

# Timestamp
ggplot(data,aes(x=Timestamp))+
  geom_histogram(fill="light green")+
  theme_light()+
  ggtitle("Distibution of Survey Submission Times")

#UVA_ID
sum(is.na(data$UVA_ID)) # 259 responses, 61 NaN
n_distinct(data$UVA_ID) # 250 unique responses

#Github_ID
sum(is.na(data$Github_ID)) # 244 responses, 76 NaN
n_distinct(data$Github_ID) # 234 unique responses

#OS
table(data$OS)
data$OS=str_replace(data$OS,"Windows 10","Windows")
data$OS=str_replace(data$OS,"Any Linux","Linux")
data$OS=str_replace(data$OS,"All of the above","Multiple")
data$OS=str_replace(data$OS, "I use Mac and Linux","Multiple")
data$OS=str_replace(data$OS,"Windows (by professional necessity), MacOS (by personal choice)","Multiple")
data=data%>%
  slice(-216)
# replacement not working, remove row

ggplot(data,aes(x=OS))+
  geom_bar(fill="darkgreen")+
  theme_light()+
  ggtitle("Distribution of Operating Systems")

#CPU_Rate
ggplot(data,aes(x=CPU_Rate))+
  geom_histogram(fill="purple")+
  theme_light()+
  xlim(0,6)+ # edit x lim to exclude outliers
  ggtitle("Distirbution of CPU Cycle Rate (in GHz)")

# CPU_Cores
ggplot(data,aes(x=CPU_Cores))+
  geom_histogram(fill="light blue")+
  theme_light()+
  ggtitle("Distribution of Number of CPU Cores")

# RAM
ggplot(data,aes(x=RAM))+
  geom_histogram(fill="pink")+
  theme_light()+
  ggtitle("Distribution of RAM (in GB)")

# Hard_Drive
ggplot(data,aes(x=Hard_Drive))+
  geom_histogram(fill="maroon")+
  theme_light()+
  ggtitle("Distribution of Hard Drive Size (in GB)")

# GPU_type
sum(is.na(data$GPU_type)) # no NaN
n_distinct(data$GPU_type) # 195 unique responses

# GPU_Cores
ggplot(data,aes(x=GPU_Cores))+
  geom_histogram(fill="chartreuse")+
  theme_light()+
  ggtitle("Distribution of Number of GPU Cores")
