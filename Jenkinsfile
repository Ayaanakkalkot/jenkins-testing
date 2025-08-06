pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up...'
                sh 'python3 -m venv venv'
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
