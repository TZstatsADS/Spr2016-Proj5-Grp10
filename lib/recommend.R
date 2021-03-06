

recommend <- function(timestr){
  weekday <- strsplit(timestr,',')[[1]][1]
  hour <- strsplit(timestr,',')[[1]][2]
  if(weekday=="Monday"){day<-0}
  if(weekday=="Tuesday"){day<-1}
  if(weekday=="Wednesday"){day<-2}
  if(weekday=="Thursday"){day<-3}
  if(weekday=="Friday"){day<-4}
  time <- day*96+as.numeric(hour)*4
  Architectural_Fine_Arts_Library <- data.frame(Architectural_Fine_Arts_Library_1_final_spr_2015[time,"count"],Architectural_Fine_Arts_Library_2_final_spr_2015[time,"count"],Architectural_Fine_Arts_Library_3_final_spr_2015[time,"count"],Architectural_Fine_Arts_Library_1_final_fall_2014[time,"count"],Architectural_Fine_Arts_Library_2_final_fall_2014[time,"count"],Architectural_Fine_Arts_Library_3_final_fall_2014[time,"count"],Architectural_Fine_Arts_Library_1_final_fall_2015[time,"count"],Architectural_Fine_Arts_Library_2_final_fall_2015[time,"count"],Architectural_Fine_Arts_Library_3_final_fall_2015[time,"count"])
  avg_arch = mean(t(Architectural_Fine_Arts_Library)[,1])/max(t(Architectural_Fine_Arts_Library)[,1])
  
  Butler <- data.frame(Butler_2_fall_2014[time,"count"],Butler_3_fall_2014[time,"count"],Butler_4_fall_2014[time,"count"],Butler_5_fall_2014[time,"count"],Butler_6_fall_2014[time,"count"],Butler_2_fall_2015[time,"count"],Butler_3_fall_2015[time,"count"],Butler_4_fall_2015[time,"count"],Butler_5_fall_2015[time,"count"],Butler_6_fall_2015[time,"count"],Butler_2_spr_2015[time,"count"],Butler_3_spr_2015[time,"count"],Butler_4_spr_2015[time,"count"],Butler_5_spr_2015[time,"count"],Butler_6_spr_2015[time,"count"])
  avg_but = mean(t(Butler)[,1])/max(t(Butler)[,1])
  Lehman <- data.frame(Lehman_2_fall_2014[time,"count"],Lehman_3_fall_2014[time,"count"],Lehman_2_spr_2015[time,"count"],Lehman_3_spr_2015[time,"count"],Lehman_2_fall_2015[time,"count"],Lehman_3_fall_2015[time,"count"])
  avg_leh = mean(t(Lehman)[,1])/max(t(Lehman)[,1])
  Science_and_Engineering_Library <- data.frame(Science_and_Engineering_Library_final_fall_2014[time,"count"],Science_and_Engineering_Library_final_spr_2015[time,"count"],Science_and_Engineering_Library_final_fall_2015[time,"count"])
  avg_noco = mean(t(Science_and_Engineering_Library)[,1])/max(t(Science_and_Engineering_Library)[,1])
  Starr_East_Asian_Library <- data.frame(Starr_East_Asian_Library_final_fall_2014[time,"count"],Starr_East_Asian_Library_final_spr_2015[time,"count"],Starr_East_Asian_Library_final_fall_2015[time,"count"])
  avg_starr = mean(t(Starr_East_Asian_Library)[,1])/max(t(Starr_East_Asian_Library)[,1])
  Uris <- data.frame(Uris_fall_2014[time,"count"],Uris_fall_2015[time,"count"],Uris_spr_2015[time,"count"])
  avg_uris = mean(t(Uris)[,1])/max(t(Uris)[,1])
  result <- data.frame(c("Avery","Butler","Lehman","NOCO","Starr","Uris"),c(avg_arch,avg_but,avg_leh,avg_noco,avg_starr,avg_uris))
  names(result) <- c('location','occupancy')
  return(result[with(result,order(result$occupancy)),])
}

Architectural_Fine_Arts_Library_1_final_spr_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_1_final_spr_2015.csv")
Architectural_Fine_Arts_Library_2_final_spr_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_2_final_spr_2015.csv")
Architectural_Fine_Arts_Library_3_final_spr_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_3_final_spr_2015.csv")
Architectural_Fine_Arts_Library_3_final_fall_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_3_final_fall_2015.csv")
Architectural_Fine_Arts_Library_3_final_fall_2014 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_3_final_fall_2014.csv")
Architectural_Fine_Arts_Library_2_final_fall_2014 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_2_final_fall_2014.csv")
Architectural_Fine_Arts_Library_2_final_fall_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_2_final_fall_2015.csv")
Architectural_Fine_Arts_Library_1_final_fall_2014 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_1_final_fall_2014.csv")
Architectural_Fine_Arts_Library_1_final_fall_2015 <- read.csv("../output/libraries/Architectural_and_Fine_Arts_Library_1_final_fall_2015.csv")

Butler_3_fall_2014 <- read.csv("../output/libraries/Butler_Library_3_final_fall_2014.csv")
Butler_4_fall_2014 <- read.csv("../output/libraries/Butler_Library_4_final_fall_2014.csv")
Butler_5_fall_2014 <- read.csv("../output/libraries/Butler_Library_5_final_fall_2014.csv") 
Butler_6_fall_2014 <- read.csv("../output/libraries/Butler_Library_6_final_fall_2014.csv")
Butler_6_fall_2015 <- read.csv("../output/libraries/Butler_Library_6_final_fall_2015.csv")
Butler_5_fall_2015 <- read.csv("../output/libraries/Butler_Library_5_final_fall_2015.csv")
Butler_4_fall_2015 <- read.csv("../output/libraries/Butler_Library_4_final_fall_2015.csv")
Butler_2_fall_2015 <- read.csv("../output/libraries/Butler_Library_2_final_fall_2015.csv")
Butler_2_spr_2015 <- read.csv("../output/libraries/Butler_Library_2_final_spr_2015.csv")
Butler_3_spr_2015 <- read.csv("../output/libraries/Butler_Library_3_final_spr_2015.csv")
Butler_4_spr_2015 <- read.csv("../output/libraries/Butler_Library_4_final_spr_2015.csv")
Butler_5_spr_2015 <- read.csv("../output/libraries/Butler_Library_5_final_spr_2015.csv")
Butler_6_spr_2015 <- read.csv("../output/libraries/Butler_Library_6_final_spr_2015.csv")
Butler_stk_spr_2015 <- read.csv("../output/libraries/Butler_Library_stk_final_spr_2015.csv")
Butler_stk_fall_2015 <- read.csv("../output/libraries/Butler_Library_stk_final_fall_2015.csv")
Butler_stk_fall_2014 <- read.csv("../output/libraries/Butler_Library_stk_final_fall_2014.csv")

Science_and_Engineering_Library_final_fall_2015 <- read.csv("../output/libraries/Science_and_Engineering_Library_final_fall_2015.csv")
Science_and_Engineering_Library_final_fall_2014 <- read.csv("../output/libraries/Science_and_Engineering_Library_final_fall_2014.csv")
Science_and_Engineering_Library_final_spr_2015 <- read.csv("../output/libraries/Science_and_Engineering_Library_final_spr_2015.csv")

Starr_East_Asian_Library_final_spr_2015 <- read.csv("../output/libraries/Starr_East_Asian_Library_final_spr_2015.csv")
Starr_East_Asian_Library_final_fall_2014 <- read.csv("../output/libraries/Starr_East_Asian_Library_final_fall_2014.csv")
Starr_East_Asian_Library_final_fall_2015 <- read.csv("../output/libraries/Starr_East_Asian_Library_final_fall_2015.csv")

Uris_fall_2014 <- read.csv("../output/libraries/Uris_final_fall_2014.csv")
Uris_fall_2015 <- read.csv("../output/libraries/Uris_final_fall_2015.csv")
Uris_spr_2015 <- read.csv("../output/libraries/Uris_final_spr_2015.csv")
