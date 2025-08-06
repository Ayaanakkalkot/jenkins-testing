pipeline {
    agent {
        docker {
            image 'python:3.10'  // or any version you need
        }
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Python Version:'
                sh 'python --version'
            }
        }

        stage('Run Email Validator') {
            steps {
                echo 'Running email validator...'
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python email_validator.py
                '''
            }
        }
    }
}
