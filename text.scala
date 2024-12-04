predictionsNew
  .write
  .mode("overwrite")
  .option("header", "true")
  .csv("predictions_new_output")

cleanedTweetsDF
  .write
  .option("header",value=true)
  .mode(saveMode="ignore")
  .csv(path = "C:/Users/CYTech Student/Projet_Scala/csv_output")
