# JUDGE MODEL SECURITY


**Objectif :** Ce projet a pour but de mettre sur pied un judge model, tester sa sécurité. Par la suite nous allons introduire un gardian pour renforcer cette sécurité afin de voir comment il réagit. 



## I. PREREQUIS
Il faut aussi avoir installé et configuré le necessaire suivant :
- Ollama (en fonction de votre système d'exploitation) ;
- Python version 3 et pip version 3 ;
- ollama pour python (pip install ollama)


### II. TESTS
En guise de démo, il suffit d'exécuter l'ensemble des scripts ci-dessous pour voir comment le modèle se comporte. 

1- Tests initiaux
```powershell
# Le premier consiste à observer le fonctionnement normale de llama
python '.\Tests initiaux\test_ollama.py'

# Le second c'est le fonctionnement d'un judge model
python '.\Tests initiaux\judge_basic.py'

# Le troisième c'est le fonctionnement d'un guardien
python '.\Tests initiaux\guard_test.py'
```



2- Tests profonds
```powershell
# Le premier consiste à observer le fonctionnement de llama dans un cas malveillant
python '.\Tests finaux\test_cases.py'

# Le second c'est le fonctionnement de llama et llama-guard dans un contexte malveillant
python '.\Tests finaux\benchmark.py'
```

**NB:** Ce travail a été fait à titre purement éducatif, c'est la raison pour laquelle aucun payload n'est présenté ici. Il a aussi pour but de montrer l'utilisation des modèles accessibles. 

>**Il est très important de ne pas essayer de reproduire ceci sur des systèmes dont vous n'êtes pas l'unique proprietaire ou sur des systèmes sur lesquelles vous n'avez reçu aucunes autorisations écrite pour effectuer ces tests.** 
