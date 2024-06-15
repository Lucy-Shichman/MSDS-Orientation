library(readxl)
data=read_excel("/Users/lucyshichman/Desktop/MSDS-Orientation/MSDS-Orientation-Computer-Survey.xlsx")
head(data)
colnames(data)<-c("Timestamp","UVA_ID","Github_ID","OS","CPU_Rate","CPU_Cores","RAM","Hard_Drive","GPU_type","GPU_Cores")
hist(data$CPU_Cores,
     main="CPU Cores on MSDS Laptops",
     xlab= "# of CPU Cores",
     col="light blue")
