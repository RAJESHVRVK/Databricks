# Databricks notebook source
x = 5
print(x)

# COMMAND ----------

 df=spark.read.csv('/FileStore/tables/EmployeesData.csv', header=True) 
 df.show() 
