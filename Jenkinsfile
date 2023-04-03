CODE_CHANGES = getGitChanges()
pipeline{
	agent any
		
	stages {
		stage('Checkout'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Scen4ri0/calc']]]) 
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

	post{
		triggers{
			githubPush()
		}
	}
}


