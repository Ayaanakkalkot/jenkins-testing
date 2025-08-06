pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up...'
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-venv python3-pip
                    python3 --version
                    python3 -m venv venv
                '''
            }
        }

        stage('Run Email Validator') {
            steps {
                echo 'Running email validator...'
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                    python your_script.py
                '''
            }
        }
    }
}
