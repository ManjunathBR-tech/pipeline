
pipeline {
  agent any
  stages {
    stage('Checkout:') {
      steps{
         checkout scm
          }
   }    

stage('Build') {
  steps{
    echo 'checking pyhton application'
    bat 'pyhton -m py_compile app.py'
  }
}
stage('test'){
  steps{
    echo 'Executing automated tests'
    bat 'pyhton -m unittest app'
  }
}
stage('Run Application'){
  steps{
    bat 'python app.py'
  }
}
post{
  success{
    echo 'CI pipeline completed succesfully'
  }
  failure{
    echo 'CI pipeline failed'
  }
}
  
