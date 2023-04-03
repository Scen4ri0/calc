pipeline{
	agent any
	
	triggers{
		githubPush()
	}
	
	stages {
		stage('Checkout'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Scen4ri0/calc']]]) 
			}
		}
	
		stage ('build'){
			steps{
				sh 'docker build -t calculator:latest .'
			}
		}
	
		stage('test'){
			steps{
				sh 'docker run -d -p 8000:8000 calculator'
				sh 'sleep 60'
				sh 'curl -d "num1=10&num2=13" -X POST http://localhost:8000/multiply'
				sh 'docker stop $(docker ps -q --filter ancestor=calculator)'
			}	
		}	
	}
}


