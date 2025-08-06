pipeline {
    agent {
        docker { image 'python:3.11-slim' }
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up...'
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Email Validator') {
            steps {
                echo 'Running email validator script...'
                sh '. venv/bin/activate && python email_validator.py'
            }
        }
    }
}
