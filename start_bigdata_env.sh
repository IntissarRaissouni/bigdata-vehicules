#!/bin/bash

# === ENVIRONNEMENT ===
export HADOOP_HOME=$HOME/hadoop-3.3.6
export SPARK_HOME=$HOME/spark-3.5.0-bin-hadoop3
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$PATH
export FLASK_APP=superset

# === DÉMARRER HADOOP (HDFS) ===
echo "✅ Démarrage de HDFS..."
$HADOOP_HOME/sbin/start-dfs.sh

# === DÉMARRER SPARK (optionnel) ===
echo "✅ Démarrage de Spark..."
$SPARK_HOME/sbin/start-all.sh

# === DÉMARRER POSTGRESQL ===
echo "✅ Démarrage de PostgreSQL..."
sudo systemctl start postgresql@14-main

# === DÉMARRER SUPERSET ===
echo "✅ Lancement de Superset..."
superset run -h 0.0.0.0 -p 8088 --with-threads --reload
