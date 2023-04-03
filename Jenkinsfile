CODE_CHANGES = getGitChanges()
pipeline{
	agent any
	
	when {
		expression{
			BRANCH_NAME == 'main' && CODE_CHANGES == true
		}
	}
	stages {
		stage('Checkout'){
			steps{
				checkout scm 
			}
		}
	}
	
	stage ('Build'){
		steps{
			sh 'docker build -t calculator:latest .'
		}
	}
	
	stage('Test'){
		steps{
			sh 'docker run -d -p 8000:8000 calculator'
			sh 'sleep 60'
			sh 'curl -d "num1=10&num2=13" -X POST http://localhost:8000/multiply'
			sh 'docker stop $(docker ps -q --filter ancestor=calculator)'
		}	
	}
}


