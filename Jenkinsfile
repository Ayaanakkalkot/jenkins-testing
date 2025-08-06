pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up...'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Email Validator') {
            steps {
                echo 'Running email validator script...'
                bat 'venv\\Scripts\\activate && python email_validator.py'
            }
        }
    }
}
